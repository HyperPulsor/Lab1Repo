from django.urls import path
from wishlist.views import *

app_name = 'wishlist'

urlpatterns = [
    path('', show_wishlist, name='show_wishlist'),
    path('ajax/', show_ajax_wishlist, name='show_ajax_wishlist'),
    path('ajax/submit/', add_wishlist, name='add_wishlist'),
    path('xml/', return_XML, name='return_XML'),
    path('json/', return_JSON, name='return_JSON'),
    path('json/<int:id>', return_ID, name='return_ID'),
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
]