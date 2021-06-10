
from django.shortcuts import render
from ITSPfrontend.models import Info

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






























