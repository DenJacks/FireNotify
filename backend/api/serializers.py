from rest_framework import serializers
from users.models import User
from api.models import Activity


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            "id",
            "username",
            "email",
            "first_name",
            "last_name",
            "role",
            "is_staff",
            "is_active",
        ]


class ActivitySerializer(serializers.ModelSerializer):

    class Meta:
        model = Activity
        fields = [
            "id",
            "title",
            "activity_type",
            "priority",
            "description",
            "activity_date",
            "activity_time",
            "location",
            "assigned_personnel",
            "status",
            "created_by",
            "created_at",
            "updated_at",
        ]