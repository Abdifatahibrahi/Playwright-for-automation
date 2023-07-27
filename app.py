from playwright.sync_api import sync_playwright

with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False, slow_mo=1000)
    page = browser.new_page()
    page.goto('https://playwright.dev/python/')
    docs_btn = page.get_by_role('link', name = 'Get started')
    docs_btn.click()