from django.shortcuts import render
from django.http import HttpResponseBadRequest, HttpResponse
import json
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from tourist.tasks import task_update_location

@csrf_exempt
@require_POST
def update_location(request):
    try:
        card_id = request.POST['card_id']
        latitude = request.POST['latitude']
        longitude = request.POST['longitude']
        
        task_update_location.delay(card_id, longitude, latitude)
        
        response = json.dumps({'status': 200})
        return HttpResponse(response, content_type='application/json')
    except Exception as error:
        return HttpResponseBadRequest(json.dumps({'error': str(error)}), content_type='application/json')
