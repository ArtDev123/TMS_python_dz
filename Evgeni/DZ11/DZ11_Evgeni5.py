from typing import Union


class SuperStr(str):
    def is_repeatance(self, s: Union[str, "SuperStr"]) -> bool:
        """
        Проверяет, можно ли представить текущую строку как целое число повторов строки s.
        Пустая строка не считается повтором.

        Пример:
          "abcabcabc".is_repeatance("abc") -> True
          "abcabcab".is_repeatance("abc") -> False
          "".is_repeatance("abc") -> False
        """
        if not s:
            return False
        if not isinstance(s, str):
            raise TypeError("Argument s must be a string")
        if len(self) == 0:
            return False
        if len(self) % len(s) != 0:
            return False
        repeat_count = len(self) // len(s)
        return s * repeat_count == self

    def is_palindrom(self) -> bool:
        """
        Проверяет, является ли строка палиндромом, игнорируя регистр.
        Пустая строка считается палиндромом.

        Пример:
          "Level".is_palindrom() -> True
          "Test".is_palindrom() -> False
          "".is_palindrom() -> True
        """
        lowered = self.lower()
        return lowered == lowered[::-1]


if __name__ == "__main__":
    s1 = SuperStr("abcabcabc")
    print(s1.is_repeatance("abc"))
    print(s1.is_repeatance("ab"))

    s2 = SuperStr("Level")
    print(s2.is_palindrom())

    s3 = SuperStr("")
    print(s3.is_palindrom())
    print(s3.is_repeatance("a"))
