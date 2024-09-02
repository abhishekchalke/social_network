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



class FriendRequesSerializer(serializers.ModelSerializer):
    name = serializers.CharField(source='to_user.name', read_only=True)

    class Meta:
        model = models.FriendRequest
        fields = ['name']



class SearchUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.CustomUser
        fields = ['name']



























'''
super@gmail.com     : qwaszx     ()
girish@gmail.com    : qwaszxG    (8aeafcaaa688dc94a801557a5ab501735e0f2f70)
vikram@gmail.com    : qwaszxV    ()
vikas@gmail.com     : qwaszxV    ()
abhi@gmail.com      : qwaszxA    ()
ravi@gmail.com      : qwaszxR    ()
manisha@gmail.com   : qwaszxM    ()
pratiksha@gmail.com : qwaszxP    ()
prajwal@gmail.com   : qwaszxP    ()
akshay@gmail.com    : qwaszxA    ()
ashrit@gmail.com    : qwaszxA    (64d3e31ecc77ab0025418ed1df69134ec5372f69)



user - - - friend (user)

API's
API to send/accept/reject friend request


'''




