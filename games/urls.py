from django.urls import path

# register
from games.views import ListCategory
from games.views import CreatePlayerView
from games.views import SuccessResponseView
from games.views import FailResponseView

# show
from games.views import ListRegisteredCategory
from games.views import ShowCategoryPlayers
from games.views import ShowPlayerDetails

urlpatterns = [
    # listing category info
    path('', ListCategory.as_view(), name='category_list'),

    # creating player instances
    path('category/<int:id>/', CreatePlayerView.as_view(),
         name='create_player_object'),

    path('player/reg/success/', SuccessResponseView.as_view(),
         name='success_response'),

    path('player/reg/fail/', FailResponseView.as_view(), name='fail_response'),


     # showing Registered Details
    path('registered/category/', ListRegisteredCategory.as_view(), name='registered_category'),

    path('registered/players/<int:id>/', ShowCategoryPlayers.as_view(), name='show_category_players'),

#     lisiting player detail info
    path('registered/player/detail/<int:id>/', ShowPlayerDetails.as_view(), name='show_player_details'),


]
