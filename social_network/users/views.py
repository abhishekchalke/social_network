from django.shortcuts import render

from rest_framework import generics, views, status as response_status
from rest_framework.response import Response

from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login

from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.models import Token

from users import serializer, models, throttling




class UserSignUpApiView(generics.CreateAPIView):
    queryset = models.CustomUser.objects.all()
    serializer_class = serializer.AuthUserSerializer



class LoginApiView(views.APIView):
    def post(self, request):
        required_fields = ['email', 'password']
        missing_fields = [field for field in required_fields if field not in request.data.keys()]

        if missing_fields:
            return Response({'error': 'Missing required fields','missing_fields': missing_fields}, status=response_status.HTTP_400_BAD_REQUEST)

        email = request.data['email'].lower()
        password = request.data['password']

        if models.CustomUser.objects.filter(email=email).exists():
            user = models.CustomUser.objects.get(email=email)
        else:
            return Response({"error": "Invalid credentials1"}, status=response_status.HTTP_400_BAD_REQUEST)

        if user.check_password(password):
            token, created = Token.objects.get_or_create(user=user)
            return Response({"message": "Login successful","token": token.key}, status=response_status.HTTP_200_OK)

        return Response({"error": "Invalid credentials"}, status=response_status.HTTP_400_BAD_REQUEST)



class SendFriendRequestApiView(views.APIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = [IsAuthenticated]
    throttle_classes = [throttling.BurstRateThrottle]

    def post(self, request, *args, **kwargs):
        required_fields = ['name']
        missing_fields = [field for field in required_fields if field not in request.data.keys()]

        if missing_fields:
            return Response({'error': 'Missing required fields','missing_fields': missing_fields}, status=response_status.HTTP_400_BAD_REQUEST)

        from_user = request.user
        to_user = request.data['name']

        if models.CustomUser.objects.filter(name=to_user).exists():
            to_user = models.CustomUser.objects.get(name=to_user)
        else:
            return Response({"error": "User not found."}, status=response_status.HTTP_404_NOT_FOUND)

        if models.FriendRequest.objects.filter(from_user=from_user, to_user=to_user).exists():
            friend_req = models.FriendRequest.objects.filter(from_user=from_user, to_user=to_user)[0]

            if friend_req.status == 'pending':
                return Response({"message": "Friend request has already been sent"}, status=response_status.HTTP_200_OK)
            else:
                return Response({"message": "Friend request has already been %s" % friend_req.status}, status=response_status.HTTP_200_OK)
        else:
            models.FriendRequest.objects.update_or_create(from_user=from_user, to_user=to_user, status='pending')
            return Response({"message": "Friend request sent"}, status=response_status.HTTP_404_NOT_FOUND)



class AcceptFriendRequestApiView(views.APIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):        
        required_fields = ['name']
        missing_fields = [field for field in required_fields if field not in request.data.keys()]

        if missing_fields:
            return Response({'error': 'Missing required fields','missing_fields': missing_fields}, status=response_status.HTTP_400_BAD_REQUEST)

        from_user = request.user
        to_user = request.data['name']

        if models.CustomUser.objects.filter(name=to_user).exists():
            to_user = models.CustomUser.objects.get(name=to_user)
        else:
            return Response({"error": "User not found."}, status=response_status.HTTP_404_NOT_FOUND)

        if models.FriendRequest.objects.filter(from_user=from_user, to_user=to_user).exists():
            friend_req = models.FriendRequest.objects.filter(from_user=from_user, to_user=to_user)[0]

            if friend_req.status == 'pending':
                friend_req.status = 'accepted'
                friend_req.save()
                return Response({"message": "Friend request accepted"}, status=response_status.HTTP_200_OK)
            else:
                return Response({"message": "Friend request has already been %s" % friend_req.status}, status=response_status.HTTP_200_OK)
        else:
            return Response({"message": "There is no friend request"}, status=response_status.HTTP_404_NOT_FOUND)



class RejectFriendRequestApiView(views.APIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        required_fields = ['name']
        missing_fields = [field for field in required_fields if field not in request.data.keys()]

        if missing_fields:
            return Response({'error': 'Missing required fields','missing_fields': missing_fields}, status=response_status.HTTP_400_BAD_REQUEST)

        from_user = request.user
        to_user = request.data['name']

        if models.CustomUser.objects.filter(name=to_user).exists():
            to_user = models.CustomUser.objects.get(name=to_user)
        else:
            return Response({"error": "User not found."}, status=response_status.HTTP_404_NOT_FOUND)

        if models.FriendRequest.objects.filter(from_user=from_user, to_user=to_user).exists():
            friend_req = models.FriendRequest.objects.filter(from_user=from_user, to_user=to_user)[0]

            if friend_req.status == 'pending':
                friend_req.status = 'rejected'
                friend_re.save()
                return Response({"message": "Friend request rejected"}, status=response_status.HTTP_200_OK)
            else:
                return Response({"message": "Friend request has already been %s" % friend_req.status}, status=response_status.HTTP_200_OK)
        else:
            return Response({"message": "There is no friend request"}, status=response_status.HTTP_404_NOT_FOUND)



class ListFriendsApiView(views.APIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        friends = models.FriendRequest.objects.filter(from_user=request.user, status='accepted')

        if friends:
            friends_srz = serializer.FriendRequesSerializer(friends, many=True)
            return Response(friends_srz.data, status=response_status.HTTP_200_OK)
        else:
            return Response({"message": "There are no friends"}, status=response_status.HTTP_404_NOT_FOUND)



class ListFriendRequestsApiView(views.APIView):
    authentication_classes = [TokenAuthentication,]
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        friend_reqs = models.FriendRequest.objects.filter(from_user=request.user, status='pending')

        if friend_reqs:
            friend_reqs_srz = serializer.FriendRequesSerializer(friend_reqs, many=True)
            return Response(friend_reqs_srz.data, status=response_status.HTTP_200_OK)
        else:
            return Response({"message": "There are no friend requests"}, status=response_status.HTTP_404_NOT_FOUND)



class SearchUsersApiView(views.APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]    

    def post(self, request, *args, **kwargs):
        required_fields = ['search', 'search_by']
        missing_fields = [field for field in required_fields if field not in request.data.keys()]

        if missing_fields:
            return Response({'error': 'Missing required fields','missing_fields': missing_fields}, status=response_status.HTTP_400_BAD_REQUEST)

        search = request.data['search']
        search_by = request.data['search_by']

        if search_by == 'email':
            users = models.CustomUser.objects.filter(email=search)
            if not users:
                users = models.CustomUser.objects.filter(email__contains=search)
        elif search_by == 'name':
            users = models.CustomUser.objects.filter(name=search)
            if not users:
                users = models.CustomUser.objects.filter(name__contains=search)
        else:
            return Response({"message":"Invalid search filter"}, status=response_status.HTTP_404_NOT_FOUND)

        users_srz = serializer.SearchUserSerializer(users, many=True)
        return Response(users_srz.data, status=response_status.HTTP_200_OK)













