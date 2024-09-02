from django.contrib import admin

from users import models




admin.site.register(models.CustomUser)

admin.site.register(models.FriendRequest)

