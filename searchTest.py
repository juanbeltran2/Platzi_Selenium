from re import search
from unicodedata import name
import unittest # Libreria para traer todas las pruebas
from pyunitreport import HTMLTestRunner # Orquestar cada prueba junto con los reportes
from selenium import webdriver # Comunicacion con el navegador

class HomePageTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path= r'C:/Platzi/Selenium/Driver/chromedriver.exe') # La ruta depende del SO
        driver = self.driver
        driver.get('http://demo-store.seleniumacademy.com/')
        driver.maximize_window()
        driver.implicitly_wait(20) # Esperar 15 segundos antes de cada accion
    
    def test_search_text_field(self):
        # ubicar elemento por ID
        search_field = self.driver.find_element_by_id("search")
        

    def tearDown(self) :
        self.driver.quit()

if __name__ == "__main__":
	unittest.main(verbosity = 2)