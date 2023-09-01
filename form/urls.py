from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='index'),
    path('login', views.login_view, name='login'),
    path('logout', views.logout_view, name = 'logout'),
    path('eventform', views.eventform, name='eventform'),
    path('events', views.events, name='events'),
    path('event/<int:event_id>', views.event, name='event'),
]