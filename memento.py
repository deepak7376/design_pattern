'''
lets you save and restore previous state.
example  :Editor, cmd

mememto ---> prserve state
caretaker ---> save in stack and pop from stack
origanator ---> where the changes occurs
'''

class Memento(object):

    def __init__(self, state):
        self.state = state

    def setState(self, state):
        self.state = state
    
    def getState(self):
        return self.state


class Originator(object):
    def __init__(self, state):
        self.state = state

    def process(self, newValue):
        self.state = newValue

    def save(self):
       return Memento(self.state)

    def restore(self, mememto):
        self.state = mememto.getState()


class Caretaker(object):

    def __init__(self, originator):
        self.originator = originator
        self.mementos = []

    def backup(self):
        self.mementos.append(self.originator.save())


    def undo(self):

        memento = self.mementos.pop()
        self.originator.restore(memento)
        

origin = Originator(10)
care = Caretaker(origin)
care.backup()

origin.process(20)
care.backup()

origin.process(30)
care.backup()
care.undo()

origin.process(40)
care.backup()

origin.process(50)
care.backup()
care.undo()

origin.process(60)
care.backup()

print([m.getState() for m in care.mementos])