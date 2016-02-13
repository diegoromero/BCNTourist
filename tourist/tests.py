from django.test import TestCase
from tourist.models import Tourist, Card

class TouristTestCase(TestCase):
    def setUp(self):
        Tourist.objects.create(first_name = 'first_name',
                                last_name = 'last_name',
                                passport = 'passport',
                                email = 'email@domain.com',
                                telephone = 'telephone',
                                country = 'country',
                                city = 'city',
                                state = 'state',
                                zip_code = 'zip_code',
                                street_address = 'street_address',
                                lat = '0',
                                lon =  '40',
                                )

    def test_tourist_current_location(self):
        tourist = Tourist.objects.get(first_name="first_name")
        self.assertEqual(tourist.current_location(), 'lon: 40, lat: 0')
        
    def test_tourist_update_location(self):
        tourist = Tourist.objects.get(first_name="first_name")
        tourist.update_current_location('10', '-10')
        self.assertEqual(tourist.current_location(), 'lon: 10, lat: -10')
        
class CardTestCase(TestCase):
    def setUp(self):
        Tourist.objects.create(first_name = 'first_name',
                                last_name = 'last_name',
                                passport = 'passport',
                                email = 'email@domain.com',
                                telephone = 'telephone',
                                country = 'country',
                                city = 'city',
                                state = 'state',
                                zip_code = 'zip_code',
                                street_address = 'street_address',
                                lat = '0',
                                lon =  '40',
                                )
        Card.objects.create(id_number='123')
        tourist = Tourist.objects.get(first_name="first_name")
        Card.objects.create(id_number='321', tourist=tourist)
        
    def test_card_availability(self):
        card1 = Card.objects.get(id_number='123')
        card2 = Card.objects.get(id_number='321')
        self.assertEqual(card1.available(), True)
        self.assertEqual(card2.available(), False)