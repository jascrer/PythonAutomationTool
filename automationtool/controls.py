from helpers import Tags

# Controls
# Button tag class


class Button(Tags):
    def __init__(self, attrs):
        Tags.__init__(self, "button", attrs)

# Label tag class


class Label(Tags):
    def __init__(self, attrs):
        Tags.__init__(self, "label", attrs)

# Input tag class


class Input(Tags):
    def __init__(self, type, attrs):
        Tags.__init__(self, "input", attrs)
        self.type = type

    def getType(self):
        return self.type

    def getPrintableTag(self):
        return Tags.getPrintableTag(self) + " type=" + self.type

# Hyperlink tag class


class HyperLink(Tags):
    def __init__(self, href, attrs):
        Tags.__init__(self, "a", attrs)
        self.href = href

    def getPrintableTag(self):
        attributes = " href=" + self.href
        if self.data:
            attributes = attributes + " data=" + self.data
        return Tags.getPrintableTag(self) + attributes

# TextArea tag class


class TextArea(Tags):
    def __init__(self, attrs):
        Tags.__init__(self, "textarea", attrs)
