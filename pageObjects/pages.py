import time

from seleniumInfrasture.infrastructure import ElemetSuppleyer
from webItems.elementWarrper import elementWarpper
from selenium.webdriver.common.by import By


class basePage(elementWarpper):

    def __init__(self, selector, id):
        super().__init__(selector, id)

class MagicSeaWeedHome(basePage):

    def __init__(self):
        super().__init__(By.XPATH, "/html/body")
        self.searchBox = elementWarpper(By.XPATH, "//*[@id='msw-js-headerPrimary']/div[2]/div/div/div[2]/div/span/input[2]", 10)

    def searchandSelect(self, text):
        self.searchBox.setText(text)
        self.searchBox.click()
        time.sleep(3)
        items = ElemetSuppleyer.getElements(By.XPATH,"//*[@id='msw-js-headerPrimary']/div[2]/div/div/div[2]/div/span/span/div/span/div/a/strong")
        for item in items:
            if item.text in text:
                item.click()
                return

    def assertSearchresultHeader(self, header):
        headerElement = elementWarpper(By.XPATH, "//*[@id='msw-js-headerPrimary']/div[6]/div/div[2]/div[1]/div/header/div[2]/h1", 10)
        assert  headerElement.getText() == header

    def goTologin(self):
        self.loginButton = elementWarpper(By.XPATH, "//*[@id='msw-js-headerPrimary']/div[2]/div/div/div[3]/div/h5/a", 10)
        self.loginButton.click()
        return loginPage()

    def goToWebcams(self):
        webcamsTab = elementWarpper(By.XPATH, "//*[@id='msw-js-primaryBurgerContainer']/div[1]/div/div/div[2]", 10)
        webcamsTab.click()
        return Webcams()

    def goToForecasts(self):
        ForecastTab = elementWarpper(By.XPATH, "//*[@id='msw-js-primaryBurgerContainer']/div[1]/div/div/div[1]/a", 10)
        ForecastTab.click()
        time.sleep(5)
        return Forecast()

    def goToCharts(self):
        ChartsTab = elementWarpper(By.XPATH, "//*[@id='msw-js-primaryBurgerContainer']/div[1]/div/div/div[3]", 10)
        ChartsTab.click()
        return Charts()

    def goToFeatures(self):
        FeaturesTab = elementWarpper(By.XPATH, "//*[@id='msw-js-primaryBurgerContainer']/div[1]/div/div/div[4]", 10)
        FeaturesTab.click()
        return Features()

    def goToPhotos(self):
        PhotosTab = elementWarpper(By.XPATH, "//*[@id='msw-js-primaryBurgerContainer']/div[1]/div/div/div[5]", 10)
        PhotosTab.click()
        return Features()

    def goToLiveData(self):
        LiveDataTab = elementWarpper(By.XPATH, "//*[@id='msw-js-primaryBurgerContainer']/div[1]/div/div/div[6]", 10)
        LiveDataTab.click()
        return LiveData()

    def goToStore(self):
        StoreTab = elementWarpper(By.XPATH, "//*[@id='msw-js-primaryBurgerContainer']/div[1]/div/div/div[7]", 10)
        StoreTab.click()
        return Features()


class loginPage(basePage):

    def __init__(self):
        super().__init__(By.XPATH, "/html/body/div[1]")
        self.usernameTextBox = elementWarpper(By.XPATH, "//*[@id='msw-js-user-login-tab']/form/div[2]/input", 10)
        self.passwordTextBox = elementWarpper(By.XPATH,"//*[@id='msw-js-user-login-tab']/form/div[3]/input", 10)
        self.loginButton = elementWarpper(By.XPATH, "//*[@id='msw-js-login']", 10)

    def login(self, userName, password):
        self.usernameTextBox.setText(userName)
        self.passwordTextBox.setText(password)
        self.loginButton.click()


