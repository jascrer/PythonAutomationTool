# from helpers import Tags
from helpers import Container

"""
RouteTableCreator Class:
Creates the route table for every action element in the html page
"""


class RouteTableCreator:
    def createTable(root):
        dictionary = {}
        for tag in root.getTags():
            if isinstance(tag, Container):
                dictionary =\
                    RouteTableCreator.createTableContainer(tag,
                                                           dictionary,
                                                           root.getTag() + ".")
            else:
                dictionary[root.getTag()+"."+tag.getTag()] = tag
        return dictionary

    def createTableContainer(container, dictionary, route):
        for tag in container.getTags():
            newRoute = route + container.getTag()
            if isinstance(tag, Container):
                dictionary =\
                    RouteTableCreator.createTableContainer(tag,
                                                           dictionary,
                                                           newRoute + ".")
            else:
                tempRoute = newRoute + "." + tag.getTag() + "_" + tag.getId()
                dictionary[tempRoute] = tag
        return dictionary
