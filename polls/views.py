from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from django.shortcuts import get_object_or_404

from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Poll, Choice, Vote
from .serializers import PollSerializer, ChoiceSerializer, VoteSerializer


class PollList(generics.ListCreateAPIView):
    queryset = Poll.objects.all()
    serializer_class = PollSerializer


class PollDetail(generics.RetrieveDestroyAPIView):
    queryset = Poll.objects.all()
    serializer_class = PollSerializer


class ChoiceList(generics.ListCreateAPIView):
    queryset = Choice.objects.all()
    serializer_class = ChoiceSerializer


class CreateVote(generics.CreateAPIView):
    queryset = VoteSerializer


# class PollList(APIView):
#     def get(self, request):
#         polls = Poll.objects.all()[:10]
#         data = PollSerializer(polls, many=True).data
#         return Response(data)
#
#
# class PollDetail(APIView):
#     def get(self, request, pk):
#         poll = get_object_or_404(Poll, pk=pk)
#         data = PollSerializer(poll).data
#         return Response(data)

# def polls_list(request):
#     MAX_OBJECTS = 20
#     polls = Poll.objects.all()[:MAX_OBJECTS]
#     data = {
#         "results": list(polls.values("question", "created_by__username", "pub_date"))
#     }
#     return JsonResponse(data)
#
#
# def polls_detail(request, pk):
#     poll = get_object_or_404(Poll, pk=pk)
#     data = {
#         "results": {
#             "question": poll.question,
#             "created_by": poll.created_by.username,
#             "pub_date": poll.pub_date
#         }
#     }
#     return JsonResponse(data)
