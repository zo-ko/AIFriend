from django.urls import path, re_path

from web.views.create import get_single
from web.views.create.create import CreateCharacterView
from web.views.create.get_list import GetListCharacterView
from web.views.create.get_single import GetSingleCharacterView
from web.views.create.remove import RemoveCharacterView
from web.views.create.update import UpdateCharacterView
from web.views.index import index
from web.views.user.account.get_user_info import GetUserInfo
from web.views.user.account.login import LoginView
from web.views.user.account.logout import LogoutView
from web.views.user.account.refresh_token import RefreshTokenView
from web.views.user.account.register import RegisterView
from web.views.user.profile.update import UpdateProfileView

urlpatterns = [
    path('api/user/account/login/',LoginView.as_view()),
    path('api/user/account/logout/',LogoutView.as_view()),
    path('api/user/account/register/',RegisterView.as_view()),
    path('api/user/account/refresh_token/',RefreshTokenView.as_view()),
    path('api/user/account/get_user_info/',GetUserInfo.as_view()),
    path('api/user/profile/update/',UpdateProfileView.as_view()),
    path('api/create/character/create/',CreateCharacterView.as_view()),
    path('api/create/character/update/',UpdateCharacterView.as_view()),
    path('api/create/character/remove/',RemoveCharacterView.as_view()),
    path('api/create/character/get_single/',GetSingleCharacterView.as_view()),
    path('api/create/character/get_list/',GetListCharacterView.as_view()),
    path('',index),
    re_path(r'^(?!media/|static/|assets/).*$', index)
]
