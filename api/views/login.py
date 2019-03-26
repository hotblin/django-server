from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
from django.views.decorators.http import require_GET


@csrf_exempt
@require_http_methods(['POST'])
def login(request):
    return JsonResponse({
        "code": "200",
        'message': "登录成功"
    })


@csrf_exempt
@require_GET
def get_user(request):
    return HttpResponse('获取用户')
