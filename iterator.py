class Iterator:
    def __init__(self, start, stop):
        self._current = start
        self._stop = stop

    def __iter__(self):
        return self

    def __next__(self):
        if self._current < self._stop:
            result = self._current
            self._current += 1
            return result
        else:
            raise StopIteration

r = Iterator(0,3)
for e in r:
    print(e)