import pytest
import allure

from selene import browser
from selene.support.shared import config
from selenium import webdriver

def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome",
                     help="Browser: chrome or firefox")
    parser.addoption("--headless", action="store_true",
                     help="Run in headless mode")

# add browser info to allure report
@pytest.hookimpl(tryfirst=True)
def pytest_runtest_setup(item):
    browser = item.config.getoption("--browser")
    allure.dynamic.tag(browser)

@pytest.fixture(scope='session', autouse=True)
def browser_management(request):
    browser_name = request.config.getoption("--browser")
    headless = request.config.getoption("--headless")

    drivers = {
        "chrome": (
            webdriver.ChromeOptions,
            "chrome",
            lambda options: (
                options.add_argument("--headless=new"),
                options.add_argument("--disable-gpu"),
            ),
        ),
        "firefox": (
            webdriver.FirefoxOptions,
            "firefox",
            lambda options: (
                options.add_argument("--headless"),
                options.add_argument("--disable-gpu"),
            ),
        ),
    }

    if browser_name not in drivers:
        raise ValueError(f"Browser '{browser_name}' is not supported!")

    options_class, selene_browser_name, headless_setup = drivers[browser_name]
    options = options_class()

    if headless:
        headless_setup(options)

    # Selene config
    config.browser_name = selene_browser_name
    config.base_url = "https://www.jenkins.io/"
    config.window_width = 1300
    config.window_height = 900
    config.driver_options = options
    config.timeout = 4.0

    browser.open("/")
    yield

    if browser_name == "chrome":
        log_text = "".join(f'{text}\n' for text in browser.driver.get_log(log_type='browser'))
        allure.attach(
                      log_text,
                      name = 'Web Browser logs',
                      attachment_type=allure.attachment_type.TEXT,
                      extension='.log',
                      )
    
    html = browser.driver.page_source
    allure.attach(
                  html,
                  name = 'Page Source',
                  attachment_type=allure.attachment_type.HTML,
                  extension='.html')
    
    browser.quit()
