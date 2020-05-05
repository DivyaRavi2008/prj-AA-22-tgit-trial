# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework.status import HTTP_201_CREATED
from rest_framework.status import HTTP_404_NOT_FOUND
from rest_framework.status import HTTP_400_BAD_REQUEST
from rest_framework.views import APIView

from django.http import JsonResponse
from .models import Team
from .serializers import TeamSerializer

def index(*arg , **kwargs):
    return HttpResponse("Welcome to our Team")

class TeamView(APIView):
    
    def post(self,request):
        serializer = TeamSerializer(data = request.data)
        if serializer.is_valid():
            org = Team.objects.create(name = serializer.data['name'],dept= serializer.data['dept'],dob = serializer.data['dob'],moto = serializer.data['moto'])
            org.save()
            return Response(status=HTTP_201_CREATED,data={'message': "Joined Team"})
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)

    def get(self, request):
        orgs = Team.objects.all()
        app = Team.objects.get(id = '1')
        print(app)
        print("run")
        apps = Team.objects.filter(id='1')
        print(apps)
        print("quick")
        dept = request.data
        name = request.data
        unit = Team.objects.filter(dept=dept).last()
        print(unit)
        units = Team.objects.filter(name=name).first()
        print(units)
        serializer = TeamSerializer(orgs, many=True)
        return JsonResponse(serializer.data, safe=False)


