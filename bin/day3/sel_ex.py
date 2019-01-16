from selenium import webdriver
from selenium.webdriver.common.keys import Keys

browser = webdriver.Chrome(r'C:\nitsmagic\lib\chromedriver.exe')
browser.get('https://google.com')
field = browser.find_element_by_name('q')
field.send_keys('python')
field.send_keys(Keys.RETURN)
browser.close()

import unittest


class MyTests(unittest.TestCase):

    def setUp(self):
        print('Inside setup')
        self.url = 'https://google.com'
        self.browser = webdriver.Chrome()

    def test_testcase_one(self):
        print('Inside Test Case I')
        self.browser.get(self.url)
        field = self.browser.find_element_by_name('q')
        field.send_keys('python')
        field.send_keys(Keys.RETURN)

    def test_testcase_two(self):
        print('Inside Test Case II')
        self.browser.get(self.url)
        field = self.browser.find_element_by_name('q')
        field.send_keys('java')
        field.send_keys(Keys.RETURN)

    def tearDown(self):
        print('Inside TearDown')
        self.browser.close()


if __name__ == '__main__':
    unittest.main()
