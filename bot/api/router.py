from bot.api.controller import Controller
from bot.api import endpoints
from bot.api.endpoints import main_endpoint

controller = Controller()
controller.add_endpoint(main_endpoint, as_default=True)

for endpoint in dir(endpoints):
    if "endpoint" in endpoint and 'main' not in endpoint:
        controller.add_endpoint(getattr(endpoints, endpoint))
