from django.shortcuts import render
from rest_framework import viewsets, permissions, mixins, generics, filters
# Create your views here.
from .serializers import *
from .models import *
from rest_framework.status import (
    HTTP_400_BAD_REQUEST,
    HTTP_404_NOT_FOUND,
    HTTP_200_OK
)
from rest_framework.response import Response
from rest_framework.views import APIView
import json


class IFSCBranchDetailView(APIView):
    queryset = branches.objects.all()
    serializer_class = ifsc_branchSerializer

    def post(self, request, *args, **kwargs):
        ifsc = request.POST.get('ifsc')
        try:
            branch = branches.objects.get(ifsc=ifsc)
            branch_serializer = branchSerializer(branch)
            return Response(branch_serializer.data, status=HTTP_200_OK)
        except:
            return Response({'status':'fail', 'detail':'branch may not exist'}, status=HTTP_200_OK)


class BankCityBranchesListView(APIView):
    queryset = branches.objects.all()
    serializer_class = bank_city_branchSerializer

    def post(self, request, *args, **kwargs):
        bank_name = request.POST.get('bank')
        city = request.POST.get('city_name')
        try:
            bank_obj = banks.objects.get(id=int(bank_name))
            branchez = branches.objects.filter(bank=bank_obj, city=city)
            branchez_dict = {}
            for i in range(len(branchez)):
                branch_serializer = branchSerializer(branchez[i])
                branchez_dict[i+1] = branch_serializer.data
            return Response(branchez_dict, status=HTTP_200_OK)
        except:
            return Response({'status':'fail', 'detail':'branch may not exist'}, status=HTTP_200_OK)