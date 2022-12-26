from django.urls import path

from games.views import (ListCategory, ListPlayerInfo,
                         CreatePlayerView, SuccessResponseView, FailResponseView)

urlpatterns = [
    # listing category info
    path('', ListCategory.as_view(), name='category_list'),

    # lisiting player info
    path('player/', ListPlayerInfo.as_view(), name='player_list'),

    # creating player instances
    path('player/<int:id>/', CreatePlayerView.as_view(),
         name='create_player_object'),

    path('player/reg/success/', SuccessResponseView.as_view(),
         name='success_response'),

    path('player/reg/fail/', FailResponseView.as_view(), name='fail_response'),


]
