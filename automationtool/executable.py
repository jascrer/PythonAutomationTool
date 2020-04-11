from urllib.request import urlopen
from bs4 import BeautifulSoup

from htmlparser import MainParser
import helpers

url = 'http://tutorialspoint.com/python/python_overview.htm'
# Fetch the html file
response = urlopen(url)
html_doc = response.read()

# Parse the html file
soup = BeautifulSoup(html_doc, 'html.parser')

# Format the parsed html file
strhtm = soup.prettify()

# Test
div = helpers.Div()
div.setId("div_1")

button = helpers.Button()
button.setId("button_1")
div.addElement(button)

label = helpers.Label()
label.setId("label_1")
div.addElement(label)

inputSubmit = helpers.Input("submit")
inputSubmit.setId("input_submit_1")

html = helpers.HTML()
html.addElement(div)

# Execution
html.printContainer()

# Parser test
testHtml = '<html><div><button></button><label>Test!</label><input type=text></input></div><button></button></html>'
htmlParser = MainParser()
htmlParser.feed(testHtml)
htmlParser.getHtmlRoot().printContainer()
