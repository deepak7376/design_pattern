'''
It is a behavioural design pattern that enables selecting an algorithm at run-time. Adding a new strategy or algorithm should not
affect the existing pattern.

Eg. different algorithms of sorting
'''

class Context(object):

    def __init__(self):
        self.strategy = None

    def getStrategy(self):
        return self.strategy

    def setStrategy(self, obj):
        self.strategy = obj

    def execute(self):
        self.strategy.algo()


class Strategy(object):

    def algo(self):
        raise NotImplementedError(" This method must be implemented ")


class Strategy1(Strategy):

    def algo(self):
        print(" this is algo 1")


class Strategy2(Strategy):

    def algo(self):
        print(" this is algo 2")


if __name__ == "__main__":

    context = Context()
    s1 = Strategy1()
    s2 = Strategy2()
    context.setStrategy(s2)
    context.execute()



