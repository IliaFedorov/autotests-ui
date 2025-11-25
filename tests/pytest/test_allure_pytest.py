import allure

@allure.step("Opening browser")
def open_browser():
    with allure.step("Get browser"):
        ...
    with allure.step("Start browser"):
        ...



@allure.step("creating course")
def create_course2(title: str):
    with allure.step(f"Creating course with title '{title}'"):
        ...

@allure.step("Creating course with title '{title}'")
def create_course(title: str):
    ...


@allure.step("closing browser")
def close_browser():
    ...

def test_feature2():
    with allure.step("Opening browser"):
        ...

    with allure.step("creating course"):
        ...

    with allure.step("closing browser"):
        ...

def test_featureu():
    open_browser()

    create_course(title='Locust')
    create_course(title='Pytest')
    create_course(title='Python')
    create_course(title='Playwright')


    close_browser()