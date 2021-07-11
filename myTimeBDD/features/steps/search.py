from behave import *
import time


use_step_matcher('parse')


@given(u'The user has landed on consumers page')
def step_user_landed_on_consumers_page(context):
    assert(context.commonOperations.open_url('https://www.mytime.com/consumers'))
    assert(context.commonOperations.url_as_expected('https://www.mytime.com/consumers'))


@given(u'sees the consumer page elements')
def step_sees_consumer_page_elements(context):
    assert (context.commonOperations.xpath_element_exists_with_attribute('//*[@id="global_container"]/div[5]/div[3]/h1',
                                                                         'innerHTML',
                                                                         'Book appointments<br class="visible-xs"> for anything',
                                                                         False))
    assert (context.commonOperations.get_xpath_element_or_none('//*[@id="search-query"]') is not None)
    assert (context.commonOperations.get_xpath_element_or_none('//*[@id="search-location"]') is not None)
    assert (context.commonOperations.get_xpath_element_or_none('//*[@id="search-form"]/div[1]/div[3]/button') is not
            None)
    assert (context.commonOperations.get_xpath_element_and_click('//*[@id="accept-cookies-and-close-button"]'))
    assert (context.commonOperations.get_xpath_element_and_click('//*[@id="global_container"]/div[5]/div[2]/h1'))


@given(u'The user enters "{query}" in query field on consumer default search tile')
def step_user_enters_query_field_on_consumer_default_search_tile(context, query):
    assert(context.commonOperations.get_xpath_element_and_select_all_delete('/html/body/div[3]/div[5]/div[2]/div[2]/div[1]/form/div[1]/div[1]/input'))
    assert(context.commonOperations.get_xpath_element_and_send_keys('/html/body/div[3]/div[5]/div[2]/div[2]/div[1]/form/div[1]/div[1]/input', query))


@ given(u'user selects item# "{item_number}" in query dropdown on consumer default search tile')
def step_user_selects_query_field_dropdown_on_consumer_default_search_tile(context, item_number):
    assert (context.commonOperations.get_xpath_element_and_click('/html/body/ul[2]/li['+item_number+']'))


@given(u'user enters "{location}" in location field on consumer default search tile')
def step_user_enters_location_field_on_consumer_default_search_tile(context, location):
    assert (context.commonOperations.get_xpath_element_and_select_all_delete('/html/body/div[3]/div[5]/div[2]/div[2]/div[1]/form/div[1]/div[2]/input'))
    assert(context.commonOperations.get_xpath_element_and_send_keys('/html/body/div[3]/div[5]/div[2]/div[2]/div[1]/form/div[1]/div[2]/input', location))


@given(u'user selects item# "{item_number}" in location dropdown on consumer default search tile')
def step_user_selects_location_field_dropdown_on_consumer_default_search_tile(context, item_number):
    assert(context.commonOperations.get_xpath_element_and_click('/html/body/ul[5]/li['+item_number+']'));


@when(u'user clicks on Search on consumer default search tile')
def step_user_clicks_search_on_consumer_default_search_tile(context):
    assert(context.commonOperations.get_xpath_element_and_click('/html/body/div[3]/div[5]/div[2]/div[2]/div[1]/form/div[1]/div[3]/button'))


@then(u'user lands on the search results page')
def step_user_lands_on_search_results_page(context):
    assert(context.commonOperations.url_starts_with('https://www.mytime.com/search'))


@then(u'user sees "{count}" search results on search results page')
def step_user_sees_results_on_search_results_page(context, count):
    for i in range(1, int(count)):
        assert(context.commonOperations.get_xpath_element_or_none('/html/body/div[3]/div[4]/div[3]/div[2]/div[2]/div[2]/div/div/div[1]/ul/li['+i.__str__()+']') is not None)


@given(u'User is on search results page for "{query}" and "{location}"')
def step_user_on_search_results_page_for_a_search(context, query, location):
    assert(context.commonOperations.get_xpath_element_and_click('/html/body/div[3]/div[4]/div[3]/div[2]/div[1]/div[1]/div[1]/div/form/div[1]/div[1]/div[1]/div/div/div[2]'))
    assert(context.commonOperations.xpath_element_exists_with_attribute('/html/body/div[3]/div[4]/div[3]/div[2]/div[1]/div[1]/div[1]/div/form/div[1]/div[1]/div[2]/div/div[1]/div/div/input', 'value', query, True))
    assert (context.commonOperations.xpath_element_exists_with_attribute('/html/body/div[3]/div[4]/div[3]/div[2]/div[1]/div[1]/div[1]/div/form/div[1]/div[1]/div[2]/div/div[2]/div/div/input', 'value', location, True))


@given(u'user clicks on the search result "{business}" on search result page')
def step_user_chooses_business_on_search_result_page(context, business):
    list_elements = context.commonOperations.get_xpath_elements_or_none('/html/body/div[3]/div[4]/div[3]/div[2]/div[2]/div[2]/div/div/div[1]/ul/li')
    element_to_click = None
    for list_element in list_elements:
        if business in context.commonOperations.get_element_attribute(list_element, 'innerHTML').__str__():
            element_to_click = list_element
            break
    assert(element_to_click is not None)
    if element_to_click:
        assert (context.commonOperations.click_or_fail(element_to_click))
    context.business = business


@Given(u'user sees express checkout page')
def step_user_sees_express_checkout_page(context):
    assert (context.commonOperations.url_starts_with('https://www.mytime.com/express_checkout'))


