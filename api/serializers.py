from rest_framework import serializers
from .models import Bot, Factory

class BotSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bot
        fields = ('__all__')

class FactorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Factory
        fields = ('__all__')