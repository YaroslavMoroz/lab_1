class Name(object):
    def __init__(self, s):
        self._s = s

    def say(self):
        print ('His name is  %s' % self._s)


class profession(object):
    def __init__(self, man):
        self._man = man

    def __getattr__(self, item):
        return getattr(self._man, item)

    def fly(self):
        #Розширюєм функціональність об'єкта добавляючи професію
        print ('%s is a student' % self._man._s)


man = Name('Yarosalv')

man_profession = profession(man)
man_profession.say()
man_profession.fly()