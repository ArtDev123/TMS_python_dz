# Разработать класс SuperStr, который наследует
# функциональность стандартного типа str и содержит два
# новых метода:
# ● метод is_repeatance(s), который принимает некоторую
# строку и возвращает True или False в зависимости от того,
# может ли текущая строка быть получена целым
# количеством повторов строки s. Считать, что пустая
# строка не содержит повторов
# ● метод is_palindrom(), который возвращает True или False в
# зависимости от того, является ли строка палиндромом вне
# зависимости от регистра. Пустую строку считать
# палиндромом.

class SuperStr(str):

    def is_repeatance(self, s: str) -> bool:
        if len(self) % len(s) != 0:
            return False
        repeats = len(self) // len(s)
        return self == s*repeats

    def is_palindrom(self) -> bool:
        new_s = self.lower()
        return new_s == new_s[::-1]
