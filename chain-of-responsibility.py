'''
    Chain of responsibility Design Pattern
        type: Behavioral
'''

from abc import ABC, abstractmethod


class AbstractHandler(ABC):
    def __init__(self, alternative):
        self._alternative = alternative

    def handler(self, request):
        handled = self.request_processor(request)
        if not handled:
            self._alternative.handler(request)

    @abstractmethod
    def request_processor(self, request):
        pass

# ---------------------------------------------------


class FirstHandler(AbstractHandler):
    def request_processor(self, request):
        if 0 < request <= 30:
            print("First Handler, proccess on your request.")
            return True


class SeconeHandler(AbstractHandler):
    def request_processor(self, request):
        if 30 < request <= 60:
            print("Second Handler, proccess on your request.")
            return True


class DefaultHandler(AbstractHandler):
    def request_processor(self, request):
        print("There is no suitable handler for your request.")
        return True

# ---------------------------------------------------


class Client:
    def __init__(self):
        self.handler = FirstHandler(SeconeHandler(DefaultHandler(None)))

    def delegate(self, requests):
        for request in requests:
            self.handler.handler(request)

# ---------------------------------------------------


my_list = [7, 22, 45, 58, 77]

c1 = Client()
c1.delegate(my_list)
