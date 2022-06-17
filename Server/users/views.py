# from django.shortcuts import render
import imp
from django.http import HttpResponse  
from django.http.response import JsonResponse
from django.contrib.auth import get_user_model
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework import  status
from .serializers import UserSerializer, UserProfileSerializer
from menus.serializers import MenuSerializer, MenuToFoodSerializer
from rest_framework_jwt.authentication import JSONWebTokenAuthentication

# kcal 계산
def get_user_kcal(data, gender):
    H = float(data.get('height'))
    a = data.get('activity')
    kcal = data.get('kcal')
    # 활동량이 적을 경우(ACTIVITY = 0)
    if a == '적음':
        # 남자인 경우(GENDER = 0)
        if gender == 0:
            avgKg = (H/100)**2 * 22
            kcal = avgKg * 27

        # 여자인 경우(GENDER = 1)    
        elif gender == 1:
            avgKg = (H/100)**2 * 21 
            kcal = avgKg * 27
            
    # 활동량이 보통일 경우(ACTIVITY = 0)        
    elif a == '보통':
        if gender == 0:
            avgKg = (H/100)**2 * 22
            kcal = avgKg * 33
        elif gender == 1:
            avgKg = (H/100)**2 * 21
            kcal = avgKg * 33

    # 활동량이 많을 경우(ACTIVITY = 2)
    elif a == '많음':
        if gender == 0:
            avgKg = (H/100)**2 * 22
            kcal = avgKg * 38
        elif gender == 1:
            avgKg = (H/100)**2 * 21
            kcal = avgKg * 38
    return kcal

