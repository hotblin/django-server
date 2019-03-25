from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods

from django.views.decorators.http import require_GET


@csrf_exempt
@require_http_methods(['POST'])
def index(request):
    return JsonResponse({
        "code": "200"
    })


# require_GET() - 声明被装饰的视图仅支持GET方法
# require_POST() - 声明被装饰的视图仅支持POST方法
# require_SAFE() - 声明被装饰的视图仅支持GET和HEAD方法


@require_GET
def sub_index(request):
    return HttpResponse("Hello, world. You're at the polls index.")
