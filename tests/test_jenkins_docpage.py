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

    with allure.step("Open 'User Handbook Overview' article from left menu"):
        jenkins_doc_page.left_menu_click("User Handbook Overview")
        allure.attach(
            browser.driver.get_screenshot_as_png(),
            name="User Handbook Overview article",
            attachment_type=allure.attachment_type.PNG,
        )
        
    with allure.step("Check 'User Handbook Overview' article"):
        jenkins_doc_page.left_menu_check_article(
            "User Handbook Overview",
            "This page provides an overview of the documentation in the Jenkins User Handbook."
            )
        allure.attach(
            browser.driver.get_screenshot_as_png(),
            name="User Handbook Overview article text",
            attachment_type=allure.attachment_type.PNG,
        )
