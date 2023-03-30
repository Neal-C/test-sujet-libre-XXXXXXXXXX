from django.urls import path, include
from .views import BotList, BotDetail, FactoryList, FactoryDetail

urlpatterns = [
    path('bot/', BotList.as_view()),
    path('bot/<int:pk>', BotDetail.as_view()),
    path('factory/', FactoryList.as_view()),
    path('factory/<int:pk>',FactoryDetail.as_view())
]
