class Singleton(object):
    obj = None
    def __new__(cls,*args, **kwargs):
        if cls.obj is None:
            cls.obj = object.__new__(cls,*args, **kwargs)
        return cls.obj


new_obj = Singleton()

obj1 = Singleton('MyInstance 1')
obj2 = Singleton('MyInstance 2')

print (obj1 is obj2)  # True