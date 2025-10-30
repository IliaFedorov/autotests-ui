from playwright.sync_api import sync_playwright, expect
with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=True)
    page = browser.new_page()
    page.goto('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration')

# Pasting Email
    registration_email_input = page.get_by_test_id('registration-form-email-input').locator('input')
    registration_email_input.fill("user.name@gmail.com")

# Pasting Username
    registration_username_input = page.get_by_test_id('registration-form-username-input').locator('input')
    registration_username_input.fill("username")

# Pasting password
    registration_password_input = page.get_by_test_id('registration-form-password-input').locator('input')
    registration_password_input.fill("password")

# Clicking Registration button
    registration_button = page.get_by_test_id('registration-page-registration-button')
    registration_button.click()

# Checking header of Dashboard page presence and text
    registration_page_dashboard_header = page.get_by_test_id('dashboard-toolbar-title-text')
    expect(registration_page_dashboard_header).to_be_visible()
    expect(registration_page_dashboard_header).to_have_text("Dashboard")
