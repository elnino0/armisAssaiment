from selenium.webdriver.support.wait import WebDriverWait

from seleniumInfrasture.infrastructure import ElemetSuppleyer, singleDriver
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC

class elementWarpper(object):

    def __init__(self, enumSelector, id, delay=10):
        self._observers = []
        self.id = id
        self.enumSelector = enumSelector
        if id is not None and enumSelector is not None:
            self._webElement = ElemetSuppleyer.getElement(enumSelector, id, delay)

    def findChildren(self):
       return self._webElement.find_elements_by_xpath(".//*")

    def findChildrenByClass(self, cls, delay=10):
         webElements = ElemetSuppleyer.getChildrenByClassElements(webElement= self._webElement, cls=cls, delay=delay)
         listOfelements = []
         for e in webElements:
            element = elementWarpper(None, None)
            element._webElement = e
            listOfelements.append(element)

         return listOfelements


    def addEventOnClick(self, event):
        self._observers.append(event)

    def findChildByClass(self, cls, delay=10):
        element = elementWarpper(None, None)
        element._webElement = ElemetSuppleyer.getChildByClassElements(webElement= self._webElement, cls=cls, delay=delay)
        return element

    def setText(self, text):
        self._webElement.send_keys(text)

    def getText(self):
        return self._webElement.text

    def clickOnParent(self):
        self._webElement.find_elements_by_xpath("..").click()

    def click(self, args=None):
        self._webElement.click()
        for callback in self._observers:
            callback(args)
            self._observers.remove(callback)

    def refreshitem(self):
        if self.id is not None and self.enumSelector is not None:
            self._webElement = ElemetSuppleyer.getElement(findbyEnum=self.enumSelector, id=self.id, delay=10)


    def expilcitClick(self):
        webdriver.ActionChains(singleDriver.getWedDriver()).move_to_element_with_offset(self._webElement, 25, 9).click(self._webElement).perform()



