class Data:
    def __init__(self, command, message, content) -> None:
        super().__init__()

        self.command = command
        self.message = message
        self.content = content