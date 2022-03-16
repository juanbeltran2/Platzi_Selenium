import unittest # Libreria para traer todas las pruebas
from pyunitreport import HTMLTestRunner # Orquestar cada prueba junto con los reportes
from selenium import webdriver # Comunicacion con el navegador

class HelloWorld(unittest.TestCase): 

    @classmethod # Permite que se ejecuten todas las pruebas en una sola ventana del navegador
    def setUpClass(cls): # Prepara el enorno de la prueba
        cls.driver = webdriver.Chrome(executable_path= r'C:/Platzi/Selenium/Driver/chromedriver.exe') # La ruta depende del SO
        driver = cls.driver
        driver.implicitly_wait(10) # Esperar 10 segundos antes de cada accion
        
    def test_hello_world(self): # Caso de prueba donde se realizan las acciones
        driver = self.driver
        driver.get('https://www.google.com')

    def test_visit_wikipedia(self): 
        driver = self.driver
        driver.get('https://es.wikipedia.org/')

    @classmethod
    def tearDownClass(cls): # Acciones que finalizan
        # Cerrar las ventanas cuando terminan las puebas
        cls.driver.quit()

if __name__ == "__main__":
	unittest.main(verbosity = 2, testRunner = HTMLTestRunner(output = 'reportes', report_name = 'hello-world-report-una-ventana'))