import random
from mc_kppk.settings import VK_TOKEN

URL = "https://api.vk.com/method/"
DEFAULT_DATA = {
    "access_token": VK_TOKEN,
    "v": "5.131",
}


def send_message(session, data):
    if not data["keyboard"]:
        del data["keyboard"]
    session.post(
        f"{URL}messages.send",
        data={
            **data,
            **DEFAULT_DATA,
            "random_id": random.randint(-2147483648, +2147483648),
        },
    )
