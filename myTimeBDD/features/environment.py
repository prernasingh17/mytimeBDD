from selenium import webdriver
from configparser import ConfigParser
from common.common import CommonOperations


def before_all(context):
    config = ConfigParser()
    config.read('./setup.cfg')
    browser = config.get('Environment', 'Browser')
    if browser == 'Edge':
        context.driver = webdriver.Edge()
    elif browser == 'Chrome':
        context.driver = webdriver.Chrome()
    context.driver.implicitly_wait(10)  # implicit wait
    context.commonOperations = CommonOperations(context.driver)


def after_all(context):
    context.driver.quit()