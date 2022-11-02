from bot.api.endpoint import Endpoint


def handler(state):
    pass


main_endpoint = Endpoint(
    name="main",
    title="Главная",
    description="Привет, я простенькой бот",
    handler=handler,
    keyboard=[['info', 'author']],
)
