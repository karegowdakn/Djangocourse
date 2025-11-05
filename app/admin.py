from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import UserProfile, Article


class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'word_count', 'status', 'created_at', 'updated_at')
    list_filter = ('status', 'created_at', 'updated_at')
    search_fields = ('title', 'content',)
    date_hierarchy = 'created_at'
    ordering = ('created_at',)
    readonly_fields = ('word_count', 'created_at', 'updated_at')


class CustomUserAdmin(UserAdmin):
    # Fields displayed during user_creation
    add_fieldsets = (
        (None,
            {
                "classes": ("wide",),
                "fields": ("email", "password1", "password2"),
            },
        ),
    )
    # Fields admin can see inside user_profile
    fieldsets = (
        (None, {"fields": ("email", "password")}),
        (("Personal info"), {"fields": ("first_name", "last_name", "username")}),
        (("Permissions"),
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                ),
            },
        ),
        (("Important dates"), {"fields": ("last_login", "date_joined")}),
    )
    list_display = ('username', 'email', 'is_staff', 'is_active')
    list_filter = ('is_staff', 'is_active')
    search_fields = ('email', 'username')


admin.site.register(UserProfile, CustomUserAdmin)
admin.site.register(Article, ArticleAdmin)
