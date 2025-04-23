from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Game, Customer, Order, Genre
from .serializers import GameSerializer, GenreSerializer

class GameViewSet(viewsets.ModelViewSet):
    queryset = Game.objects.all()
    serializer_class = GameSerializer

class GenreViewSet(viewsets.ModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer  

@api_view(['GET'])
def report_view(request):
    total_games = Game.objects.count()
    total_customers = Customer.objects.count()
    total_orders = Order.objects.count()
    report = {
        "total_games": total_games,
        "total_customers": total_customers,
        "total_orders": total_orders
    }
    return Response(report)