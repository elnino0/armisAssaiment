import time
import unittest

from pageObjects.pages import MagicSeaWeedHome
from selenium.webdriver.common.by import By

from seleniumInfrasture.infrastructure import navigate, singleDriver


class MagicSeaWeedTests(unittest.TestCase):

    def setUp(self):
        singleDriver.getWedDriver().fullscreen_window()
        navigate.navigate("https://magicseaweed.com/Israel-Surf-Forecast/90/")

    def login(self):
        homepage = MagicSeaWeedHome()
        homepage.goTologin().login("aliranrubin@gmail.com","Teamo1986")
        navigate.assertNavigation("https://magicseaweed.com/Israel-Surf-Forecast/90/")

    def failLogin(self):
        homepage = MagicSeaWeedHome()
        homepage.goTologin().login("aliranrubin@gmail.com", "Teamo198")

    def test_startRegoin(self):
        homepage = MagicSeaWeedHome()
        homepage.goToForecasts().assertRegion("MIDDLE EAST").assertState("ISRAEL")

    def test_RecommendeSpots(self):
        homepage = MagicSeaWeedHome()
        homepage.goToForecasts().assertSpotsRecoomended(["HILTON", "MARINA - HERZELIA", "BEIT YANAI", "DOLPHINARIUM", "HOF MARAVI"])

    def test_worldWide(self):
        homepage = MagicSeaWeedHome()
        homepage.goToForecasts().assertWorldWide("EUROPE", ["AZORES" ,"BALTIC SEA","BULGARIA + ROMANIA","CANARY ISLANDS","CYPRUS","FRANCE","GERMANY + DENMARK","GREECE","ICELAND","ITALY","MALTA","NETHERLANDS + BELGIUM","NORWAY","RUSSIA","SPAIN + PORTUGAL","SWEDEN","TURKEY","UK + IRELAN"])

    def test_changeRegoin(self):
        homepage = MagicSeaWeedHome()
        forecasts = homepage.goToForecasts()
        forecasts.changeRegion("Africa")
        forecasts.changeState("South Africa")
        homepage.goToForecasts().assertSpotsRecoomended(["JEFFREYS BAY (J-BAY)", "MUIZENBERG", "CAPE TOWN", "DURBAN", "KOMMETJIE", "LLANDUDN"])

    def test_regoinalOverview(self):
        homepage = MagicSeaWeedHome()
        homepage.goToForecasts().assertregionalOverView(["ARGAMANS BEACH", "ASHDOD", "ASHQELON", "BACKDOOR HAIFA", "BAT YAM", "BEIT YANAI", "BETSET", "CAESAREA"])

    def test_searchArea(self):
        homepage = MagicSeaWeedHome()
        homepage.searchandSelect("ERICEIRA")
        homepage.assertSearchresultHeader("ERICEIRA SURF REPORT AND FORECAST")

    def test_changeAreaurl(self):
        homepage = MagicSeaWeedHome()
        homepage.goToForecasts().selectWorldWideRegion("EUROPE", "AZORES")
        time.sleep(3)
        navigate.assertNavigation("https://magicseaweed.com/Azores-Surf-Forecast/67/")

    def tearDown(self):
       singleDriver.CloseWedDriver()


if __name__ == '__main__':
    unittest.main()