import unittest

from hamcrest import assert_that
from pytest import fail
from selenium import webdriver

from tests.constants import *
from tests.custom_matchers.has_number_of_elements_greater_than import has_number_of_elements_greater_than
from tests.page_objects.featured_dropdown_grid_category_page import FeaturedDropdownGridCategoryPage
from tests.page_objects.featured_file_filtering_page import FeaturedFileFilteringPage
from tests.page_objects.featured_nested_grid_page import FeaturedNestedGridPage


class Exercises(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(DEFAULT_WAIT_TIME)

    def test_exercise_1(self):
        # Exercise 1.
        # http://www.smartclient.com/smartgwt/showcase/#featured_tile_filtering

        page = FeaturedFileFilteringPage(self.driver)
        page.go_to_page_url()

        # Fill fields
        # 1.	Animal set using letter „a”

        page.send_keys_to_animal_input("a")

        # 2.	Max life span set to  40

        page.set_age_slider_to(40)

        # 3.	Sort order by „Life Span”

        page.select_sort_order(FeaturedFileFilteringPage.SORT_ORDER_OPTION_LIFE_SPAN)

        # 4.	Select checkbox  to Ascending

        page.tick_ascending_checkbox()

        # Assert that results contains more than 12 items

        assert_that(page, has_number_of_elements_greater_than(12, FeaturedFileFilteringPage.TILE_SORTED_HITS_LOCATOR))

    def test_exercise_2(self):
        # Exercise 2.
        # http://www.smartclient.com/smartgwt/showcase/#featured_dropdown_grid_category

        page = FeaturedDropdownGridCategoryPage(self.driver)
        page.go_to_page_url()

        # Select from dropdown row which will meet all criteria

        # 1.	Item contains „Exercise”

        item_criteria = lambda item: "Exercise" in item

        # 2.	Units contains  Ea

        units_criteia = lambda units: "Ea" in units

        # 3.	Unit Cost greater than 1.1

        unit_cost_criteria = lambda unit_cost: float(unit_cost) > 1.1
        criteria = {
            FeaturedDropdownGridCategoryPage.ITEM: item_criteria,
            FeaturedDropdownGridCategoryPage.UNITS: units_criteia,
            FeaturedDropdownGridCategoryPage.UNIT_COST: unit_cost_criteria
        }
        item_element = page.select_and_return_item_based_on_criteria(criteria)
        if item_element is None:
            fail("No item found with attributes")

    def test_exercise_3(self):
        # Exercise 3.
        # http://www.smartclient.com/smartgwt/showcase/#featured_nested_grid

        page = FeaturedNestedGridPage(self.driver)
        page.go_to_page_url()

        # for each item containing name „Correction” do following actions
        #   sub items change „Description” to incremental number starting from 1 and proceeding random 10 characters
        #   ex. 1 asdfasdfasdf, 2 asdasdasdas …

        page.change_sub_items_for_items_with_name_containing_correction()