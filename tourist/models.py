from django.db import models

class Tourist(models.Model):
    first_name = models.CharField(max_length=128, blank=True, default='')
    last_name = models.CharField(max_length=128, blank=True, default='')
    passport = models.CharField(max_length=20, blank=True, default='')
    email = models.EmailField(max_length=64, blank=True, default='')
    telephone = models.CharField(max_length=20, blank=True, default='')
    country = models.CharField(max_length=64, blank=True, default='')
    city = models.CharField(max_length=64, blank=True, default='')
    state = models.CharField(max_length=64, blank=True, default='')
    zip_code = models.CharField(max_length=10, blank=True, default='')
    street_address = models.CharField(max_length=255, blank=True, default='')
    lat = models.CharField(max_length=30, blank=True, default='') #latitude
    lon = models.CharField(max_length=30, blank=True, default='') #longitude
    
    def __unicode__(self):
        return '%s, %s' % (self.last_name, self.first_name)
        
    def current_location(self):
        return 'lon: %s, lat: %s' % (self.lon, self.lat)
        
    def update_current_location(self, lon, lat):
        self.lon = lon
        self.lat = lat
        self.save()
    
    
    
class Card(models.Model):
    id_number = models.CharField(max_length=64, unique=True)
    tourist = models.ForeignKey('Tourist', blank=True, null=True)
    
    def __unicode__(self):
        return 'id: %s, user: %s' % (self.id_number, self.tourist)
    
    def available(self):
        return not bool(self.tourist)
    
