from amom.protocol import Protocol


class Openwire(Protocol):
    def __init__(self, default_port=5672):
        super(Openwire, self).__init__(default_port)