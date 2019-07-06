from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
import json


@csrf_exempt
def do_main(request):
    if request.method == 'POST':
        reply = ''
        request_json = json.loads(request.body.decode('utf-8'))
        if(request_json != None):
            for event in request_json['events']:
                reply_token = event['replyToken']
                message_type = event['message']['type']
                
                if message_type == 'text':
                    text = event['message']['text']
                    print(text)


    return HttpResponse(status=200)


