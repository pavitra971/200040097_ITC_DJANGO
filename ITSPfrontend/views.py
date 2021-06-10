
from django.shortcuts import render
from django.http import  HttpResponse,JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Info
from .serializers import InfoSerializer
from rest_framework import viewsets


# Create your views here.

def index(request):
    return render(request,'index.html')


def SumSquad(request):
    return render(request,'SumSquad.html')

def ITS21001(request):
    return render(request,'ITS21001.html')

def ITS21002(request):
    return render(request,'ITS21002.html')

def ITS21003(request):
    return render(request,'ITS21003.html')

def ITS21004(request):
    return render(request,'ITS21004.html')

def ITS21005(request):
    return render(request,'ITS21005.html')

def ITS21006(request):
    return render(request,'ITS21006.html')

def ITS21007(request):
    return render(request,'ITS21007.html')

def ITS21008(request):
    return render(request,'ITS21008.html')

def ITS21009(request):
    return render(request,'ITS21009.html')

def ITS21010(request):
    return render(request,'ITS21010.html')





def ITS31001(request):
    return render(request,'ITS31001.html')

def ITS31002(request):
    return render(request,'ITS31002.html')


def info(request):
    if request.method == "POST":


        teamname=request.POST.get('teamname')
        teamid=request.POST.get('teamid')
        teamleadername=request.POST.get('teamleadername')
        teamleaderphoneno=request.POST.get('teamleaderphoneno')
        teamleaderemail=request.POST.get('teamleaderemail')
        member1name=request.POST.get('member1name'),
        member1phoneno=request.POST.get('member1phoneno')
        member1email=request.POST.get('member1email')
        member2name=request.POST.get('member2name')
        member2phoneno=request.POST.get('member2phoneno')
        member2email=request.POST.get('member2email')
        member3name=request.POST.get('member3name')
        member3phoneno=request.POST.get('member3phoneno')
        member3email=request.POST.get('member3email')

        
        info=Info(teamname=teamname, teamid=teamid, teamleadername=teamleadername, teamleaderphoneno=teamleaderphoneno, teamleaderemail=teamleaderemail, member1name=member1name, member1phoneno=member1phoneno, member1email=member1email, member2name=member2name, member2phoneno=member2phoneno, member2email=member2email, member3name=member3name, member3phoneno=member3phoneno, member3email=member3email)
        info.save()
 
             

    return render(request,'info.html')   


@csrf_exempt
def Info_list(request):
   
    if request.method == 'GET':
        Info = info.objects.all()
        serializer = InfoSerializer(Info, many=True)
        return JsonResponse(Info.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = InfoSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


@csrf_exempt
def Info_detail(request, pk):
   
    try:
        Info = info.objects.get(pk=pk)
    except info.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = InfoSerializer(Info)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = InfoSerializer(Info, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        Info.delete()
        return HttpResponse(status=204)















