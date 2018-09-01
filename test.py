import unittest
from selenium import webdriver

class NewVisitorTest(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Chrome()

    def tearDown(self):
        self.browser.quit()
        
        
    def test_starting_a_new_todo_list(self):
        self.browser.get('http://localhost:5000')
        self.assertIn('Django', self.browser.title)
        
if __name__ == '__main__':
    unittest.main()

