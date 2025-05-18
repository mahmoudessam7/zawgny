from django.shortcuts import render
from rest_framework import viewsets, generics, status, permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from django.db.models import Q
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404

from .models import Profile, MatchPreference, MatchRequest, Conversation, Message
from .serializers import (
    UserSerializer, ProfileSerializer, MatchPreferenceSerializer,
    MatchRequestSerializer, ConversationSerializer, MessageSerializer,
    UserRegistrationSerializer
)

class UserRegistrationView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserRegistrationSerializer
    permission_classes = [permissions.AllowAny]

class CustomAuthToken(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        
        return Response({
            'token': token.key,
            'user_id': user.pk,
            'email': user.email,
            'username': user.username,
            'first_name': user.first_name,
            'last_name': user.last_name,
        })

class ProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    
    def get_queryset(self):
        if self.request.user.is_staff:
            return Profile.objects.all()
        return Profile.objects.filter(user=self.request.user)
    
    @action(detail=False, methods=['get'])
    def my_profile(self, request):
        try:
            profile = request.user.profile
            serializer = self.get_serializer(profile)
            return Response(serializer.data)
        except Profile.DoesNotExist:
            return Response({'detail': 'Profile not found'}, status=status.HTTP_404_NOT_FOUND)
    
    @action(detail=False, methods=['get'])
    def potential_matches(self, request):
        """Return profiles that match the user's preferences."""
        try:
            user_profile = request.user.profile
            user_preferences = user_profile.preferences
            
            # Get opposite gender profiles
            opposite_gender = 'M' if user_profile.gender == 'F' else 'F'
            potential_matches = Profile.objects.filter(
                gender=opposite_gender,
                is_active=True,
                is_verified=True
            ).exclude(user=request.user)
            
            # Filter by preferences if they exist
            if user_preferences:
                # Add preference-based filtering here
                # This is a simple example, you'd want more sophisticated matching
                if user_preferences.country_preference:
                    potential_matches = potential_matches.filter(
                        country=user_preferences.country_preference
                    )
            
            serializer = self.get_serializer(potential_matches, many=True)
            return Response(serializer.data)
        except Profile.DoesNotExist:
            return Response({'detail': 'Profile not found'}, status=status.HTTP_404_NOT_FOUND)

class MatchPreferenceViewSet(viewsets.ModelViewSet):
    queryset = MatchPreference.objects.all()
    serializer_class = MatchPreferenceSerializer
    
    def get_queryset(self):
        if self.request.user.is_staff:
            return MatchPreference.objects.all()
        try:
            return MatchPreference.objects.filter(profile=self.request.user.profile)
        except Profile.DoesNotExist:
            return MatchPreference.objects.none()
    
    def perform_create(self, serializer):
        try:
            serializer.save(profile=self.request.user.profile)
        except Profile.DoesNotExist:
            return Response(
                {'detail': 'Profile not found'},
                status=status.HTTP_400_BAD_REQUEST
            )

class MatchRequestViewSet(viewsets.ModelViewSet):
    queryset = MatchRequest.objects.all()
    serializer_class = MatchRequestSerializer
    
    def get_queryset(self):
        if self.request.user.is_staff:
            return MatchRequest.objects.all()
        try:
            profile = self.request.user.profile
            profile_filter = Q(sender=profile) | Q(receiver=profile)
            return MatchRequest.objects.filter(profile_filter)
        except Profile.DoesNotExist:
            return MatchRequest.objects.none()
    
    def perform_create(self, serializer):
        try:
            sender = self.request.user.profile
            serializer.save(sender=sender)
        except Profile.DoesNotExist:
            return Response(
                {'detail': 'Profile not found'},
                status=status.HTTP_400_BAD_REQUEST
            )
    
    @action(detail=True, methods=['post'])
    def accept(self, request, pk=None):
        match_request = self.get_object()
        
        if match_request.receiver.user != request.user:
            return Response(
                {'detail': 'Not authorized to accept this request'},
                status=status.HTTP_403_FORBIDDEN
            )
        
        match_request.status = 'A'
        match_request.save()
        
        # Create a conversation when request is accepted
        Conversation.objects.create(match_request=match_request)
        
        serializer = self.get_serializer(match_request)
        return Response(serializer.data)
    
    @action(detail=True, methods=['post'])
    def reject(self, request, pk=None):
        match_request = self.get_object()
        
        if match_request.receiver.user != request.user:
            return Response(
                {'detail': 'Not authorized to reject this request'},
                status=status.HTTP_403_FORBIDDEN
            )
        
        match_request.status = 'R'
        match_request.save()
        
        serializer = self.get_serializer(match_request)
        return Response(serializer.data)

class ConversationViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Conversation.objects.all()
    serializer_class = ConversationSerializer
    
    def get_queryset(self):
        if self.request.user.is_staff:
            return Conversation.objects.all()
        try:
            profile = self.request.user.profile
            profile_filter = (
                Q(match_request__sender=profile) | 
                Q(match_request__receiver=profile)
            )
            return Conversation.objects.filter(
                profile_filter,
                match_request__status='A',
                is_active=True
            )
        except Profile.DoesNotExist:
            return Conversation.objects.none()

class MessageViewSet(viewsets.ModelViewSet):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
    
    def get_queryset(self):
        if self.request.user.is_staff:
            return Message.objects.all()
        try:
            profile = self.request.user.profile
            conversation_id = self.request.query_params.get('conversation')
            if conversation_id:
                # Get the conversation first
                profile_filter = Q(match_request__sender=profile) | Q(match_request__receiver=profile)
                conversation = get_object_or_404(
                    Conversation.objects.filter(profile_filter),
                    id=conversation_id,
                    is_active=True
                )
                return Message.objects.filter(conversation=conversation)
            else:
                # Get all messages from active conversations involving the profile
                profile_conversation_filter = (
                    Q(conversation__match_request__sender=profile) | 
                    Q(conversation__match_request__receiver=profile)
                )
                return Message.objects.filter(
                    profile_conversation_filter,
                    conversation__is_active=True
                )
        except Profile.DoesNotExist:
            return Message.objects.none()
    
    def perform_create(self, serializer):
        try:
            conversation_id = self.request.data.get('conversation')
            profile = self.request.user.profile
            
            # Check if the user is part of this conversation
            profile_filter = (
                Q(match_request__sender=profile) | 
                Q(match_request__receiver=profile)
            )
            conversation = get_object_or_404(
                Conversation.objects.filter(profile_filter),
                id=conversation_id,
                is_active=True
            )
            
            serializer.save(
                sender=profile,
                conversation=conversation
            )
        except Profile.DoesNotExist:
            return Response(
                {'detail': 'Profile not found'},
                status=status.HTTP_400_BAD_REQUEST
            )
