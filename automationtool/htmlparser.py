from tagfactory import TagFactory
import helpers
from html.parser import HTMLParser


# List of ignored tags
IgnoredTags = ["script", "meta", "head", "title", "style", "link", "img"]
IgnoredModifiers = ["i", "b", "addr", "hr", "br"]

"""
Main Parser Class:
Class for parsing the html and create a tree of Tags object
"""


class MainParser(HTMLParser):

    """
    Initializes the parser
    """
    def __init__(self):
        HTMLParser.__init__(self)
        self.htmlRoot = None
        self.parserCursor = None

    """
    Handles the starting tag for a html object
    """
    def handle_starttag(self, tag, attrs):
        if self.htmlRoot and tag not in IgnoredTags + IgnoredModifiers:
            newTag = TagFactory.CreateTagObject(tag, attrs)
            if isinstance(newTag, helpers.Container):
                newTag.setParent(self.parserCursor)
                self.parserCursor.addElement(newTag)
                self.parserCursor = newTag
            else:
                self.parserCursor.addElement(newTag)
                newTag.setParent(self.parserCursor)
        else:
            if tag == "html":
                self.htmlRoot = TagFactory.CreateTagObject(tag, attrs)
                self.parserCursor = self.htmlRoot

    """
    Handles the data inside the tag for a html object
    """
    def handle_data(self, data):
        if self.parserCursor:
            lastIndex = self.parserCursor.getTagsLength() - 1
            if lastIndex >= 0:
                elementCursor = self.parserCursor.getElement(lastIndex)
                if elementCursor:
                    elementCursor.setData(data)

    """
    Handles the ending tag for a html object
    """
    def handle_endtag(self, tag):
        if self.parserCursor:
            if self.parserCursor.getTag() == tag:
                self.parserCursor = self.parserCursor.getParent()

    """
    Returns the root of the parsed tree
    """
    def getHtmlRoot(self):
        return self.htmlRoot
