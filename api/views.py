# Create your views here.

from rest_framework import generics
from .models import Bot, Factory
from .serializers import BotSerializer, FactorySerializer


class BotList(generics.ListCreateAPIView):
    """
    API endpoint that allows users to be viewed or edited.
    """
    #queryset = User.objects.all().order_by('-date_joined')
    serializer_class = BotSerializer

    def get_queryset(self):
        queryset = Bot.objects.all()
        factory = self.request.query_params.get('factory')
        if factory is not None:
            queryset = queryset.filter(botFactory=factory)
        return queryset

class BotDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = BotSerializer
    queryset = Bot.objects.all()

class FactoryList(generics.ListCreateAPIView):
    serializer_class = FactorySerializer
    queryset = Factory.objects.all()

class FactoryDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = FactorySerializer
    queryset = Factory.objects.all()



    """
    API endpoint that allows groups to be viewed or edited.
    """