class Forecast(basePage):

    def __init__(self):
        super().__init__(By.XPATH, "//*[@id='msw-js-primaryBurgerContainer']/div[2]/div/div[1]/div/div[1]")
        self.spotsRecoomended = self.findChildrenByClass("div/div[1]/div[2]/div/ul/li/a/div")
        self.spotsRegoinal = self.findChildrenByClass("li[1]/a")
        self.selectedRegion = self.findChildByClass("div[@id='msw-js-forecasts-regions']/div[1]/div[1]/div/a/span")
        self.selectedState = self.findChildByClass("div[@id='msw-js-forecasts-regions']/div[1]/div[2]/div/a/span")
        self.selectRegionButton = self.findChildByClass("div[@id='msw-js-forecasts-regions']/div[1]/div[1]/div/a/span[2]")
        self.selectStateButton = self.findChildByClass("div[@id='msw-js-forecasts-regions']/div[1]/div[2]/div/a/span[2]")
        self.regionalOverView = self.findChildrenByClass("div[@data-type='list']")[0]
        self.worldwide = self.findChildrenByClass("div[@data-type='list']")[1]

    def assertSpotsRecoomended (self, listOfSpots=[]):
        for spot in self.spotsRecoomended:
            assert spot.getText() in listOfSpots

    def assertSpotsRegoinal (self, listOfSpots=[]):
        for spot in self.spotsRegoinal:
            assert spot.text in listOfSpots

    def assertregionalOverView(self, listOfSpots=[]):
        regionalOverViewItems = self.regionalOverView.findChildrenByClass("*[@id='msw-js-c60']/li/a")
        for spot in regionalOverViewItems:
            assert spot.text in listOfSpots

    def selectWorldWideRegion (self, continent, area):

        continentList = self.worldwide.findChildrenByClass("*[@id='msw-js-forecasts-continents']/div/h4/a")
        spotsIncontinent = []
        for spot in continentList:
            if spot.getText() == continent:
                spot.click()
                spotsIncontinent = spot.findChildrenByClass("*[@id='msw-js-forecasts-continents']/div[1]/ul/li/a")

        for spot in spotsIncontinent:
            if spot.getText() == area:
                spot.click()
                return

    def assertWorldWide (self, continent, listOfSpots=[]):

        continentList = self.worldwide.findChildrenByClass("*[@id='msw-js-forecasts-continents']/div[1]/h4/a")
        spotsIncontinent = []
        for spot in continentList:
            if spot.getText() == continent:
                spot.click()
                spotsIncontinent = spot.findChildrenByClass("*[@id='msw-js-c159']/li/a")

        for spot in spotsIncontinent:
            assert spot.text in listOfSpots

    def changeRegion(self, region):
        self.selectRegionButton = self.findChildByClass("div[@id='msw-js-forecasts-regions']/div[1]/div[1]/div/a/span[2]")
        self.selectRegionButton.addEventOnClick(self._onSelectedRegion)
        self.selectRegionButton.click(region)

    def changeState(self, state):
        self.selectStateButton = self.findChildByClass("div[@id='msw-js-forecasts-regions']/div[1]/div[2]/div/a/span[2]")
        self.selectStateButton.addEventOnClick(self._onSelectedState)
        self.selectStateButton.click(state)


    def _onSelectedRegion(self, selectedItem):
        size = len(self.findChildrenByClass("*[@id='select2-drop']/ul/li/div"))
        for index in range(size):
            try:
                if self.findChildrenByClass("*[@id='select2-drop']/ul/li/div")[index].getText() == selectedItem:
                    self.findChildrenByClass("*[@id='select2-drop']/ul/li/div")[index].click()
            except IndexError:
                pass

    def _onSelectedState(self, selectedItem):
        size = len(self.findChildrenByClass("*[@id='select2-drop']/ul/li/div"))
        for index in range(size):
            try:
                if self.findChildrenByClass("*[@id='select2-drop']/ul/li/div")[index].getText() == selectedItem:
                    self.findChildrenByClass("*[@id='select2-drop']/ul/li/div")[index].click()
            except IndexError:
                pass

    def assertRegion(self, region):
        assert self.selectedRegion.getText() == region
        return self

    def assertState(self, state):
        assert self.selectedState.getText() == state
        return self


class Store(basePage):
    def __init__(self):
        pass
class LiveData(basePage):
    def __init__(self):
        pass

class Webcams(basePage):
    def __init__(self):
        pass
class Photos(basePage):

    def __init__(self):
        pass

class Charts(basePage):

    def __init__(self):
        pass

class Features(basePage):

    def __init__(self):
        pass