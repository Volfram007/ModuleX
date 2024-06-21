class EvenNumbers:
    def __init__(self, start=0, end=1):
        if start == end:
            raise ValueError('"start" и "end" числа не могут быть равны')
        elif start > end:
            start, end = end, start
            # raise ValueError('"start" число должно быть меньше "end"')

        self.start = start if start % 2 == 0 else start + 1
        self.end = end if end % 2 == 1 else end + 1

    def __iter__(self):
        self.current = self.start
        return self

    def __next__(self):
        if self.current <= self.end:
            result = self.current
            self.current += 2
            return result
        else:
            raise StopIteration


try:
    en = EvenNumbers(10, 25)
    for i in en:
        print(i)
except ValueError as e:
    print(f"Ошибка: {e}")
