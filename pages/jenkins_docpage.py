from selene import browser, have, be, command
import time

class JenkinsDocpage():

    def __init__(self):
        self.browser = browser

    def open(self):
        browser.open("/doc")
        time.sleep(2)
        return self

    def check_h1(self, value):
        browser.element("h1").should(be.visible).should(have.text(value))
        time.sleep(2)
        return self

    def left_menu_click(self, value):
        menu_item = browser.all("#sidebar-content > ul > li")
        menu_item.element_by(have.exact_text(value)).click()
        time.sleep(2)
        browser.element("h1").should(be.visible).should(have.text("User Handbook Overview"))
        browser.should(have.url_containing("book/getting-started/"))
        time.sleep(1)
        return self