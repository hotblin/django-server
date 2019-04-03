from django.http import HttpResponse
from api.models import Business
import uuid
from django.utils.timezone import now,localtime
print(now())
print(localtime())

def get_business(request):
    # 1. 新建
    business = Business(id=uuid.uuid4(), name="北京天安门", created_at='')
    business.save()

    # 2. 查询
    try:
        bus = Business.objects.get(id="")
        buss = Business.objects.filter(name="长安").first()
    #     filter 返回列表
    except Exception as err:
        print(err)

    # 3.删除数据，先查询，再删除
    business1 = Business.objects.get(id='1')
    business1.delete()

    # 4. 修改数据

    business3 = Business.objects.get(id='222')
    business3.name = '修改名称'

    return HttpResponse("get business")
