from ebpy.async import receive_message, NotAsyncReceiver, SignatureMismatch

from django.http import HttpResponse, Http404
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def receive(request):
    try:
        receive_message(request.body)
    except (NotAsyncReceiver, SignatureMismatch):
        raise Http404()
    return HttpResponse('ok', content_type='text/plain')


