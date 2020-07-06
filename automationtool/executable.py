from urllib.request import urlopen
from bs4 import BeautifulSoup

from htmlparser import MainParser
from routetablecreator import RouteTableCreator
import controls
import containers

from seleniumtemplatecreator import SeleniumTemplateCreator

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
testHtml = ('<html><div><button></button><label>Test!</label>' +
            '<input type=text></input></div><button></button></html>')
htmlParser = MainParser()
htmlParser.feed(testHtml)
htmlParser.getHtmlRoot().printContainer()
print("")

writer = open("tree.txt", "w")
htmlParser2 = MainParser()
htmlParser2.feed(html_doc.decode("utf-8"))
htmlParser2.getHtmlRoot().printerContainer(writer)
writer.close()

# Route Table test
routeTable = RouteTableCreator.createTable(htmlParser.getHtmlRoot())
for key, value in routeTable.items():
    print(key + " = " + value.getTag())

writer = open("routetable.txt", "w")
routeTable2 = RouteTableCreator.createTable(htmlParser2.getHtmlRoot())
for key, value in routeTable2.items():
    writer.write(key + " = " + value.getTag() + "\n")
writer.close()

# Test Seleniumtemplatecreator


creator = SeleniumTemplateCreator('Chrome', 'http://localhost')
creator.setSeleniumTemplate()
template = creator.renderTemplate('test_1', ['getinstruction'], [])
print(template)
