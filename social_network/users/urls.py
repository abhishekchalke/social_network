from django.urls import path
from users import views

urlpatterns = [
    path('api/signup/', views.UserSignUpApiView.as_view(), name = 'api_signup'),
    path('api/login/', views.LoginApiView.as_view(), name = 'api_login'),

    path('api/friend_request/send/', views.SendFriendRequestApiView.as_view(), name = 'api_friend_request_send'),
    path('api/friend_request/accept/', views.AcceptFriendRequestApiView.as_view(), name = 'api_friend_request_accept'),
    path('api/friend_request/reject/', views.RejectFriendRequestApiView.as_view(), name = 'api_friend_request_reject'),

    path('api/list/friends/', views.ListFriendsApiView.as_view(), name = 'api_list_friends'),
    path('api/list/friend_requests/', views.ListFriendRequestsApiView.as_view(), name = 'api_list_friend_requests'),

    path('api/search/users/', views.SearchUsersApiView.as_view(), name = 'api_search_users'),

]






