from urllib.request import urlopen
from bs4 import BeautifulSoup

from htmlparser import MainParser
import controls
import containers

url = 'http://tutorialspoint.com/python/python_overview.htm'
# Fetch the html file
response = urlopen(url)
html_doc = response.read()

# Parse the html file
soup = BeautifulSoup(html_doc, 'html.parser')

# Format the parsed html file
strhtm = soup.prettify()

# Test
div = containers.Div({})
div.setId("div_1")

button = controls.Button({})
button.setId("button_1")
div.addElement(button)

label = controls.Label({})
label.setId("label_1")
div.addElement(label)

inputSubmit = controls.Input("submit", {})
inputSubmit.setId("input_submit_1")

html = containers.HTML({})
html.addElement(div)

# Execution
# html.printContainer()

# Parser test
testHtml = '<html><div><button></button><label>Test!</label><input type=text></input></div><button></button></html>'
htmlParser = MainParser()
htmlParser.feed(testHtml)
htmlParser.getHtmlRoot().printContainer()

writer = open("tree.txt", "w")
htmlParser2 = MainParser()
htmlParser2.feed(html_doc.decode("utf-8"))
htmlParser2.getHtmlRoot().printerContainer(writer)
writer.close()
