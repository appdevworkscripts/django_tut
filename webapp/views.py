# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import JsonResponse
from webapp.models import employees
from . serializers import EmployeeSerializer
from django.db import connection
# Create your views here.


class employeeList(APIView):
    def get(self,request):
        es=employees.objects.all()
        serializer=EmployeeSerializer(es,many=True)
        return Response(serializer.data)
    def post(self,request):
        e=employees(name=request.data['name'],emp_id=request.data['emp_id'])
        e.save()
        s=EmployeeSerializer(e,many=False)
        resp={'success':True,'employee':s.data}
        return JsonResponse(resp)
    def put(self,request):
        with connection.cursor() as cursor:
            cursor.execute("SELECT zip FROM zip_vs_real LIMIT 2");
            results = cursor.fetchall()
        resp={'success':True,'result':results}
        return JsonResponse(resp)
