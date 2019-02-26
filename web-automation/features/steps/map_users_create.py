from behave import *

from pages.register_page import RegisterPage
from pages.main_page import MainPage


@given(u'I open the web app')
def step_impl(context):
	# global page is an instance of MainPage
	global page
	page = MainPage(context.browser)
	page.open('/')
	page.check_page_loaded()

@given(u'I restore the database')
def step_impl(context):
	pass

@given(u'I open the register page')
def step_impl(context):
	global page
	page.click_register_button()

	# global page is now an instance of RegisterPage
	page = RegisterPage(context.browser)


@then(u'I should ensure that all the empty fields give approprate warnings')
def step_impl(context):
  for row in context.table:
  	print(row)
  	username 	= row["username"]
  	email 		= row["email"]
  	birthday 	= row["birthday"]
  	address 	= row["address"]
  	warning 	= row["warning"]
  	page.enter_username(username)
  	page.enter_email(email)
  	page.enter_birthday(birthday)
  	page.enter_address(address)
  	page.submit_register_form()

  	assert warning in page.get_validation_message()
  	page.refresh_page()
  	page.click_register_button()


@when(u'I enter "{username}" for user name')
def step_impl(context, username):
  page.enter_username(username)


@when(u'I enter "{email}" for e-mail')
def step_impl(context, email):
	page.enter_email(email)


@when(u'I enter "{birthday}" for birthday')
def step_impl(context, birthday):
	page.enter_birthday(birthday)


@when(u'I enter "{address}" for address')
def step_impl(context, address):
	page.enter_address(address)


@when(u'I click on Register button')
def step_impl(context):
	page.submit_register_form()


@then(u'I should see the correct "{message}"')
def step_impl(context, message):
	assert message in page.get_message()

@when(u'I should see created users')
def step_impl(context):
    page.check_users(["testusername1", "testusername2"])

@when(u'I click "{username}" on users page')
def step_impl(context, username):
    page.click_user(username)

@then(u'I should see the detail of "{username}"')
def step_impl(context, username):
    page.check_user_info(username)