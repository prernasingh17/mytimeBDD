import time

from selenium.common.exceptions import ElementNotInteractableException
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CommonOperations(object):

    def __init__(self, driver: WebDriver):
        super(CommonOperations, self).__init__()
        self._driver: WebDriver = driver

    def get_xpath_element_or_none(self, element_xpath):
        element = None
        try:
            element: WebElement = self._driver.find_element_by_xpath(element_xpath)
            return element
        except:
            print('fail: failed with exception while retrieving the element with XPath = ' + element_xpath)
            return element

    def get_nested_xpath_element_or_none(self, parent_element: WebElement, element_xpath):
        element = None
        try:
            element: WebElement = parent_element.find_element_by_xpath(element_xpath)
            return element
        except:
            print('fail: failed with exception while retrieving the element with XPath = ' + element_xpath)
            return element

    def get_xpath_elements_or_none(self, element_xpath):
        elements = None
        try:
            elements: [WebElement] = self._driver.find_elements_by_xpath(element_xpath)
            return elements
        except:
            print('fail: failed with exception while retrieving the element with XPath = ' + element_xpath)
            return elements


    def get_xpath_element_with_wait_or_none(self, element_xpath):
        element = None
        try:
            element: WebElement = WebDriverWait(self._driver, 10).until(EC.visibility_of_element_located((By.XPATH, element_xpath)))
            return element
        except:
            print('fail: failed with exception while retrieving the element with XPath = ' + element_xpath)
            return None

    def get_id_element_or_none(self, element_id):
        element = None
        try:
            element: WebElement = self._driver.find_element_by_id(element_id)
            return element
        except:
            print('fail: failed with exception while retrieving the element with ID = ' + element_id)
            return None

    def get_name_element_or_none(self, element_name):
        element = None
        try:
            element: WebElement = self._driver.find_element_by_name(element_name)
            return element
        except:
            print('fail: failed with exception while retrieving the element with Name = ' + element_name)
            return None

    def get_css_selector_element_or_none(self, element_css_selector):
        element = None
        try:
            element: WebElement = self._driver.find_element_by_css_selector(element_css_selector)
            return element
        except:
            print('fail: failed with exception while retrieving the element with CSS Selector = ' + element_css_selector)
            return None

    def click_or_fail(self, element: WebElement):
        if element:
            element.click()
            return True
        else:
            print('fail: could not click a None element')
            return False

    def click_with_javascript_or_fail(self, element: WebElement):
        """This function tries to click the element via javascript because webdriver is unable to click the element

        Parameters:
        element (WebElement): The element which needs to be clicked via javascript

        Returns:
        bool:Whether the function was able to click the element or faced an error while doing so

       """
        if element:
            self._driver.execute_script("arguments[0].click();", element)
            return True
        else:
            print('fail: could not click a None element')
            return False

    def send_keys_or_fail(self, element: WebElement, keys_to_be_sent):
        if element:
            try:
                element.send_keys(keys_to_be_sent)
                return True
            except ElementNotInteractableException as e:
                try:
                    ActionChains(self._driver).move_to_element(element).send_keys(keys_to_be_sent).perform()
                    return True
                except Exception as e:
                    print('fail: could not send keys to the element')
                    print(e.__str__())
                    try:
                        self._driver.execute_script("arguments[0].scrollIntoView(true);", element);
                        element.click()
                        return True
                    except Exception as ee:
                        print(ee.__str__())
                        return False
        else:
            print('fail: could not send keys to a None element')
            return

    def select_all_delete_or_fail(self, element: WebElement):
        if element:
            try:
                element.send_keys(Keys.CONTROL, "a", Keys.DELETE)
                return True
            except ElementNotInteractableException as e:
                try:
                    ActionChains(self._driver).move_to_element(element).send_keys(Keys.CONTROL, "a", Keys.DELETE).perform()
                    return True
                except Exception as e:
                    print('fail: could not send keys to the element')
                    print(e.__str__())
                    try:
                        self._driver.execute_script("arguments[0].scrollIntoView(true);", element);
                        element.send_keys(Keys.CONTROL, "a", Keys.DELETE)
                        return True
                    except Exception as ee:
                        print(ee.__str__())
                        return False
        else:
            print('fail: could not send keys to a None element')
            return False

    def element_has_text(self, element: WebElement, element_text):
        if element:
            if element.text == element_text:
                return True
            else:
                print('fail: element does not have the mentioned text')
                return False
        else:
            print('fail: could not find text in a None element')
            return False

    def element_has_attribute_with_value_ignore_case(self, element: WebElement, attribute, value, ignore_case: bool):
        if element:
            if element.get_attribute(attribute).__str__().strip() == value.__str__().strip() or \
                    (ignore_case and element.get_attribute(attribute).__str__().lower().strip() == value.__str__().lower().strip()):
                return True
            else:
                print('fail: element does not have the mentioned attribute with the value provided')
                print(element.get_attribute(attribute))
                print(value)
                return False
        else:
            print('fail: could not find attribute in a None element')
            return False

    def get_element_attribute(self, element: WebElement, attribute):
        if element:
            return element.get_attribute(attribute).__str__().strip()
        else:
            print('fail: could not find attribute in a None element')
            return None

    def get_xpath_element_and_click(self, element_xpath):
        element: WebElement = self.get_xpath_element_or_none(element_xpath)
        return self.click_or_fail(element)

    def get_xpath_element_and_click_with_javascript(self, element_xpath):
        element: WebElement = self.get_xpath_element_with_wait_or_none(element_xpath)
        return self.click_with_javascript_or_fail(element)

    def xpath_element_exists_with_text(self, element_xpath, element_text):
        element: WebElement = self.get_xpath_element_or_none(element_xpath)
        return self.element_has_text(element, element_text)

    def xpath_element_exists_with_attribute(self, element_xpath, attribute, value, ignore_case: bool):
        element: WebElement = self.get_xpath_element_or_none(element_xpath)
        return self.element_has_attribute_with_value_ignore_case(element, attribute, value, ignore_case)

    def get_xpath_element_attribute(self, element_xpath, attribute):
        element: WebElement = self.get_xpath_element_or_none(element_xpath)
        return self.get_element_attribute(element, attribute)

    def nested_xpath_element_exists_with_attribute(self, element_xpath, parent_element: WebElement, attribute, value, ignore_case: bool):
        element: WebElement = self.get_nested_xpath_element_or_none(parent_element, element_xpath)
        return self.element_has_attribute_with_value_ignore_case(element, attribute, value, ignore_case)

    def get_nested_xpath_element_attribute(self, element_xpath, parent_element: WebElement, attribute):
        element: WebElement = self.get_nested_xpath_element_or_none(parent_element, element_xpath)
        return self.get_element_attribute(element, attribute)

    def get_xpath_element_and_send_keys(self, element_id, keys_to_be_sent):
        element: WebElement = self.get_xpath_element_or_none(element_id)
        return self.send_keys_or_fail(element, keys_to_be_sent)

    def get_xpath_element_and_select_all_delete(self, element_id):
        element: WebElement = self.get_xpath_element_or_none(element_id)
        return self.select_all_delete_or_fail(element)

    def get_name_element_and_send_keys(self, element_name, keys_to_be_sent):
        element: WebElement = self.get_name_element_or_none(element_name)
        return self.send_keys_or_fail(element, keys_to_be_sent)

    def url_as_expected(self, expected_url):
        if expected_url == self._driver.current_url:
            return True
        else:
            WebDriverWait(self._driver, 10).until(EC.url_changes(self._driver.current_url))
            if expected_url == self._driver.current_url:
                return True
            else:
                return False

    def url_starts_with(self, expected_url):
        if self._driver.current_url.__str__().startswith(expected_url):
            return True
        else:
            WebDriverWait(self._driver, 10).until(EC.url_changes(self._driver.current_url))
            if self._driver.current_url.__str__().startswith(expected_url):
                return True
            else:
                return False

    def open_url(self, url):
        try:
            self._driver.get(url)
            return True
        except:
            return False
