from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from base import Page
from locators import *
import users
from selenium.webdriver.support.ui import WebDriverWait




class MainPage(Page):
	def check_page_loaded(self)
		return True if self.find_element(*MainPageLocators.LOGO) 
		else False

	def search_item(self, item):
		self.find_element(*MainPageLocators.SEARCH).send_keys(item)
		self.find_element(*MainPageLocators.SEARCH).send_keys(Keys.ENTER)
		return self.find_element(*MainPageLocators.SEARCH_LIST).text

	def clk_signUp_btn(self):
		self.hover(*MainPageLocators.ACCOUNT)
		self.find_element(*MainPageLocators.SIGNUP).click()
		return signUpPage(self.driver)

	def clk_signIn_btn(self):
		self.hover(*MainPageLocators.ACCOUNT)
		self.find_element(*MainPageLocators.SIGNIN).click()
		return signInPage(self.driver)


class LoginPage(Page):
	def enter_email(self, user):
		self.find_element(*MainPageLocators.EMAIL).send_keys(users.get_user(user)["email"])

	def enter_password(self, user):
		self.find_element(*MainPageLocators.PASSWORD).send_keys(users.get_user(user)["password"])

	def clk_logIn_btn(self)
		self.find_element(*MainPageLocators.SUBMIT).click()

	def login(self, user):
		self.enter_email(user)
		self.enter_passord(user)
		self.click(clk_signIn_btn)

	def login_with_valid(self, user):	
		self.login(user)
		return HomePage(self.driver)

	def login_with_invalid(self, user);
		self.login(user)
		return find_element(*MainPageLocators.ERROR_MESSAGE).text


class HomePage(Page):
	pass


class SignUp(Page):
	pass
		









