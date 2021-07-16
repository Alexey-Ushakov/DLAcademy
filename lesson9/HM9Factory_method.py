# Очевидно что это не совсем абстратный метод а ммм функциональное программирование
import abc


class Tag(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def get_html(self):
        pass

class Image(Tag):
    def __init__(self, src=None):
        self.src = src


class Input(Tag):
    def __init__(self, in_type=None):
        self.in_type = in_type

class Text(Tag):
    def __init__(self, text=None):
        self.text = text

class Link(Tag):
    def __init__(self, link=None):
        self.link = link

class Tagfactory:
    def create_tag(self, name):
        if name == 'image':
            print("<img>")
        elif name == 'input':
            print("<input>")
        elif name == 'p':
            print("<p>")
        elif name == 'a':
            print("<a>")
        elif name == "":
            print("<Тут ничего нет>")


factory = Tagfactory()
elements = ["image", "input", "p", "a", ""]
for el in elements:
    factory.create_tag(el)
