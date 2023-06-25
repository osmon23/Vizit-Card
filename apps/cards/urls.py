from django.urls import path

from .views import VizitCardView

urlpatterns = [
    path('', VizitCardView.as_view(), name='index'),
]
