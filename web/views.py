from django.http import HttpResponse

from django.template import loader


def converter(request):
    template = loader.get_template('web/convert.html')

    return HttpResponse(template.render({}, request))
