from django.contrib import admin
from .models import Post, User_New, Comment_on_Post, Comment, Block_User


# Register your models here.

class CommentAdmin(admin.TabularInline):
    model = Comment_on_Post
    extra = 0
    list_display = ("comment_description", "date_comment_created")

    def has_add_permission(self, request, obj=None):
            return True

    def has_view_permission(self, request, obj=None):
        return True

    def has_change_permission(self, request, obj=None):
        if (obj and (obj.user == request.user)) or request.user.is_superuser:
            return True
        return False

    def has_delete_permission(self, request, obj = None):
        if (obj and (obj.user == request.user)) or request.user.is_superuser:
            return True
        return False

class PostAdmin(admin.ModelAdmin):
    def has_view_permission(self, request, obj=None):
        return True

    def has_add_permission(self, request):
        return True

    def has_change_permission(self, request, obj=None):
        if obj and (obj.user.user == request.user) or request.user.is_superuser:
            return True
        return False

    def has_delete_permission(self, request, obj=None):
        if obj and (obj.user.user == request.user) or request.user.is_superuser:
            return True
        return False

    list_display = ("title", "description")
    search_fields = ("title", "description")
    inlines = [CommentAdmin]


admin.site.register(Post, PostAdmin)


class UserAdmin(admin.ModelAdmin):

    def has_change_permission(self, request, obj=None):
        if obj and (obj.user == request.user):
            return True
        return False

    def has_delete_permission(self, request, obj=None):
        if obj and (obj.user == request.user):
            return True
        return False
    list_display = ("name",)

admin.site.register(User_New, UserAdmin)
class CommentInAdmin(admin.ModelAdmin):
    def has_add_permission(self, request, obj=None):
        return True

    def has_view_permission(self, request, obj=None):
        return True

    def has_change_permission(self, request, obj=None):
        if (obj and (obj.comment_user.user == request.user)) or request.user.is_superuser:
            return True
        return False

    def has_delete_permission(self, request, obj=None):
        if (obj and (obj.comment_user.user == request.user)) or request.user.is_superuser:
            return True
        return False

admin.site.register(Comment,CommentInAdmin)

class BlockAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        return True
    def has_view_permission(self, request, obj=None):
        return True
admin.site.register(Block_User,BlockAdmin)


