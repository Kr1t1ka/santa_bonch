from django.http import HttpResponse
import rest_framework
from rest_framework import views

from bot.api.controller import State
from bot.api.router import controller
from bot.api.vk_models import VkResponse
from mc_kppk.settings import VK_CONFIRMATION_TOKEN, SECRET_KEY


class VkBotViewSet(views.APIView):

    def post(self, request, *_, **__):
        request = VkResponse(request.data)

        if request.secret != SECRET_KEY:
            return HttpResponse('ok')

        if request.type == 'confirmation':
            return HttpResponse(VK_CONFIRMATION_TOKEN,
                                status=rest_framework.status.HTTP_200_OK)
        if request.message.is_user_msg:
            state = State(request.message)
            controller.handle(state)

        return HttpResponse('ok', status=rest_framework.status.HTTP_200_OK)
