from .tasks import notify_customers
from django.core.cache import cache
from django.core.mail import send_mail, BadHeaderError, mail_admins, EmailMessage
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from rest_framework.response import Response
from rest_framework.views import APIView
from templated_mail.mail import BaseEmailMessage
import requests
import logging

logger = logging.getLogger(__name__)


class SayHello(APIView):

    @method_decorator(cache_page(2*60))
    def get(self, request):
        # try:
        #     # response = requests.get("https://httpbin.org/delay/2")
        #     # data = response.json()
        #     # logger.info("salam")
        # except requests.ConnectionError:
        #     pass

        # notify_customers.delay("hello")
        # try:

        #     message = BaseEmailMessage(
        #         context={"name": "Ali"},
        #         template_name="emails/hello.html"
        #     )
        #     message.send(to=['john@mosh.com'])
        # except BadHeaderError:
        #     print("bad")
        return Response({'name': 'data'}, status=200)


@cache_page(2*60)
def say_hello(request):
    # response = requests.get("https://httpbin.org/delay/2")
    # data = response.json()

    # notify_customers.delay("hello")
    # try:

    #     message = BaseEmailMessage(
    #         context={"name": "Ali"},
    #         template_name="emails/hello.html"
    #     )
    #     message.send(to=['john@mosh.com'])
    # except BadHeaderError:
    #     print("bad")
    return render(request, 'hello.html', {'name': 'data'})
