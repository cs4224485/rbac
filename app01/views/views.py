from django.shortcuts import render,HttpResponse, redirect

# Create your views here.

from rbacapp.models import *
from rbacapp.service import permission
import re



def add_user(request):

    return HttpResponse('ok')


def role(request):
    role_list = Role.objects.all()
    return HttpResponse('角色')


def login(request):
    if request.method == 'POST':
        user = request.POST.get('username')
        pwd = request.POST.get('password')
        print(user, pwd)
        user_obj = User.objects.filter(name=user, pwd=pwd).first()
        if user_obj:
            # 在session中注册用户ID
            request.session['user_id'] = user_obj.pk

            # 查询当前登录用户的所有角色
            user_obj.roles.all()

            # 查询当前登录用户的所有权限
            permission_data = user_obj.roles.filter(permissions__isnull=False).values("permissions__url", "permissions__group_id", "permissions__action").distinct()

            # 构建权限，并保存到session
            permission.initial_session(request, permission_data)

            '''
                    备注: 此方案信息不够需要重新构建
                    #将权限信息保存到session
                    permission_list = []
                    for item in permission:
                        permission_list.append(item['permissions__url'])
                    request.session['permission'] = permission_list
                    return HttpResponse('登录成功')
             '''
            return redirect('/customer/list/')

    return render(request, 'login.html')