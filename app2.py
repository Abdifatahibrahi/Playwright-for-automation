from playwright.sync_api import sync_playwright

playwright = sync_playwright().start()
browser = playwright.chromium.launch(headless=False, slow_mo = 1000)
page = browser.new_page()
page.goto('https://playwright.dev/python/')
page.get_by_role('link', name='get started')
page.get_by_text()
page.get_by_alt_text()
page.get_by_title()
page.locator("css=h1").highlight()
page.locator("h1:text('Navbars')").highlight()
page.locator("h1:text-is('Navbars')").highlight() #pse-udo
page.locator("div.dropdown-menu:visible").highlight()
page.locator(":nth-match(button.btn-primary, 4)").highlight()
page.locator("xpath=//h1[@id='navbars']")
page.locator("//h1[text() = 'Head']")
page.get_by_role("button", name="primary").locator("nth=2").highlight()
page.locator("button").locator("nth=18").highlight()