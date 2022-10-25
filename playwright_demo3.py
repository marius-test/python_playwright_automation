# npx playwright codegen https://the-internet.herokuapp.com/login
# the code below is demonstrated using Playwright Inspector

from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()

    page = context.new_page()

    page.goto("https://the-internet.herokuapp.com/login")

    page.get_by_label("Username").click()

    page.get_by_label("Username").fill("tomsmith")

    page.get_by_label("Username").press("Tab")

    page.get_by_label("Password").fill("SuperSecretPassword!")

    page.get_by_label("Password").press("Enter")
    page.wait_for_url("https://the-internet.herokuapp.com/secure")
    
    page.screenshot(path='screenshot.png')

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
