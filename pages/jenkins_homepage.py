from selene import browser, have, be, command
import time

class JenkinsHomepage():

    def __init__(self):
        self.browser = browser

    def open(self):
        browser.open("/")
        time.sleep(2)
        return self

    def check_h1(self, value):
        time.sleep(2)
        browser.element("h1").should(be.visible).should(have.exact_text(value))
        return self

    def recent_posts_section(self, value):
        # recent posts section not visible
        recent_posts = browser.all(".app-card")
        recent_posts.should(have.size(9))
        time.sleep(1)
        recent_posts.should(be.not_.visible)
        # 4th post in recent posts section is visible after scroll to it
        (recent_posts[3]
            .perform(command.js.scroll_into_view)
            .should(be.visible)
            .should(have.text(value))
        )
        time.sleep(2)
        return self