class SuperStr(str):

    def is_repeatance(self, s: str) -> bool:
        if len(self) % len(s) != 0:
            return False
        repeats = len(self) // len(s)
        return self == s*repeats

    def is_palindrom(self) -> bool:
        new_s = self.lower()
        return new_s == new_s[::-1]
