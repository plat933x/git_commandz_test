import time, pytest
from playwright.sync_api import Playwright, expect


@pytest.mark.parametrize("run", range(3))
@pytest.mark.flaky(reruns=3)
def test_create_an_account(run, playwright: Playwright) -> None:

    browser = playwright.chromium.launch(headless=True)
    context = browser.new_context()
    page = context.new_page()

    page.goto("https://candymapper.com/")
    # waiting for website to load correctly - avoiding 500's errors
    page.wait_for_load_state("domcontentloaded")

    page.locator("#popup-widget307423-close-icon").click()
    page.locator("[id=\"\\34 \"]").click()
    page.get_by_role("link", name="Create Account").click()

    page.get_by_role("textbox", name="First name").wait_for(state="visible", timeout=3000)
    first_name = page.get_by_role("textbox", name="First name")
    first_name.click()

    page.get_by_role("textbox", name="First name").type("John")

    last_name = page.get_by_role("textbox", name="Last name")
    last_name.click()

    page.get_by_role("textbox", name="Last name").type("Doe")

    email = (page.get_by_role("textbox", name="Email"))
    email.click()

    page.get_by_role("textbox", name="Email").type("john.doe@gmail.com")

    phone = (page.get_by_role("textbox", name="Phone (optional)"))
    phone.click()

    page.get_by_role("textbox", name="Phone (optional)").type("+48100200300")

    # page occasionaly gets reloaded by itself, to prevent error double check for first name added
    if first_name.input_value() == "":
        first_name.type("John")

    page.get_by_role("button", name="Create Account").click()

    check_your_email_announced = page.get_by_role("heading", name="Check your email")
    expect(check_your_email_announced).to_be_visible(timeout=15000)

    whole_page_content = page.content()
    # pytest logic saved with additional assert after playwrightish expect
    assert "Check your email" in whole_page_content, "Account was not created therefore proper content was not reached"

    context.close()
    browser.close()
