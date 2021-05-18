from django.db.models import Q
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt

from rest_framework.parsers import JSONParser
from .models import BranchInfo
from .serializers import BranchSerializer

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status


# Create your views here.


@api_view(['GET'])
def autocomplete_branch(request):
    if request.method == 'GET':
        q = request.query_params['q']
        limit = int(request.query_params['limit'])
        offset = int(request.query_params['offset'])
        branches = BranchInfo.objects.all().filter(branch__contains=q).order_by('ifsc')[offset:offset + limit]
        serializer = BranchSerializer(branches, many=True)
        return Response(serializer.data)

@api_view(['GET'])
def allpossible_branch(request):
    if request.method == 'GET':
        q = request.query_params['q']
        limit = int(request.query_params['limit'])
        offset = int(request.query_params['offset'])
        branches = BranchInfo.objects.all().filter(
            Q(ifsc__contains=q) | Q(bank_id__contains=q) | Q(branch__contains=q) | Q(address__contains=q) |
            Q(city__contains=q) | Q(district__contains=q) | Q(state__contains=q) | Q(bank_name__contains=q)
        ).order_by('ifsc')[offset:offset + limit]
        serializer = BranchSerializer(branches, many=True)
        return Response(serializer.data)
