from pages.base_page import BasePage
from pages.search_page import SearchPage
from utils.locators import SearchLocator


def test_items_can_be_searched(driver):
    search_page = SearchPage(driver)
    base_page = BasePage(driver)
    search_page.type_on_search_field("Pablo Picasso")
    total_results = base_page.retrieve_text(*SearchLocator.NUMBER_OF_RESULTS)

    assert not total_results == "0 results"


def test_it_shows_0_when_item_not_found(driver):
    search_page = SearchPage(driver)
    base_page = BasePage(driver)
    search_page.type_on_search_field("skdfsldkjfls")
    total_results = base_page.retrieve_text(*SearchLocator.NUMBER_OF_RESULTS)

    assert total_results == "0 results"

