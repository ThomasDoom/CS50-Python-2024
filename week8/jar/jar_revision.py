class Jar:
    def __init__(self, capacity=12):
        self._input_check(capacity, "Capacity")
        self._capacity = capacity
        self._cookies = 0

    def __str__(self):
        return "🍪" * self._cookies

    def deposit(self, n):
        self._operation_check(n, "Deposit")
        self._cookies += n

    def withdraw(self, n):
        self._operation_check(n, "Withdrawal")
        self._cookies -= n

    @property
    def capacity(self):
        return self._capacity

    @property
    def size(self):
        return self._cookies

    def _operation_check(self, n, operation):
        self._input_check(n, operation)
        if operation == "Deposit" and self._cookies + n > self._capacity:
            raise ValueError("Cookies are oVERFLOWINGGG!!")
        if operation == "Withdrawal" and n > self._cookies:
            raise ValueError("Not enough cookies in the jar!")

    @staticmethod
    def _input_check(n, name):
        if not isinstance(n, int) or n < 0:
            raise ValueError(f"{name} must be a positive integer!")
