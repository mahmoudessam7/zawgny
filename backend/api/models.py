from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

class Profile(models.Model):
    """Profile model for matrimonial users."""
    
    GENDER_CHOICES = (
        ('M', _('Male')),
        ('F', _('Female')),
    )
    
    MARITAL_STATUS_CHOICES = (
        ('S', _('Single')),
        ('D', _('Divorced')),
        ('W', _('Widowed')),
    )
    
    EDUCATION_CHOICES = (
        ('HS', _('High School')),
        ('BA', _('Bachelor\'s Degree')),
        ('MA', _('Master\'s Degree')),
        ('PHD', _('PhD')),
        ('OTH', _('Other')),
    )
    
    RELIGIOSITY_CHOICES = (
        ('VR', _('Very Religious')),
        ('R', _('Religious')),
        ('MR', _('Moderately Religious')),
        ('NVR', _('Not Very Religious')),
    )
    
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    date_of_birth = models.DateField()
    phone_number = models.CharField(max_length=20)
    city = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    marital_status = models.CharField(max_length=1, choices=MARITAL_STATUS_CHOICES)
    children = models.IntegerField(default=0)
    education = models.CharField(max_length=3, choices=EDUCATION_CHOICES)
    occupation = models.CharField(max_length=100)
    height = models.FloatField(help_text=_("Height in cm"))
    religiosity = models.CharField(max_length=3, choices=RELIGIOSITY_CHOICES)
    bio = models.TextField(max_length=500)
    photo = models.ImageField(upload_to='profile_photos/', blank=True, null=True)
    is_verified = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"{self.user.username} Profile"

class MatchPreference(models.Model):
    """Model for user's preferences for matching."""
    
    AGE_CHOICES = (
        ('18-25', _('18-25')),
        ('26-35', _('26-35')),
        ('36-45', _('36-45')),
        ('46+', _('46+')),
    )
    
    HEIGHT_CHOICES = (
        ('150-160', _('150-160 cm')),
        ('161-170', _('161-170 cm')),
        ('171-180', _('171-180 cm')),
        ('181+', _('181+ cm')),
    )
    
    profile = models.OneToOneField(Profile, on_delete=models.CASCADE, related_name='preferences')
    age_range = models.CharField(max_length=10, choices=AGE_CHOICES)
    height_range = models.CharField(max_length=10, choices=HEIGHT_CHOICES)
    education_preference = models.CharField(max_length=3, choices=Profile.EDUCATION_CHOICES, blank=True, null=True)
    marital_status_preference = models.CharField(max_length=1, choices=Profile.MARITAL_STATUS_CHOICES, blank=True, null=True)
    has_children_preference = models.BooleanField(null=True, blank=True)
    country_preference = models.CharField(max_length=100, blank=True, null=True)
    religiosity_preference = models.CharField(max_length=3, choices=Profile.RELIGIOSITY_CHOICES, blank=True, null=True)
    additional_preferences = models.TextField(blank=True, null=True)
    
    def __str__(self):
        return f"{self.profile.user.username}'s Preferences"

class MatchRequest(models.Model):
    """Model for tracking match requests between users."""
    
    STATUS_CHOICES = (
        ('P', _('Pending')),
        ('A', _('Accepted')),
        ('R', _('Rejected')),
        ('C', _('Canceled')),
    )
    
    sender = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='sent_requests')
    receiver = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='received_requests')
    status = models.CharField(max_length=1, choices=STATUS_CHOICES, default='P')
    message = models.TextField(blank=True, null=True)
    admin_approved = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        unique_together = ('sender', 'receiver')
    
    def __str__(self):
        return f"Request from {self.sender.user.username} to {self.receiver.user.username}"

class Conversation(models.Model):
    """Model for conversations between matched users."""
    
    match_request = models.OneToOneField(MatchRequest, on_delete=models.CASCADE, related_name='conversation')
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"Conversation between {self.match_request.sender.user.username} and {self.match_request.receiver.user.username}"

class Message(models.Model):
    """Model for messages within conversations."""
    
    conversation = models.ForeignKey(Conversation, on_delete=models.CASCADE, related_name='messages')
    sender = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='sent_messages')
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)
    
    def __str__(self):
        return f"Message from {self.sender.user.username} at {self.created_at}"
