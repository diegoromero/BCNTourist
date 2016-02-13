from django.contrib import admin
from haystack.admin import SearchModelAdmin
from tourist.models import Tourist, Card
from django.utils.translation import ugettext_lazy as _

class TouristAdmin(SearchModelAdmin):
    fields = ('first_name', 'last_name', 'email', 'telephone', 'passport', 'country', 'city', 'state', 'zip_code', 'street_address' )
    list_display = ('first_name', 'last_name', 'telephone', 'country', 'passport', 'current_location' )
    list_filter = ('country',)
    search_fields = ('first_name', 'last_name', 'email', 'telephone', 'passport', 'country', 'city', 'state', 'zip_code', 'street_address')
    
class AvailableCardListFilter(admin.SimpleListFilter):
    # Human-readable title which will be displayed in the
    # right admin sidebar just above the filter options.
    title = _('card available')

    # Parameter for the filter that will be used in the URL query.
    parameter_name = 'available'

    def lookups(self, request, model_admin):
        """
        Returns a list of tuples. The first element in each
        tuple is the coded value for the option that will
        appear in the URL query. The second element is the
        human-readable name for the option that will appear
        in the right sidebar.
        """
        return (
            (True, 'True'),
            (False, 'False'),
        )

    def queryset(self, request, queryset):
        """
        Returns the filtered queryset based on the value
        provided in the query string and retrievable via
        `self.value()`.
        """
        if self.value() == 'True':
            return queryset.filter(tourist__isnull=True)
        if self.value() == 'False':
            return queryset.exclude(tourist__isnull=True)
    
    
class CardAdmin(SearchModelAdmin):
    list_display = ('id_number', 'tourist', 'available' )
    list_filter = (AvailableCardListFilter,)
    search_fields = ('id_number', 'tourist__last_name', 'tourist__first_name',)
    
admin.site.register(Tourist, TouristAdmin)
admin.site.register(Card, CardAdmin)