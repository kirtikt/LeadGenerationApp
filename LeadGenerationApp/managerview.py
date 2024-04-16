
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser
from rest_framework import status
from django.views.decorators.clickjacking import xframe_options_exempt
from LeadGenerationApp.models import Manager
from LeadGenerationApp.models import States
from LeadGenerationApp.models import Cities
from django.db import connection
from .import tuple_to_dict
from LeadGenerationApp.serializers import ManagerSerializer
from LeadGenerationApp.serializers import StatesSerializer
from LeadGenerationApp.serializers import CitiesSerializer
from django.http.response import JsonResponse


@xframe_options_exempt
@api_view(['GET','POST','DELETE'])
def ManagerInterface(request):
    return render(request,"Manager.html",{})

@xframe_options_exempt
def DisplayAllManager(request):
    return render(request,"DisplayAllManager.html",{})
@xframe_options_exempt
@api_view(['GET','POST','DELETE'])
def ManagerSubmit(request):
   if request.method == 'POST':
      print("employeeeeee",request.data)
      manager_serializer = ManagerSerializer(data=request.data)
      if manager_serializer.is_valid():
        manager_serializer.save()
        return render(request,"Manager.html",{"message":"Record Submitted Successfully"})
     
      
      return render(request,"Manager.html",{"message":"Fail to Submit Record"})
    
'''
@api_view(['GET','POST','DELETE'])
def Manager_List(request):
  if request.method=='GET':
    manager_list=Manager.objects.all()
    manager_serializer=ManagerSerializer(manager_list,many=True)
    #print("Employee",employee_serializer.data)
    return JsonResponse(manager_serializer.data,safe=False)
  return JsonResponse({},safe=False)
'''
@xframe_options_exempt
@api_view(['GET', 'POST', 'DELETE'])
def Manager_List(request):
   if request.method=='GET':
    cursor=connection.cursor() 
    q="select E.*,(select S.statename from leadgenerationapp_states S where S.stateid=E.state) as statename,(select C.cityname from leadgenerationapp_cities C where C.cityid=E.city) as cityname from leadgenerationapp_manager E"
    cursor.execute(q)
    data=tuple_to_dict.ParseToDictAll(cursor)
    return JsonResponse(data,safe=False)
   return JsonResponse({},safe=False)