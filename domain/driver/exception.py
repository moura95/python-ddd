class NameCannotBeEmpty(Exception):
    def __init__(self, message):
        self.message = message


class EmailCannotBeEmpty(Exception):
    def __init__(self, message):
        self.message = message
