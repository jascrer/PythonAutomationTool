# Base classes
# Tag class: base class for all html objects


class Tags:
    def __init__(self, tag, attrs):
        self.tag = tag
        self.id = ""
        self.data = None
        self.attrs = attrs
        self.parent = None

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

    def getAttributes(self):
        return self.attrs

    def setAttributes(self, attrs):
        self.attrs = attrs

    def getParent(self):
        return self.parent

    def setParent(self, parent):
        self.parent = parent

    def getPrintableTag(self):
        if len(self.id) == 0:
            return self.tag + self.getPrintableAttributes()
        return self.tag + " id=" + self.id + self.getPrintableAttributes()

    def getPrintableAttributes(self):
        attributes = ""
        for attr, value in self.attrs.items():
            attributes = attributes + " " + attr + "=" + value
        return attributes

# Container class: for all html objects that can contain html objets


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
        if len(self.tags) == 0:
            return None
        return self.tags[index]

    def getParent(self):
        return self.parent

    def setParent(self, parent):
        self.parent = parent

    def printContainer(self, tabs):
        tabChars = "    " * tabs
        print(tabChars + "|->" + self.getPrintableTag())
        self.printChildrenTags(tabs + 1)

    def printerContainer(self, printer, tabs):
        tabChars = "    " * tabs
        printer.write("\n" + tabChars + "|->" + self.getPrintableTag())
        self.printerChildrenTags(printer, tabs + 1)

    def printChildren(self):
        self.printChildrenTags(1)

    def printerChildren(self, printer):
        self.printerChildrenTags(printer, 1)

    def printChildrenTags(self, tabs):
        tabChars = "    " * tabs
        for tag in self.tags:
            if(isinstance(tag, Container)):
                tag.printContainer(tabs)
            elif(isinstance(tag, Tags)):
                print(tabChars + "|->" + tag.getPrintableTag())

    def printerChildrenTags(self, printer, tabs):
        tabChars = "    " * tabs
        for tag in self.tags:
            if(isinstance(tag, Container)):
                tag.printerContainer(printer, tabs)
            elif(isinstance(tag, Tags)):
                printer.write("\n" + tabChars + "|->" + tag.getPrintableTag())
