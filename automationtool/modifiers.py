from helpers import Tags

# Metainformation tags
# Abbreviation tag class


class Abbreviation(Tags):
    def __init__(self, title, attrs):
        Tags.__init__(self, "abbr", attrs)
        self.title = title

# Address tag class


class Address(Tags):
    def __init__(self, attrs):
        Tags.__init__(self, "address", attrs)

# Italic tag class


class Italic(Tags):
    def __init__(self, attrs):
        Tags.__init__(self, "i", attrs)
