import json


class VkMessage:
    _fixed_payload = {}

    def __init__(self, message):
        self.peer_id = message['peer_id']
        self.text = message['text']
        self.is_user_msg = message['peer_id'] == message['from_id']
        if 'payload' in message:
            self._payload = message['payload']
        else:
            self._payload = None

    @property
    def fixed_payload(self):
        if not self._fixed_payload:
            if self._payload:
                try:
                    self._fixed_payload = json.loads(self._payload)
                except json.JSONDecodeError:
                    self._fixed_payload = {}
        return self._fixed_payload

    @property
    def payload_action(self):
        return self.fixed_payload.get("action")

    @property
    def payload_data(self):
        return self.fixed_payload.get("data")


class VkResponse:

    def __init__(self, request):
        if 'object' in request:
            self.message = VkMessage(request['object']['message'])
        self.secret = request['secret']
        self.type = request['type']
