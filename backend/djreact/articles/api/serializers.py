from rest_framework import serializers
from articles.models import Stocks

class StocksSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stocks
        fields = ('label', 'values')