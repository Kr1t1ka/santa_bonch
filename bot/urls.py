from django.urls import path, include

from .views import (
    VkBotViewSet
)


urlpatterns = [
    path("bot/", VkBotViewSet.as_view()),
]