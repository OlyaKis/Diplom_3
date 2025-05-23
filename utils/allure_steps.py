import allure


def step_with_screenshot(driver, description):
    with allure.step(description):
        allure.attach(driver.get_screenshot_as_png(), name="screenshot", attachment_type=allure.attachment_type.PNG)
