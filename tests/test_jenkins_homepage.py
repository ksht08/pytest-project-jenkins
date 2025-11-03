import time
import allure
from selene import browser
from pages.jenkins_homepage import JenkinsHomepage

@allure.title("Test Jenkins homepage")
def test_jenkins_homepage():

    jenkins_home_page = JenkinsHomepage()

    with allure.step("Open Jenkins homepage"):
        jenkins_home_page.open()

    with allure.step("Check H1 header"):
        jenkins_home_page.check_h1("Jenkins")
        allure.attach(
            browser.driver.get_screenshot_as_png(),
            name="h1 header",
            attachment_type=allure.attachment_type.PNG,
        )

    with allure.step("Check recent posts section"):
        jenkins_home_page.recent_posts_section("Revamped Tests UI in Jenkins")
        allure.attach(
            browser.driver.get_screenshot_as_png(),
            name="recent posts section",
            attachment_type=allure.attachment_type.PNG,
        )
    