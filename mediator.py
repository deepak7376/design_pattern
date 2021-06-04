'''
Mediator design pattern restrict direct communication between objects. reduce chaotic dependancies between objects.
ATC (Air traffic controller)
'''

class Mediator(object):
    def __init__(self):
        self.colleagues = []

    def addColleague(self, colleagueObj):
        self.colleagues.append(colleagueObj)

    def sendMessage(self, originator, message):

        for colleague in self.colleagues:
            if colleague != originator:

                colleague.receiveMessage(message)


class Colleague(object):

    def __init__(self, mediator):
        self.mediator = mediator

    def sendMessage(self, message):
        self.mediator.sendMessage(self, message)

    def receiveMessage(self, message):
        print(f"message recived from mediator: {message}")


m = Mediator()
c1 = Colleague(m)
m.addColleague(c1)

c2 = Colleague(m)
m.addColleague(c2)

c3 = Colleague(m)
m.addColleague(c3)

c4 = Colleague(m)
m.addColleague(c4)

c5 = Colleague(m)
m.addColleague(c5)

c2.sendMessage(100)
