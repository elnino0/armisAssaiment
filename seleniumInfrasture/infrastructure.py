from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException, StaleElementReferenceException


class singleDriver():
    driver = webdriver.Chrome()

    @staticmethod
    def getWedDriver():
        return singleDriver.driver

    @staticmethod
    def CloseWedDriver():
        return singleDriver.driver.close()

class navigate():

    @staticmethod
    def navigate(urlPath):
        singleDriver.getWedDriver().get(urlPath)

    @staticmethod
    def assertNavigation(urlPath):
        assert urlPath in singleDriver.getWedDriver().current_url


class ElemetSuppleyer():

    @staticmethod
    def getElement(findbyEnum, id, delay=3):
        return WebDriverWait(singleDriver.driver, delay).until(EC.visibility_of(singleDriver.getWedDriver().find_element(findbyEnum, id)))

    @staticmethod
    def getElements(findbyEnum, id, delay=3):
        elements = singleDriver.getWedDriver().find_elements(findbyEnum, id)
        return elements

    @staticmethod
    def getChildrenByClassElements(webElement, cls, ECMethod=None, delay=3):
        elements = webElement.find_elements_by_xpath("//" + cls)
        if ECMethod is not None:
            for element in elements:
                 WebDriverWait(singleDriver.driver, delay).until(ECMethod(element))
        return elements

    @staticmethod
    def getChildByClassElements(webElement, cls, delay=3):
        return WebDriverWait(singleDriver.driver, delay).until(
            EC.visibility_of(webElement.find_element_by_xpath("//" + cls)))



