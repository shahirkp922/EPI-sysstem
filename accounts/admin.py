from django.contrib import admin
from .models import Post,Profile

# Register your models here.
admin.site.register(Post)
admin.site.register(Profile)




from django.contrib import admin
from .models import Profile, Post
from django.contrib.auth.models import User

# Register your models here.

class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'referral_code', 'referred_by', 'kyc_document_type', 'pan_card', 'bank_passbook')
    search_fields = ('user__username', 'referral_code')
    list_filter = ('kyc_document_type',)

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'img', 'desc')
    search_fields = ('title',)
    list_filter = ('title',)

# Register models in the Django admin interface
# Register the User model for the admin interface
