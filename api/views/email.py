from django.http import HttpResponse
from api.models import EmailOffer
import uuid


def post_email(request):
    email_offer = EmailOffer(name="lw1140@163.com", id=uuid.uuid4(), own_company="阿里云")
    email_offer.save()
    return HttpResponse("success")


def get_email(request):

    pass
