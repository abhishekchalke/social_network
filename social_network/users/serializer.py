from django.contrib.auth.models import User

from rest_framework import serializers

from users import models




class AuthUserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    name = serializers.CharField(required=True)

    class Meta:
        model = models.CustomUser
        fields = ['email', 'password', 'name']

    def create(self, validated_data):
        user = models.CustomUser(email=validated_data['email'].lower(), name=validated_data['name'])
        user.set_password(validated_data['password'])
        user.save()

        return user




class FromFriendsSerializer(serializers.ModelSerializer):
    name = serializers.CharField(source='to_user.name', read_only=True)

    class Meta:
        model = models.FriendRequest
        fields = ['name']




class ToFriendsSerializer(serializers.ModelSerializer):
    name = serializers.CharField(source='from_user.name', read_only=True)

    class Meta:
        model = models.FriendRequest
        fields = ['name']




class FriendRequesSerializer(serializers.ModelSerializer):
    name = serializers.CharField(source='from_user.name', read_only=True)

    class Meta:
        model = models.FriendRequest
        fields = ['name']



class SearchUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.CustomUser
        fields = ['name']













