from abc import ABC, abstractmethod


# -------------------------------SENDER------------------------------------
class ISender(ABC):
    @staticmethod
    @abstractmethod
    def format(protocol, sender):
        pass


class MySender(ISender):
    @staticmethod
    def format(protocol, sender):
        if protocol == 'IM':
            return ''.join(["I'm ", sender])
        return sender


# --------------------------------------------------------------------------


# -------------------------------RECEIVER------------------------------------
class IReceiver(ABC):
    @staticmethod
    @abstractmethod
    def format(protocol, receiver):
        pass


class MyReceiver(IReceiver):
    @staticmethod
    def format(protocol, receiver):
        if protocol == 'IM':
            return ''.join(["I'm ", receiver])
        return receiver


# --------------------------------------------------------------------------


# -------------------------------CONTENT------------------------------------
class IContent(ABC):
    def __init__(self, text):
        self.text = text

    @abstractmethod
    def format(self):
        pass


class MyContent(IContent):

    def format(self):
        return ''.join(['<myML>', self.text, '</myML>'])


# --------------------------------------------------------------------------

class IEmail(ABC):
    @abstractmethod
    def set_sender(self, sender):
        pass

    @abstractmethod
    def set_receiver(self, receiver):
        pass


class Email(IEmail):

    def __init__(self, protocol):
        self.protocol = protocol
        self.__sender = None
        self.__receiver = None
        self.__content = None

    def set_sender(self, receiver):
        self.__sender = MySender.format(self.protocol, receiver)

    def set_receiver(self, receiver):
        self.__receiver = MyReceiver.format(self.protocol, receiver)

    def set_content(self, content):
        self.__content = content.format()

    def __repr__(self):
        template = "Sender: {sender}\nReceiver: {receiver}\nContent:\n{content}"

        return template.format(sender=self.__sender, receiver=self.__receiver, content=self.__content)


# Official Test
email = Email('IM')
email.set_sender('qmal')
email.set_receiver('james')
content = MyContent('Hello, there!')
email.set_content(content)
print(email)

print()
print()

# Random Test
email = Email('GO')
email.set_sender('qmal')
email.set_receiver('james')
content = MyContent('Hello, there!')
email.set_content(content)
print(email)
