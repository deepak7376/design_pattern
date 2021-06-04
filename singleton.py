# '''
# Only one object is created for the classs.
# '''


class _Tigger:

    def __str__(self):
        return "I'm the only one!"

    def roar(self):
        return 'Grrr!'

_instance = None

def Tigger():

    global _instance

    if _instance is None:
        _instance = _Tigger()
    
    return _instance


a = Tigger()
b = Tigger()
c = Tigger()

print(f'ID(a) = {id(a)}')
print(f'ID(b) = {id(b)}')
print(f'ID(c) = {id(c)}')
print(f'Are they the same object? {a is b is c}')