from playwright.sync_api import sync_playwright
from time import perf_counter

# with sync_playwright() as playwright:
#     browser = playwright.chromium.launch(headless=False, slow_mo=1000)
#     page = browser.new_page()
#     page.goto('https://www.scrapethissite.com/pages/ajax-javascript/')
#     link = page.get_by_role('link', name='2015')
#     link.click()

#     print('2015 loading....')
#     start = perf_counter()
#     spotlight = page.locator('td.film-title').first
#     spotlight.wait_for()
    
#     time_taken = perf_counter() - start

#     print(f"... loaded with {round(time_taken, 2)} seconds")

def on_load(page):
    print("Page loaded:", page)
with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False, slow_mo=1000)
    page = browser.new_page()

    page.on("domcontentloaded", on_load)
    page.goto("https://bootswatch.com/default")

    browser.close()