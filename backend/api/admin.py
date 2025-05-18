from django.contrib import admin
from .models import Profile, MatchPreference, MatchRequest, Conversation, Message

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'gender', 'city', 'country', 'is_verified', 'is_active')
    list_filter = ('gender', 'marital_status', 'is_verified', 'is_active')
    search_fields = ('user__username', 'user__email', 'city', 'country')
    actions = ['verify_profiles', 'deactivate_profiles', 'activate_profiles']
    
    def verify_profiles(self, request, queryset):
        queryset.update(is_verified=True)
    verify_profiles.short_description = "Mark selected profiles as verified"
    
    def deactivate_profiles(self, request, queryset):
        queryset.update(is_active=False)
    deactivate_profiles.short_description = "Deactivate selected profiles"
    
    def activate_profiles(self, request, queryset):
        queryset.update(is_active=True)
    activate_profiles.short_description = "Activate selected profiles"

@admin.register(MatchPreference)
class MatchPreferenceAdmin(admin.ModelAdmin):
    list_display = ('profile', 'age_range', 'height_range', 'country_preference')
    list_filter = ('age_range', 'education_preference', 'religiosity_preference')
    search_fields = ('profile__user__username', 'country_preference')

@admin.register(MatchRequest)
class MatchRequestAdmin(admin.ModelAdmin):
    list_display = ('sender', 'receiver', 'status', 'admin_approved', 'created_at')
    list_filter = ('status', 'admin_approved')
    search_fields = ('sender__user__username', 'receiver__user__username')
    actions = ['approve_requests', 'reject_requests']
    
    def approve_requests(self, request, queryset):
        queryset.update(admin_approved=True)
    approve_requests.short_description = "Approve selected match requests"
    
    def reject_requests(self, request, queryset):
        queryset.update(admin_approved=False, status='R')
    reject_requests.short_description = "Reject selected match requests"

@admin.register(Conversation)
class ConversationAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'created_at', 'is_active')
    list_filter = ('is_active',)
    search_fields = ('match_request__sender__user__username', 'match_request__receiver__user__username')

@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ('sender', 'conversation', 'created_at', 'is_read')
    list_filter = ('is_read', 'created_at')
    search_fields = ('sender__user__username', 'content')