@When(u'user clicks on "{service}" on services panel on express checkout page')
def step_user_chooses_service_in_service_panel_on_express_checkout_page(context, service):
    list_elements = context.commonOperations.get_xpath_elements_or_none('/html/body/div[1]/div/div/div[2]/div/section/aside/div/section[2]/fieldset/label/span')
    element_to_click = None
    for list_element in list_elements:
        if service.__str__().strip() == context.commonOperations.get_element_attribute(list_element, 'innerHTML').__str__().strip():
            element_to_click = list_element
            break
    assert (element_to_click is not None)
    if element_to_click:
        assert (context.commonOperations.click_or_fail(element_to_click))


@When(u'user selects staff# "{staff_number}" from staff filter on express checkout page')
def step_user_selects_staff_item_from_staff_filter_on_express_checkout_page(context, staff_number):
    list_elements = context.commonOperations.get_xpath_elements_or_none('/html/body/div[1]/div/div/div[2]/div/section/aside/div/section[3]/fieldset/label')
    element_to_click = None
    counter = 1
    for list_element in list_elements:
        if counter == int(staff_number):
            element_to_click = context.commonOperations.get_nested_xpath_element_or_none(list_element, './/span')
            break
        counter += 1
    if element_to_click:
        context.service_staff_name = context.commonOperations.get_element_attribute(element_to_click, 'innerText')
        assert(context.commonOperations.click_or_fail(element_to_click))


@When(u'user clicks Book button for "{service}" service on express checkout page')
def step_user_clicks_book_button_for_service_on_express_checkout_page(context, service):
    context.service = 'Men\'s Haircut'
    list_elements = context.commonOperations.get_xpath_elements_or_none(
        '/html/body/div[1]/div/div/div[2]/div/section/main/section/div/div')
    booking_div_to_check = None
    staff_div_to_check = None
    for list_element in list_elements:
        if context.service in context.commonOperations.get_element_attribute(list_element, 'innerHTML').__str__():
            booking_div_to_check = list_element
        if context.service_staff_name in context.commonOperations.get_element_attribute(list_element, 'innerHTML').__str__():
            staff_div_to_check = list_element
    assert (booking_div_to_check is not None)
    context.session = {"service_price": booking_div_to_check.find_element_by_xpath('.//div/div[1]/div/div/span[2]/span').get_attribute('innerText').__str__(),
                       "service_name": booking_div_to_check.find_element_by_xpath('.//div/div[1]/h5/span').get_attribute('innerText').__str__(),
                       "service_staff_name": staff_div_to_check.find_element_by_xpath('.//fieldset/div/div/div/span[1]/div[1]/span').get_attribute('innerText').__str__()}

    #Click the “Book” button for the “Men's Haircut” service
    assert(context.commonOperations.get_xpath_element_and_click('//button[@aria-label="Book Service Men\'s Haircut"]'))


@When(u'user clicks selects time on add-on modal on express checkout page')
def step_user_clicks_selects_time_on_add_on_modal_on_express_checkout_page(context):
    #Press "Select Time" in the add-on modal opened
    assert(context.commonOperations.get_xpath_element_and_click('/html/body/div[1]/div/div/div[2]/div/section/main/div[2]/div/div[3]/div/div[2]/div[2]/button'))

@Then(u'user lands on pick a time section on express checkout page')
def step_user_lands_on_pick_a_time_section_on_express_checkout_page(context):
    assert (context.commonOperations.xpath_element_exists_with_attribute('/html/body/div[1]/div/div/div[2]/div/section/main/h2', 'innerText', 'Pick a Time', False))


@Then(u'user sees the previously selected service, staff and price on time section on express checkout page')
def step_user_sees_the_previously_selected_service_staff_and_price_on_time_section_on_express_checkout_page(context):
    #Verify that the user is presented with a list of available time slots with at least 2 entries
    go_to_next_element = context.commonOperations.get_xpath_element_or_none('//button[@data-automation="timePage.goToNextAvailableDate"]')
    if go_to_next_element is None:
        list_elements = context.commonOperations.get_xpath_elements_or_none('/html/body/div[1]/div/div/div[2]/div/section/main/div[2]/div')
        assert(len(list_elements) >= 2)
    else:
        go_to_next_element.click()
        local_counter = 0
        list_elements = context.commonOperations.get_xpath_elements_or_none(
            '/html/body/div[1]/div/div/div[2]/div/section/main/div[2]/div')
        while len(list_elements) < 2:
            time.sleep(1)
            local_counter += 1
            if local_counter > 5 :
                break
            list_elements = context.commonOperations.get_xpath_elements_or_none(
                '/html/body/div[1]/div/div/div[2]/div/section/main/div[2]/div')
        assert (len(list_elements) >= 2)

    #Verify in the right side panel
    #Service displayed is the one selected in the step before
    assert(context.commonOperations.xpath_element_exists_with_attribute('/html/body/div[1]/div/div/div[2]/div/section/aside/div/div/section[1]/ul/li/div[1]/span', 'innerText', context.session['service_name'], False))

    #Service price is the same as the one displayed in the step before
    assert (context.commonOperations.xpath_element_exists_with_attribute('/html/body/div[1]/div/div/div[2]/div/section/aside/div/div/section[1]/ul/li/div[2]/span/span', 'innerText', context.session['service_price'], False))

    #Staff selected is the staff chosen before
    assert (context.commonOperations.xpath_element_exists_with_attribute('/html/body/div[1]/div/div/div[2]/div/section/aside/div/div/section[2]/div/table/tbody/tr[1]/td[2]/span/div/div/span[1]/div[1]/span', 'innerText', context.session['service_staff_name'], False))
