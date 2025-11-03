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
        menu_item.element_by(have.text(value)).click()
        browser.should(have.url_containing("book/getting-started/"))
        
        return self

    def left_menu_check_article(self, article_name, article_text):
        browser.element("h1").should(be.visible).should(have.text(article_name))
        article_text_elements = browser.all(".section .paragraph p")
        article_text_elements[0].should(have.text(article_text))

        return self