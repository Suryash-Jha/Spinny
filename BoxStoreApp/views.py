from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
# from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout, get_user_model
User = get_user_model()
from .models import BoxModel




def hello(req):
    return HttpResponse('Hello, world!')

def is_authenticated(req):
    if req.user.is_authenticated:
        return True
    else:
        return False

def is_staff(req):
    if req.user.is_staff:
        return True
    else:
        return False



@csrf_exempt
def register(req):
    if req.method == 'POST':
        username = req.POST['username']
        password = req.POST['password']
        usertype = req.POST['type']
        user = User.objects.create_user(username, usertype, password)
        user.save()
        return HttpResponse('User created')
    else:
        return HttpResponse('Error creating user')
@csrf_exempt
def loginx(req):
    if req.method == 'POST':
        username = req.POST['username']
        password = req.POST['password']
        user = authenticate(req, username=username, password=password)
        if user is not None:
            login(req, user)
            return HttpResponse('User logged in'+ str(user.username)+': ' +str(user.typex)+ ':'+ str(user.is_staff))
        else:
            return HttpResponse('Error logging in')
    else:
        return HttpResponse('Error logging in')

@csrf_exempt
def logoutx(req):
    logout(req)
    return HttpResponse('User logged out')

@csrf_exempt
def isLogged(req):
    if req.user.is_authenticated:
        return HttpResponse('User is logged in')
    else:
        return HttpResponse('User is not logged in')

@csrf_exempt
def addBox(req):
    if req.method == 'POST':
        boxName = req.POST['name']
        boxLength = int(req.POST['length'])
        boxWidth = int(req.POST['width'])
        boxHeight = int(req.POST['height'])
        boxCreated_by = req.POST['created_by']
        boxUpdated_by = req.POST['updated_by']
        boxArea= 2*(boxLength*boxWidth +boxLength*boxHeight +boxWidth*boxHeight )
        boxVolume= boxLength*boxWidth*boxHeight

        box = BoxModel.objects.create(name=boxName, length=boxLength, width=boxWidth, height=boxHeight, area=boxArea, volume= boxVolume, created_by= boxCreated_by, updated_by=boxUpdated_by)
        
        box.save()
        print(BoxModel.objects.all().values())
        return HttpResponse('Box created')
    else:
        return HttpResponse('Error creating box')


# Create your views here.
@csrf_exempt
def updateBox(req, id):
    if req.method == 'POST':
        boxName = req.POST['name']
        boxLength = int(req.POST['length'])
        boxWidth = int(req.POST['width'])
        boxHeight = int(req.POST['height'])
        boxUpdated_by = req.POST['updated_by']
        boxArea= 2*(boxLength*boxWidth +boxLength*boxHeight +boxWidth*boxHeight )
        boxVolume= boxLength*boxWidth*boxHeight

        box = BoxModel.objects.get(id=id)
        box.name= boxName
        box.length= boxLength
        box.width= boxWidth
        box.height= boxHeight
        box.area= boxArea
        box.volume= boxVolume
        box.updated_by= boxUpdated_by
        box.save()
        return HttpResponse('Box updated')
    else:
        return HttpResponse('Error updating box')

@csrf_exempt
def deleteBox(req, id):
    # if req.method == 'DELETE' and is_authenticated(req) and is_staff(req):
    if req.method == 'DELETE':

        box = BoxModel.objects.get(id=id)
        box.delete()
        return HttpResponse('Box deleted')
    else:
        return HttpResponse('Error deleting box')
