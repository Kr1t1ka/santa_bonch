from bot.api.endpoint import Endpoint


def handler(state):
    pass


info_endpoint = Endpoint(
    name="info",
    title="Какая-то информация",
    description="немного полезной информации",
    handler=handler,
    keyboard=[],
)
