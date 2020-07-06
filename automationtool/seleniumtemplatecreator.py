from jinja2 import Environment, FileSystemLoader
import os

# Template location
TEMPLATES_PATH = os.path.join(os.path.dirname(__file__), 'templates')

"""
Class for creating and rendering the selenium class
"""


class SeleniumTemplateCreator:
    def __init__(self, browser, url):
        self.environment = Environment(
            loader=FileSystemLoader(TEMPLATES_PATH)
        )
        self.browser = browser
        self.url = url

    def setSeleniumTemplate(self):
        self.template = self.environment.get_template('seleniumtemplate.pt')

    def getSeleniumTemplate(self):
        return self.template

    def renderTemplate(self, testName, instructions, libraries):
        return self.template.render(
            testName=testName,
            browser=self.browser,
            url=self.url,
            instructions=instructions,
            libraries=libraries
        )
