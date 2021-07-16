# Без асбстрактного метода? О_о и без наследования
class Image():
    def __init__(self, src=None):
        self.src = src


class Input():
    def __init__(self, in_type=None):
        self.in_type = in_type


class Text():
    def __init__(self, text=None):
        self.text = text



class Link():
    def __init__(self, link=None):
        self.link = link



class Tagfactory:
    def create_tag(self, name):
        if name == 'image' or name == "src":
            return "img"
        elif name == 'input':
            return "input"
        elif name == 'p':
            return "p"
        elif name == 'a':
            return "a"
        elif name == "":
            return ""

    def get_html(self, name):
        print("<></{}>".format(name))



factory = Tagfactory()
elements = ["image", "input", 'p', 'a', '']
for el in elements:
    factory.get_html(factory.create_tag(el))
