import unittest
from selenium import webdriver
from pages import *
from testCases import test_cases
from locators import *
from selenium.webdriver.common.by import By


class TestPages(unittest.testCases):
	
	def setup(self):
		self.driver = webdriver.Chrome()
		self.driver.get('http://amazon.com')

	def page_loaded(self):
		print "\n" + str(test_cases(0))
		page = MainPage(self.driver)
		self.assertTrue(check_page_loaded())