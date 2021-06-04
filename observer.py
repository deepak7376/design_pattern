
# Observer design pattern lets you define subscription mechanism to notify multiple observer whenever there is 
# a change in the objects.

# pub --- sub.



class Subject(object):

    def __init__(self):
        self.observers = []

    def attach(self, observer):
        self.observers.append(observer)

    def detach(self, observer):
        self.observers.remove(observer)

    def notify(self):

        for observer in self.observers:
            observer.update(self)


class Subject1(Subject):

    def __init__(self):
        super().__init__()
        self.state = None

    def setState(self, state):
        self.state = state
        self.notify()

    def getState(self):
        return self.state

class Subject2(Subject):

    def __init__(self):
        super().__init__()
        self.state = None

    def setState(self, state):
        self.state = state
        self.notify()

    def getState(self):
        return self.state

class Observer(object):

    def update(self, subject):
        raise NotImplementedError("this method must be implemented.")

class Observer1(Observer):

    def update(self, subject):
        print(f"ob1 notification recieved: {subject.state}")

class Observer2(Observer):

    def update(self, subject):
        print(f"ob2 notification recieved:{subject.state}")

class Observer3(Observer):

    def update(self, subject):
        print(f"ob3 notification recieved:{subject.state}")

class Observer4(Observer):

    def update(self, subject):
        print(f"ob4 notification recieved:{subject.state}")


class Observer5(Observer):

    def update(self, subject):
        print(f"ob5 notification recieved:{subject.state}")


if __name__ == "__main__":

    ob1 = Observer1()
    ob2 = Observer2()
    ob3 = Observer3()
    ob4 = Observer4()
    ob5 = Observer5()
    
    cricket = Subject1()
    politics = Subject2()


    cricket.attach(ob1)
    cricket.attach(ob3)
    cricket.attach(ob5)

    politics.attach(ob2)
    politics.attach(ob4)
    politics.attach(ob1)

    politics.detach(ob1)


    cricket.setState(100)
    politics.setState(50)

