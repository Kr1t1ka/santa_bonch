from bot.api.endpoint import Endpoint


def handler(state):
    pass


author_endpoint = Endpoint(
    name="author",
    title="Автор",
    description="дуров",
    handler=handler,
    keyboard=[],
)
