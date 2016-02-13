from celery import shared_task
from tourist.models import Card

@shared_task
def task_update_location(card_id, longitude, latitude):
    try:
        card = Card.objects.get(id_number=card_id)
        tourist = card.tourist
        
        tourist.update_current_location(longitude, latitude)
    except:
        pass
