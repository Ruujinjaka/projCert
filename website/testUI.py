import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

 
class EdurekaOrg(unittest.TestCase):
  
    def setUp(self):
        self.driver = webdriver.Firefox();
 
    def test_search_title(self):
        driver = self.driver
        driver.get("http://34.67.113.188:30753/")
        title = driver.find_element(By.TAG_NAME, "h2")
 
        # Looking for the string "simple" in the heading
        self.assertIn("Simple", title.text)
 
 
    def test_search_heading(self):
        driver = self.driver
        driver.get("http://34.67.113.188:30753/")
        heading = driver.find_element(By.TAG_NAME, "h3")
        self.assertIn("Home", heading.text)
 
    def test_about_page(self):
        driver = self.driver
        driver.get("http://34.67.113.188:30753/")
        driver.find_element(By.ID, "About Us").click()
        about = driver.find_element(By.TAG_NAME, "b")
        self.assertIn("about", about.text)
 
 
    def test_product_page(self):
        driver = self.driver
        driver.get("http://34.67.113.188:30753/")
        driver.find_element(By.ID, "Products").click()
        product = driver.find_element(By.TAG_NAME, "b")
        self.assertIn("product", product.text)
 
 
    def test_contact_page(self):
        driver = self.driver
        driver.get("http://34.67.113.188:30753/")
        driver.find_element(By.ID, "Contact").click()
        contact  = driver.find_element(By.TAG_NAME, "b")
        self.assertIn("contact", contact.text)
 
 
    def tearDown(self):
        self.driver.close()
 
if __name__ == "__main__":
    unittest.main();
