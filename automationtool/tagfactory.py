import helpers
import containers
import controls

"""
TagFactory Class:
This class is a factory for the different classes of html objects
"""


class TagFactory:
    """
    Creates a Tag object based on the given html tag
    """
    def CreateTagObject(tag, attrs):
        attributes = TagFactory.ConvertTupleToDictionary(attrs)
        if tag == "html":
            return containers.HTML(attributes)
        elif tag == "div":
            return containers.Div(attributes)
        elif tag == "button":
            return controls.Button(attributes)
        elif tag == "label":
            return controls.Label(attributes)
        elif tag == "input":
            if "type" in attributes:
                type = attributes["type"]
                attributes.pop("type")
                return controls.Input(type, attributes)
            return controls.Input("text", attributes)
        elif tag == "header":
            return containers.Header(attributes)
        elif tag == "body":
            return containers.Body(attributes)
        elif tag == "iframe":
            return containers.Iframe(attributes)
        elif tag == "a":
            if "href" in attributes:
                href = attributes["href"]
                attributes.pop("href")
                return controls.HyperLink(href, attributes)
            return controls.HyperLink("", attributes)
        elif tag == "span":
            return containers.Span(attributes)
        elif tag == "ul":
            return containers.Ul(attributes)
        elif tag == "li":
            return containers.Li(attributes)
        elif tag == "footer":
            return containers.Footer(attributes)
        elif tag == "p":
            return containers.Parragraph(attributes)
        elif tag == "h1" or tag == "h2" or tag == "h3" or tag == "h4":
            return containers.Headers(tag, attributes)
        else:
            return helpers.Tags("default_" + tag, {})

    """
    Converts the tuple of attributes in a more convenient dictionary
    """
    def ConvertTupleToDictionary(listAttributes):
        dictionary = {}
        for attribute in listAttributes:
            dictionary[attribute[0]] = attribute[1]
        return dictionary
