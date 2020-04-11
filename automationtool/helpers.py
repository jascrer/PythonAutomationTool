# Base classes
class Tags:
    def __init__(self, tag):
        self.tag = tag
        self.id = ""
        self.data = None

    def getData(self):
        return self.data

    def setData(self, data):
        self.data = data

    def getTag(self):
        return self.tag

    def getId(self):
        return self.id

    def setId(self, id):
        self.id = id

    def getPrintableTag(self):
        if len(self.id) == 0:
            return self.tag
        return self.tag + " id=" + self.id

# Container


class Container:
    def __init__(self):
        self.tags = []
        self.parent = None

    def addElement(self, element):
        self.tags.append(element)

    def getTags(self):
        return self.tags

    def getTagsLength(self):
        return len(self.tags)

    def getElement(self, index):
        return self.tags[index]

    def getParent(self):
        return self.parent

    def setParent(self, parent):
        self.parent = parent

    def printContainer(self, tabs):
        print()

    def printChildren(self):
        self.printChildrenTags(1)

    def printChildrenTags(self, tabs):
        tabChars = "    " * tabs
        for tag in self.tags:
            if(isinstance(tag, Container)):
                tag.printContainer((tabs))
            elif(isinstance(tag, Tags)):
                print(tabChars + "|->" + tag.getPrintableTag())

# HTML


class HTML(Tags, Container):
    def __init__(self):
        Tags.__init__(self, "html")
        Container.__init__(self)

    def printContainer(self):
        print(self.getPrintableTag())
        self.printChildren()

# Div


class Div(Tags, Container):
    def __init__(self):
        Tags.__init__(self, "div")
        Container.__init__(self)

    def printContainer(self, tabs):
        tabChars = "    " * tabs
        print(tabChars + "|->" + self.getPrintableTag())
        self.printChildrenTags(tabs + 1)

# Controls
# Button


class Button(Tags):
    def __init__(self):
        Tags.__init__(self, "button")

# Label


class Label(Tags):
    def __init__(self):
        Tags.__init__(self, "label")

# Input


class Input(Tags):
    def __init__(self, type):
        Tags.__init__(self, "input")
        self.type = type

    def getType(self):
        return self.type

    def getPrintableTag(self):
        return Tags.getPrintableTag(self) + " type=" + self.type

# Tag Factory Class


class TagFactory:
    def CreateTagObject(tag, attrs):
        if tag == "html":
            return HTML()
        elif tag == "div":
            return Div()
        elif tag == "button":
            return Button()
        elif tag == "label":
            return Label()
        elif tag == "input":
            return Input("text")
