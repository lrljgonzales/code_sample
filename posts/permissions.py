from django.contrib.auth.models import Group, User
from rest_framework.permissions import BasePermission

#admin_group = Group.objects.create(name="Admin")
#user = User.objects.get(username="admin_user")
#user.groups.add(admin_group)

class IsPostAuthor(BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.author == request.user
