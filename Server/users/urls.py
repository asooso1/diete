from django.urls import path
from . import views
from rest_framework_jwt.views import obtain_jwt_token


app_name = 'users'

urlpatterns = [
    # 회원가입
    path('join/', views.join),
    
    # 로그인
    path('api-token-auth/', obtain_jwt_token),
    #  path('login/', views.login),
    
    # 아이디 중복 확인
    path('id/<str:username>/', views.check_id),
    
    # 회원정보 업데이트
    path('update/', views.update_user_info),
]