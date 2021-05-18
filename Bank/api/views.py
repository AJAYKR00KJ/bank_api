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
        branches = BranchInfo.objects.all().filter(branch__icontains=q).order_by('ifsc')[offset:offset + limit]
        serializer = BranchSerializer(branches, many=True)
        return Response(serializer.data)

@api_view(['GET'])
def allpossible_branch(request):
    if request.method == 'GET':
        q = request.query_params['q']
        limit = int(request.query_params['limit'])
        offset = int(request.query_params['offset'])
        branches = BranchInfo.objects.all().filter(
            Q(ifsc__icontains=q) | Q(bank_id__icontains=q) | Q(branch__icontains=q) | Q(address__icontains=q) |
            Q(city__icontains=q) | Q(district__icontains=q) | Q(state__icontains=q) | Q(bank_name__icontains=q)
        ).order_by('ifsc')[offset:offset + limit]
        serializer = BranchSerializer(branches, many=True)
        return Response(serializer.data)
