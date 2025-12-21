# Bad version intentionally violates conventions for testing

MAXABSRESULT = 1000000  # should be UPPER_SNAKE_CASE and readable

class calculator:  # class should be PascalCase
    def __init__(self, cfg=None):
        self.cfg = cfg or {"max": MAXABSRESULT}  # hidden dict config

    def Add(self, a, b):  # should be snake_case
        try:
            r = a + b
            if r > self.cfg["max"]:
                return self.cfg["max"]
            if r < -self.cfg["max"]:
                return -self.cfg["max"]
            return r
        except:
            return 0  # swallowing errors silently is bad

    def sub(self, a, b):
        return self.Add(a, -b)  # relies on Add naming mismatch
