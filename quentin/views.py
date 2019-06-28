from ebpy.mq import receive_message, NotQueueReceiver

from django.http import HttpResponse, Http404
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def receive(request):
    try:
        receive_message(request.body)
    except NotQueueReceiver:
        raise Http404()
    return HttpResponse('ok', content_type='text/plain')


