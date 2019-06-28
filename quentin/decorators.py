from ebpy.mq import ebsqs_worker, ebsqs_cron

from django.http import HttpResponse, Http404


class quentin_worker(ebsqs_worker):
    pass


class quentin_cron(ebsqs_cron):
    """decorator class for cron views"""

    def __init__(self, cron_function):
        super(quentin_cron, self).__init__(
            cron_function,
            csrf_exempt = True,
            http404_exception_class = Http404,
            http_response = HttpResponse('ok cron', content_type='text/plain')
            )


