from django.urls import path
from .views import StocksListView, StocksDetailView


urlpatterns = [
    path('', StocksListView.as_view()),
    path('<pk>', StocksDetailView.as_view()),
]