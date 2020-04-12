import helpers
import containers
import controls

# Tag Factory Class
# This class is a factory for the different classes of html objects


class TagFactory:
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
        else:
            return helpers.Tags("default_" + tag, {})

    def ConvertTupleToDictionary(listAttributes):
        dictionary = {}
        for attribute in listAttributes:
            dictionary[attribute[0]] = attribute[1]
        return dictionary
