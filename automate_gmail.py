from playwright.sync_api import sync_playwright
with sync_playwright() as playwright:
    browser = playwright.firefox.launch(headless=False, slow_mo=500)
    context = browser.new_context(
        storage_state = "playwright/.auth/storage_state.json"
    )
    page = context.new_page()
    page.goto('https://accounts.google.com/')

    # email = page.get_by_label('Email or phone')
    # email.fill('alsidiq099@gmail.com')
    # next_btn = page.get_by_text('Next')
    # next_btn.click()

    page.pause()

    # Save the authentication state

    # context.storage_state(path="playwright/.auth/storage_state.json")
    context.close()






    # try_btn = page.get_by_text('Try another way')
    # try_btn.click()

    # email = page.get_by_label('Email or phone')
    # email.fill('alsidiq099@gmail.com')
    # next_btn = page.get_by_text('Next')
    # next_btn.click()