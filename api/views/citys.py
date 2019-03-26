from django.views.generic import View
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, JsonResponse
from django.utils.decorators import method_decorator


def my_decorator(func):
    # 此处增加了self
    def wrapper(request, *args, **kwargs):
        print('自定义装饰器被调用了')
        print('请求路径%s' % request.path)
        return func(request, *args, **kwargs)

    return wrapper


# csrf_exempt 取消当前函数，跨站请求伪造功能
# 定义类视图

class CityView(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super(CityView, self).dispatch(request, *args, **kwargs)

    def get(self, request):
        return HttpResponse('111')

    def put(self):
        pass

    def post(self, request):
        return JsonResponse({
            "code": 200
        })


@method_decorator(my_decorator, name='dispatch')
@method_decorator(csrf_exempt, name='dispatch')
class CalcCity(View):
    model = []

    def get(self, request):
        return HttpResponse("calc_city get_methods")

    def post(self, request):
        return JsonResponse({
            "code": 200
        })