# 회원 가입
@api_view(['POST'])
@permission_classes([AllowAny])
def join(request):
    password = request.data.get('password')
    serializer = UserSerializer(data=request.data)
    menuSerializer = MenuSerializer(data=request.data)
    
    if serializer.is_valid(raise_exception=True):
        user = serializer.save()
        user.set_password(password)
        user.kcal = get_user_kcal(request.data, gender=user.gender)
        user.save()
    # 선호 식단을 골랐을 떄 들어가는 식단
        preference = request.data.get('preference')
        
        #채소 선호 식단을 골랐을 경우 
        if preference == '채소':
            menudata = { 
            "userId" : user.id,
            "dateTime" : "2000-01-01",
            "mealTime" : 0
            }
            
            menuSerializer = MenuSerializer(data=menudata)
            if menuSerializer.is_valid(raise_exception=True) :
                menuSerializer.save()
                menuTempId = menuSerializer.data["id"]
            else:
                return Response({'error': 'menu 테이블 삽입 에러'}, status=status.HTTP_400_BAD_REQUEST)
            
            menus = [6967, 6879, 7026, 7048, 7208, 7290]
            print(menus)
            for menu in menus:
                basketdata = {
                    "menuId" : menuTempId,
                    "foodId" : menu,
                    "amount" : 1,
                }
                mtfSerializer = MenuToFoodSerializer(data=basketdata)
                if mtfSerializer.is_valid(raise_exception=True):
                    mtfSerializer.save()
                else:
                    return Response({'error': 'menutofood 테이블 삽입 에러'}, status=status.HTTP_400_BAD_REQUEST)
                
            menudata = { 
            "userId" : user.id,
            "dateTime" : "2000-01-01",
            "mealTime" : 1
            }
             
            menuSerializer = MenuSerializer(data=menudata)
            if menuSerializer.is_valid(raise_exception=True) :
                menuSerializer.save()
                menuTempId = menuSerializer.data["id"]
            else:
                return Response({'error': 'menu 테이블 삽입 에러'}, status=status.HTTP_400_BAD_REQUEST)
            
            menus = [7007, 6884, 7023, 7047, 7222, 5]
            print(menus)
            for menu in menus:
                basketdata = {
                    "menuId" : menuTempId,
                    "foodId" : menu,
                    "amount" : 1,
                }
                mtfSerializer = MenuToFoodSerializer(data=basketdata)
                if mtfSerializer.is_valid(raise_exception=True):
                    mtfSerializer.save()
                else:
                    return Response({'error': 'menutofood 테이블 삽입 에러'}, status=status.HTTP_400_BAD_REQUEST)
                
            menudata = { 
            "userId" : user.id,
            "dateTime" : "2000-01-01",
            "mealTime" : 2
            }
            
            menuSerializer = MenuSerializer(data=menudata)
            if menuSerializer.is_valid(raise_exception=True) :
                menuSerializer.save()
                menuTempId = menuSerializer.data["id"]
            else:
                return Response({'error': 'menu 테이블 삽입 에러'}, status=status.HTTP_400_BAD_REQUEST)
            
            menus = [6967, 6886, 6925, 7073, 7190, 7116]
            print(menus)
            for menu in menus:
                basketdata = {
                    "menuId" : menuTempId,
                    "foodId" : menu,
                    "amount" : 1,
                }
                mtfSerializer = MenuToFoodSerializer(data=basketdata)
                if mtfSerializer.is_valid(raise_exception=True):
                    mtfSerializer.save()
                else:
                    return Response({'error': 'menutofood 테이블 삽입 에러'}, status=status.HTTP_400_BAD_REQUEST)
                
        # 고기 선호 식단을 골랐을 경우
        elif preference == '고기':
            menudata = { 
            "userId" : user.id,
            "dateTime" : "2000-01-01",
            "mealTime" : 0
            }
            
            menuSerializer = MenuSerializer(data=menudata)
            if menuSerializer.is_valid(raise_exception=True) :
                menuSerializer.save()
                menuTempId = menuSerializer.data["id"]
            else:
                return Response({'error': 'menu 테이블 삽입 에러'}, status=status.HTTP_400_BAD_REQUEST)
            
            menus = [137, 7, 7055, 7216, 261]
            for menu in menus:
                basketdata = {
                    "menuId" : menuTempId,
                    "foodId" : menu,
                    "amount" : 1,
                }
                mtfSerializer = MenuToFoodSerializer(data=basketdata)
                if mtfSerializer.is_valid(raise_exception=True):
                    mtfSerializer.save()
                else:
                    return Response({'error': 'menutofood 테이블 삽입 에러'}, status=status.HTTP_400_BAD_REQUEST)
           
            menudata = { 
            "userId" : user.id,
            "dateTime" : "2000-01-01",
            "mealTime" : 1
            }
            
            menuSerializer = MenuSerializer(data=menudata)
            if menuSerializer.is_valid(raise_exception=True) :
                menuSerializer.save()
                menuTempId = menuSerializer.data["id"]
            else:
                return Response({'error': 'menu 테이블 삽입 에러'}, status=status.HTTP_400_BAD_REQUEST)
            
            menus = [6967, 9, 203, 4256, 6866, 261]
            print(menus)
            for menu in menus:
                basketdata = {
                    "menuId" : menuTempId,
                    "foodId" : menu,
                    "amount" : 1,
                }
                mtfSerializer = MenuToFoodSerializer(data=basketdata)
                if mtfSerializer.is_valid(raise_exception=True):
                    mtfSerializer.save()
                else:
                    return Response({'error': 'menutofood 테이블 삽입 에러'}, status=status.HTTP_400_BAD_REQUEST)


            menudata = { 
            "userId" : user.id,
            "dateTime" : "2000-01-01",
            "mealTime" : 2
            }
            
            menuSerializer = MenuSerializer(data=menudata)
            if menuSerializer.is_valid(raise_exception=True) :
                menuSerializer.save()
                menuTempId = menuSerializer.data["id"]
            else:
                return Response({'error': 'menu 테이블 삽입 에러'}, status=status.HTTP_400_BAD_REQUEST)
            
            menus = [ 7020, 242, 7030, 6859, 4256, 6866]
            print(menus)
            for menu in menus:
                basketdata = {
                    "menuId" : menuTempId,
                    "foodId" : menu,
                    "amount" : 1,
                }
                mtfSerializer = MenuToFoodSerializer(data=basketdata)
                if mtfSerializer.is_valid(raise_exception=True):
                    mtfSerializer.save()
                else:
                    return Response({'error': 'menutofood 테이블 삽입 에러'}, status=status.HTTP_400_BAD_REQUEST)
            
            
        # 일반 식단을 골랐을 경우
        elif preference == '일반':
            return Response({'message' : '일반 식단'}, status=status.HTTP_200_OK)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


# ID 중복체크
@api_view(['GET'])
@permission_classes([AllowAny])
def check_id(response, username):
    User = get_user_model()
    data = {'isUnique': not User.objects.filter(username=username).exists()}
    return JsonResponse(data)

# 회원 정보 수정
@api_view(['PUT'])
@authentication_classes([JSONWebTokenAuthentication])
@permission_classes([IsAuthenticated])
def update_user_info(request):
    
    User = get_user_model()
    # if request.user.username != request.data.get('username') and User.objects.filter(username=request.data.get('username')).exists():
    #         return Response({'error': '일치하는 닉네임이 존재합니다.'}, status=status.HTTP_400_BAD_REQUEST)
    serializer = UserProfileSerializer(request.user, data=request.data)

    if serializer.is_valid(raise_exception=True):
        user = serializer.save()
        # kcal 다시 계산하고 serializer에추가
        user.kcal = get_user_kcal(data=request.data, gender=request.user.gender)
        print(user.kcal)
        user.save()
        return Response(serializer.data)