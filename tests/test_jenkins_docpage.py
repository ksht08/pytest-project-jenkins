import time
import allure
from selene import browser
from pages.jenkins_docpage import JenkinsDocpage

@allure.title("Test Jenkins docpage")
def test_jenkins_docpage():

    jenkins_doc_page = JenkinsDocpage()

    with allure.step("Open Jenkins docpage"):
        jenkins_doc_page.open()

    with allure.step("Check H1 header"):
        jenkins_doc_page.check_h1("Jenkins User Documentation")
        allure.attach(
            browser.driver.get_screenshot_as_png(),
            name="h1 header",
            attachment_type=allure.attachment_type.PNG,
        )

    with allure.step("Check recent posts section"):
        jenkins_doc_page.left_menu_click("User Handbook Overview")
        
    time.sleep(1)