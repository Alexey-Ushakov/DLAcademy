# Метод перенес в продукты
import abc


class Tag(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def get_html(self):
        pass


class Image(Tag):
    def __init__(self, src):
        self.src = src

    def get_html(self):
        return "<></{}>".format(self.src)


class Input(Tag):
    def __init__(self, in_type):
        self.in_type = in_type

    def get_html(self):
        return "<></{}>".format(self.in_type)

class Text(Tag):
    def __init__(self, text):
        self.text = text

    def get_html(self):
        return "<></{}>".format(self.text)


class Link(Tag):
    def __init__(self, link):
        self.link = link

    def get_html(self):
        return "<></{}>".format(self.link)

class None_text(Tag):
    def __init__(self, none_text):
        self.none_text = none_text

    def get_html(self):
        return "<></{}>".format(self.none_text)

class Tagfactory:
    def create_tag(self, name):
        if name == 'image' or name == "src":
            return Image(name)
        elif name == 'input':
            return Input(name)
        elif name == 'a':
            return Link(name)
        elif name == 'p':
            return Text(name)
        elif name == '':
            return None_text(name)

factory = Tagfactory()
elements = ["image", "input", 'a', 'p', '', 'src']
for el in elements:
    print(factory.create_tag(el).get_html())
