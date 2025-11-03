from selene import browser, have, be

class JenkinsDocpage():

    def __init__(self):
        self.browser = browser

    def open(self):
        browser.open("/doc")

        return self

    def check_h1(self, value):
        browser.element("h1").should(be.visible).should(have.text(value))

        return self

    def left_menu_click(self, value):
        menu_item = browser.all("#sidebar-content > ul > li")
        menu_item.element_by(have.exact_text(value)).click()
        browser.should(have.url_containing("book/getting-started/"))
        browser.element("h1").should(be.visible).should(have.text(value))
        
        return self
