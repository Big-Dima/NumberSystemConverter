import json
from django.http import HttpResponse, Http404
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def des_convert_base(request):
    def convert_base(num, to_base, from_base):
        if request.method != 'POST':
            raise Http404

        if isinstance(num, str):
            n = int(num, from_base)
        else:
            n = int(num)

        alphabet = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"

        if n < to_base:
            return alphabet[n]
        else:
            return convert_base(n // to_base, to_base, from_base) + alphabet[n % to_base]

    num = request.POST.get("number", "")
    to_base = int(request.POST.get("notation1", ""))
    from_base = int(request.POST.get("notation", ""))
    result = convert_base(num, to_base, from_base)
    response = {
        "result": result
    }
    return HttpResponse(json.dumps(response),
                        status=200,
                        content_type='application/json; charset=utf-8')
