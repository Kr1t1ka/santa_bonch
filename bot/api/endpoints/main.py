from bot.api.endpoint import Endpoint


def handler(state):
    pass


main_endpoint = Endpoint(
    name="main",
    title="Хочу участвовать!",
    description="Вот ссылка - https://clck.ru/32mmCc \n"
                "Переходи и заполняй форму!",
    handler=handler,
    keyboard=[['main']],
)
