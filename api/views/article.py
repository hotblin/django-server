from django.http import HttpResponse
from api.models import Article


def get_aiticle(request):
    article = Article()
    return HttpResponse("success")