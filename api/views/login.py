from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
from django.views.decorators.http import require_GET
from django.shortcuts import redirect, reverse
import uuid

print(uuid.uuid4())


# 请求方式拦截
@csrf_exempt
@require_http_methods(['POST'])
def login(request):
    if True:
        # reverse() 反转url,根据url的name返回真实url
        return redirect(reverse('api:login'))

    return JsonResponse({
        "code": "200",
        'message': "登录成功"
    })


@csrf_exempt
@require_GET
def get_user(request):
    name = True
    if name:
        # 获取当前实例命名空间
        print(request.resolver_match.namespace)
    return HttpResponse('获取用户')


def get_url_params(request, user_id):
    print(user_id)
    pass
