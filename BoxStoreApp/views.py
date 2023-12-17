from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
# from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout, get_user_model
User = get_user_model()
from .models import BoxModel
from rest_framework.authtoken.models import Token
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.decorators import authentication_classes, permission_classes
from django.db.models import Sum, Q
from django.conf import settings
from datetime import datetime
from .validation import validate_box
# settings.configure()


def hello(req):
    return HttpResponse('Hello, world!')

def is_authenticated(req):
    if req.user.is_authenticated:
        return True
    else:
        return False

def get_user(req):
    auth_header = req.headers.get('Authorization')
    auth_token = auth_header[6:]
    user = Token.objects.get(key=auth_token).user
    return user

def is_staff(user):
    if user.is_staff:
        return True
    else:
        return False

@csrf_exempt
def register(req):
    if req.method == 'POST':
        username = req.POST['username']
        password = req.POST['password']
        usertype = req.POST['type']
        if usertype == 'staff':
            usertype = True
        else:
            usertype = False
        user = User.objects.create_user(username= username, is_staff= usertype, password=password)
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
            token, created= Token.objects.get_or_create(user=user)
            print(token.key)
            return JsonResponse({'status': 200, 'token': token.key, 'user': user.username, 'isStaff': user.is_staff})
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


def home(req):
    return render(req, 'index.html')

@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
@csrf_exempt
def addBox(req):
    user=  get_user(req)
    if req.method == 'POST' and is_staff(user):
        boxName = req.POST['name']
        boxLength = int(req.POST['length'])
        boxWidth = int(req.POST['width'])
        boxHeight = int(req.POST['height'])
        boxCreated_by = user.username
        boxUpdated_by = user.username
        boxArea= 2*(boxLength*boxWidth +boxLength*boxHeight +boxWidth*boxHeight )
        boxVolume= boxLength*boxWidth*boxHeight
        valid, msg= validate_box(boxCreated_by, boxArea, boxVolume)
        if valid:
            box = BoxModel.objects.create(name=boxName, length=boxLength, width=boxWidth, height=boxHeight, area=boxArea, volume= boxVolume, created_by= boxCreated_by, updated_by=boxUpdated_by)
            box.save()
            print(BoxModel.objects.all().values())
            return HttpResponse('Box created')
        else:
            resp= 'Constraints failed. Box addition failed due to '+ msg
            return HttpResponse(resp)
    else:
        return HttpResponse('Error creating box'+ str(req.user.is_authenticated)+ str(req.user.is_staff))


# Create your views here.
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
@csrf_exempt
def updateBox(req, id):
    user=  get_user(req)
    if req.method == 'POST' and is_staff(user):
        boxName = req.POST['name']
        boxLength = int(req.POST['length'])
        boxWidth = int(req.POST['width'])
        boxHeight = int(req.POST['height'])
        boxUpdated_by = user.username
        boxArea= 2*(boxLength*boxWidth +boxLength*boxHeight +boxWidth*boxHeight )
        boxVolume= boxLength*boxWidth*boxHeight

        box = BoxModel.objects.get(id=id)
        old_area= box.area
        old_volume= box.volume
        valid, msg= validate_box(box.created_by, boxArea-old_area, boxVolume-old_volume)
        if valid:
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
            return HttpResponse('Constraints failed. Box updation failed due to ', msg)

    else:
        return HttpResponse('Error updating box')

@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
@csrf_exempt
def deleteBox(req, id):
    user=  get_user(req)
    # if req.method == 'DELETE' and is_authenticated(req) and is_staff(req):
    if req.method == 'DELETE' and is_staff(user):
        box = BoxModel.objects.get(id=id)
        box.delete()
        return HttpResponse('Box deleted')
    else:
        return HttpResponse('Error deleting box')


@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
@csrf_exempt
def listBox(req):
    user=  get_user(req)
    if req.method == 'GET':
        total_area= BoxModel.objects.aggregate(Sum('area'))
        total_volume= BoxModel.objects.aggregate(Sum('volume'))
        total_individual_box_count= BoxModel.objects.filter(created_by=user.username).count()
        total_boxes= BoxModel.objects.all().count()
        filtered_data= filter_boxes(req, user)
        print(filtered_data)
        return JsonResponse(
            {
            'status': 200,
            'filtered Data': str(filtered_data),
            'total_boxes_retrieved': len(filtered_data),
            'user': str(user.username), 
            'total_area': total_area, 
            'total_volume': total_volume, 
            'total_individual_area': total_individual_box_count, 
            'total_boxes': total_boxes
            }
            )
    else:
        return HttpResponse('Error listing boxes')




def filter_boxes(request, user):
    length_more_than = request.GET.get('length_more_than', 0)
    area_more_than = request.GET.get('area_more_than', 0)
    volume_more_than = request.GET.get('volume_more_than', 0)
    height_more_than = request.GET.get('height_more_than', 0)
    width_more_than = request.GET.get('width_more_than', 0)

    # just for a maximum value as float('inf') is not working
    maxm= 10000000000
    length_less_than = request.GET.get('length_less_than', maxm)
    area_less_than = request.GET.get('area_less_than', maxm)
    volume_less_than = request.GET.get('volume_less_than', maxm)
    height_less_than = request.GET.get('height_less_than', maxm)
    width_less_than = request.GET.get('width_less_than', maxm)

    created_by = request.GET.get('created_by', None)

    # print('ll:', length_more_than, length_less_than)
    boxes= BoxModel.objects.filter(
        Q(length__gte=length_more_than) & 
        Q(area__gte=area_more_than) & 
        Q(volume__gte=volume_more_than) & 
        Q(height__gte=height_more_than) & 
        Q(width__gte=width_more_than)&
        Q(length__lte= length_less_than)&
        Q(width__lte= width_less_than)&
        Q(height__lte= height_less_than)&
        Q(area__lte= area_less_than)&
        Q(volume__lte= volume_less_than)
        )
    
    if created_by:
        boxes = boxes.filter(created_by=created_by)

    if not is_staff(user):
        exclude_keys = ['created_by', 'updated_by']
        filtered_boxes = [{key: value for key, value in box.items() if key not in exclude_keys} for box in boxes.values()]
        boxes = filtered_boxes
        return boxes
    
    else:
        filtered_boxes = [{key: value for key, value in box.items()} for box in boxes.values()]
        boxes = filtered_boxes
        return boxes

    return boxes.values()


@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
@csrf_exempt
def listBoxMe(req):
    user= get_user(req)
    if req.method == 'GET':
        boxes = BoxModel.objects.filter(created_by=user.username).values()
        total_individual_box_count= BoxModel.objects.filter(created_by=user.username).count()
        return JsonResponse({'status': 200,'boxes': str(boxes), 'user': str(user),'total_individual_count': total_individual_box_count})
    else:
        return HttpResponse('Error listing boxes'+ str(user)+ str(user.username))
