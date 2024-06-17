import asyncio
from pyppeteer import launch

async def main():
    browser = await launch(headless=True)
    page = await browser.newPage()
    await page.goto('https://www.example.com')
    title = await page.title()
    print(title)
    await browser.close()

asyncio.get_event_loop().run_until_complete(main())
