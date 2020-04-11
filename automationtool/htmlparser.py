import helpers
from html.parser import HTMLParser


class MainParser(HTMLParser):
    def __init__(self):
        HTMLParser.__init__(self)
        self.htmlRoot = None
        self.parserCursor = None

    def handle_starttag(self, tag, attrs):
        if self.htmlRoot:
            newTag = helpers.TagFactory.CreateTagObject(tag, attrs)
            if isinstance(newTag, helpers.Container):
                newTag.setParent(self.parserCursor)
                self.parserCursor.addElement(newTag)
                self.parserCursor = newTag
            else:
                self.parserCursor.addElement(newTag)
        else:
            if tag == "html":
                self.htmlRoot = helpers.TagFactory.CreateTagObject(tag, attrs)
                self.parserCursor = self.htmlRoot

    def handle_data(self, data):
        if self.parserCursor:
            lastIndex = self.parserCursor.getTagsLength() - 1
            self.parserCursor.getElement(lastIndex).setData(data)

    def handle_endtag(self, tag):
        if self.parserCursor:
            if self.parserCursor.getTag() == tag:
                self.parserCursor = self.parserCursor.getParent()

    def getHtmlRoot(self):
        return self.htmlRoot
