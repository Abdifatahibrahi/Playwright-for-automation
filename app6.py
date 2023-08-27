# from playwright.sync_api import sync_playwright


# def on_download(download):
#     print("download received...")
#     download.save_as('mountain.png')


# with sync_playwright() as playwright:
#     browser = playwright.chromium.launch(headless=False, slow_mo=1000)
#     page = browser.new_page()
#     page.goto("https://unsplash.com/photos/a-large-rock-formation-with-a-sky-background-0dqqcem_lWI")

#     btn = page.get_by_text('Download free')
#     page.on("download", on_download)
#     with page.expect_download() as mountain_download:
#         btn.click()

    # download = mountain_download.value
    # download.save_as("mountain.jpg")

    # browser.close()


from playwright.async_api import async_playwright
import asyncio


async def main():
    async with async_playwright() as playwright:
        browser = await playwright.chromium.launch(headless=False, slow_mo=1000)
        page = await browser.new_page()
        await page.goto("https://playwright.dev/python/")
        print(await page.title())
        await browser.close()

asyncio.run(main())