from behave import *
from splinter import Browser
from django.core import management

def before_all(context):
    # PhantomJS is used there (headless browser - meaning we can execute tests in a command-line environment

    context.browser = Browser('firefox', headless=True)

def before_scenario(context, scenario):
    # Reset the database before each scenario
    # This means we can create, delete and edit objects within an
    # individual scenerio without these changes affecting our
    # other scenarios
    management.call_command('flush', verbosity=0, interactive=False)

def after_all(context):
    # Explicitly quits the browser, otherwise it won't once tests are done
    context.browser.quit()

