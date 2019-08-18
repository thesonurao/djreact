from rest_framework.generics import ListAPIView, RetrieveAPIView
from articles.models import Stocks
from .serializers import StocksSerializer

class StocksListView(ListAPIView):
    queryset = Stocks.objects.all()
    serializer_class = StocksSerializer


class StocksDetailView(RetrieveAPIView):
    queryset = Stocks.objects.all()
    serializer_class = StocksSerializer
