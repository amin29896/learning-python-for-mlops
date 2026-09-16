class limitexception(Exception):
    def __init__(self):
        super().__init__("you puted a number bigger than the maximum input value")

