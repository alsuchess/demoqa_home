from pages.swag_labs import SwagLabs
from conftest import browser

def test_check_icon(browser):
    swaglabs = SwagLabs(browser)
    swaglabs.visit()
    assert swaglabs.exist_icon()

def test_check_name(browser):
    swaglabs = SwagLabs(browser)
    swaglabs.visit()
    assert swaglabs.exist_name()

def test_check_password(browser):
    swaglabs = SwagLabs(browser)
    swaglabs.visit()
    assert swaglabs.exist_password()
