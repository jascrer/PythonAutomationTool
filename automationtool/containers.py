from helpers import Tags
from helpers import Container

# HTML tag class


class HTML(Tags, Container):
    def __init__(self, attrs):
        Tags.__init__(self, "html", attrs)
        Container.__init__(self)

    def printContainer(self):
        print(self.getPrintableTag())
        self.printChildren()

    def printerContainer(self, printer):
        printer.write("\n" + self.getPrintableTag())
        self.printerChildren(printer)

# Div tag class


class Div(Tags, Container):
    def __init__(self, attrs):
        Tags.__init__(self, "div", attrs)
        Container.__init__(self)

# Header tag class


class Header(Tags, Container):
    def __init__(self, attrs):
        Tags.__init__(self, "header", attrs)
        Container.__init__(self)

# Body tag class


class Body(Tags, Container):
    def __init__(self, attrs):
        Tags.__init__(self, "body", attrs)
        Container.__init__(self)

# iFrame tag class


class Iframe(Tags, Container):
    def __init__(self, attrs):
        Tags.__init__(self, "iframe", attrs)
        Container.__init__(self)
        self.src = None

# Span tag class


class Span(Tags, Container):
    def __init__(self, attrs):
        Tags.__init__(self, "span", attrs)
        Container.__init__(self)

# Ul tag class


class Ul(Tags, Container):
    def __init__(self, attrs):
        Tags.__init__(self, "ul", attrs)
        Container.__init__(self)

# Li tag class


class Li(Tags, Container):
    def __init__(self, attrs):
        Tags.__init__(self, "li", attrs)
        Container.__init__(self)

# Footer tag class


class Footer(Tags, Container):
    def __init__(self, attrs):
        Tags.__init__(self, "footer", attrs)
        Container.__init__(self)

# Parragraph tag class


class Parragraph(Tags, Container):
    def __init__(self, attrs):
        Tags.__init__(self, "p", attrs)
        Container.__init__(self)

# Headers tag class


class Headers(Tags, Container):
    def __init__(self, tag, attrs):
        Tags.__init__(self, tag, attrs)
        Container.__init__(self)
