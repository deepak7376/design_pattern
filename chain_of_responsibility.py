'''
This design pattern lets you pass yours request along chain of handllers.
Staff---> Supervisor ---> Director
Authentication --> auth --> rate limit --> data sanitization --> caching --> db
'''

class Handler(object):

    def __init__(self):
        self.sucessor = None

    def handle(self, request):
        raise NotImplementedError("This method must be implemented.")

    def makeSucessor(self, sucessor):
        self.sucessor = sucessor


class Staff(Handler):
    def handle(self, request):
        if request == "L1":
            print("Handle by Staff")
            # do some action       
        elif self.sucessor:
            self.sucessor.handle(request)

class Supervisor(Handler):
    def handle(self, request):
        if request == "L2":
            print("Handle by Supervisor")
            # do some action       
        elif self.sucessor:
            self.sucessor.handle(request)

class Director(Handler):
    def handle(self, request):
        if request == "L3":
            print("Handle by Director")
            # do some action       
        elif self.sucessor:
            self.sucessor.handle(request)
            

s1 = Staff()
sup1 = Supervisor()
d1 = Director()

s1.makeSucessor(sup1)
sup1.makeSucessor(d1)
d1.makeSucessor(None)

request = "L3"
s1.handle(request)