from django.urls import path
from wishlist.views import show_wishlist, return_XML, return_JSON, return_ID

app_name = 'wishlist'

urlpatterns = [
    path('', show_wishlist, name='show_wishlist'),
    path('xml/', return_XML, name='return_XML'),
    path('json/', return_JSON, name='return_JSON'),
    path('json/<int:id>', return_ID, name='return_ID')
]