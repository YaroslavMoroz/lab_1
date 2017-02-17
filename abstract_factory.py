class TopClass(object):
    def Bad_combination_combination(self):
        raise NotImplementedError()

    def Bad_combination(self):
        raise NotImplementedError()


class Good(object):
    def __init__(self, name):
        self._name = name

    def __str__(self):
        return self._name


class Bad(object):
    def __init__(self, name):
        self._name = name

    def __str__(self):
        return self._name


class TopClass1(TopClass):
    def Bad_combination_combination(self):
        return Good('High-card')

    def Bad_combination(self):
        return Bad('You lose')


class TopClass2(TopClass):
    def Bad_combination_combination(self):
        return Good('Royal Flush')

    def Bad_combination(self):
        return Bad('You Win!')


def get_factory(ident):
    if ident == 0:
        return TopClass1()
    elif ident == 1:
        return TopClass2()

factory = get_factory(1)
print (factory.Bad_combination_combination())
print (factory.Bad_combination())