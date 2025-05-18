from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Profile, MatchPreference, MatchRequest, Conversation, Message

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name', 'last_name']
        extra_kwargs = {'password': {'write_only': True}}

class ProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    
    class Meta:
        model = Profile
        fields = '__all__'
        read_only_fields = ['is_verified', 'created_at', 'updated_at']

class MatchPreferenceSerializer(serializers.ModelSerializer):
    class Meta:
        model = MatchPreference
        fields = '__all__'
        read_only_fields = ['profile']

class MatchRequestSerializer(serializers.ModelSerializer):
    sender_name = serializers.SerializerMethodField()
    receiver_name = serializers.SerializerMethodField()
    
    class Meta:
        model = MatchRequest
        fields = '__all__'
        read_only_fields = ['admin_approved', 'created_at', 'updated_at']
    
    def get_sender_name(self, obj):
        return f"{obj.sender.user.first_name} {obj.sender.user.last_name}"
    
    def get_receiver_name(self, obj):
        return f"{obj.receiver.user.first_name} {obj.receiver.user.last_name}"

class ConversationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Conversation
        fields = '__all__'

class MessageSerializer(serializers.ModelSerializer):
    sender_name = serializers.SerializerMethodField()
    
    class Meta:
        model = Message
        fields = '__all__'
        read_only_fields = ['created_at', 'is_read']
    
    def get_sender_name(self, obj):
        return f"{obj.sender.user.first_name} {obj.sender.user.last_name}"

class UserRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    profile = ProfileSerializer(required=False)
    
    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'first_name', 'last_name', 'profile']
    
    def create(self, validated_data):
        profile_data = validated_data.pop('profile', None)
        user = User.objects.create_user(**validated_data)
        
        if profile_data:
            Profile.objects.create(user=user, **profile_data)
        
        return user 