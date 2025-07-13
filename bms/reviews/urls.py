from django.urls import path
from .serializers import *
from .views import *
urlpatterns = [
    path('review/',ReviewListView.as_view())
]