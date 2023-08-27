from playwright.sync_api import sync_playwright


# with sync_playwright() as playwright:
#     browser = playwright.chromium.launch(headless=False, slow_mo=2000)
#     page = browser.new_page()
#     page.goto("https://testpages.herokuapp.com/styled/alerts/alert-test.html")
#     alert = page.get_by_text("Show alert box")
#     alert.click()

#     browser.close()

# def on_dialog(dialog):
#     print("Dialog opened:", dialog)
#     dialog.accept()
#     # dialog.dismiss()

# with sync_playwright() as playwright:
#     browser = playwright.chromium.launch(headless=False, slow_mo=2000)
#     page = browser.new_page()
#     page.goto("https://testpages.herokuapp.com/styled/alerts/alert-test.html")

#     page.on("dialog", on_dialog)
#     alert_btn = page.get_by_text("Show confirm box")
#     alert_btn.click()

#     browser.close()



def on_dialog(dialog):
    print("Dialog opened:", dialog)
    dialog.accept("Playwright is cool")
    # dialog.dismiss()

with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False, slow_mo=2000)
    page = browser.new_page()
    page.goto("https://testpages.herokuapp.com/styled/alerts/alert-test.html")

    page.on("dialog", on_dialog)
    alert_btn = page.get_by_text("Show prompt box")
    alert_btn.click()

    browser.close()