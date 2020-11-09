from django.urls import path
from .views import *

urlpatterns = [
    path("polls/", PollList.as_view(), name="polls_list"),
    path("polls/<int:pk>/", PollDetail.as_view(), name="polls_detail"),
    # path("choices/", ChoiceList.as_view(), name="choice_list"),
    # path("vote/", CreateVote.as_view(), name="create_vote"),
    path("polls/<int:pk>/choices/", ChoiceList.as_view(), name="choice_list"),
    path("polls/<int:pk>/choices/<int:choice_pk>/vote/", CreateVote.as_view(), name="create_vote"),
]
