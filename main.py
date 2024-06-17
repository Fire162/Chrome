import asyncio
from pyppeteer import launch

async def main():
    browser = await launch(headless=True)
    page = await browser.newPage()
    await page.goto('https://www.yescoin.gold/#tgWebAppData=user%3D%257B%2522id%2522%253A6723624511%252C%2522first_name%2522%253A%2522%25C3%2597%25CD%259C%25C3%2597%2520%25F0%259F%2587%25B2%25CA%2580%2520%25F0%259F%2587%25AB%25C9%25AA%25CA%2580%25E1%25B4%2587%25C2%25BB%25E2%2583%259F%25F0%259F%2587%25AE%25F0%259F%2587%25B3%2520%2528%2520%2523Hindu%2520%2529%2520%25E0%25A4%259C%25E0%25A4%25AF%2520%25E0%25A4%25B6%25E0%25A5%258D%25E0%25A4%25B0%25E0%25A5%2580%2520%25E0%25A4%25B0%25E0%25A4%25BE%25E0%25A4%25AE%2520%25F0%259F%259A%25A9%2522%252C%2522last_name%2522%253A%2522%2522%252C%2522username%2522%253A%2522Mr_Maurya%2522%252C%2522language_code%2522%253A%2522en%2522%252C%2522allows_write_to_pm%2522%253Atrue%257D%26chat_instance%3D5363848827076348223%26chat_type%3Dsender%26auth_date%3D1718583909%26hash%3D2dd0aafdfade6c3fa96e2c912dc498e02f1efc5933f3f6bd7f1edb3688f98528&tgWebAppVersion=7.4&tgWebAppPlatform=android&tgWebAppThemeParams=%7B%22bg_color%22%3A%22%23212d3b%22%2C%22section_bg_color%22%3A%22%231d2733%22%2C%22secondary_bg_color%22%3A%22%23151e27%22%2C%22text_color%22%3A%22%23ffffff%22%2C%22hint_color%22%3A%22%237d8b99%22%2C%22link_color%22%3A%22%235eabe1%22%2C%22button_color%22%3A%22%2350a8eb%22%2C%22button_text_color%22%3A%22%23ffffff%22%2C%22header_bg_color%22%3A%22%23242d39%22%2C%22accent_text_color%22%3A%22%2364b5ef%22%2C%22section_header_text_color%22%3A%22%2379c4fc%22%2C%22subtitle_text_color%22%3A%22%237b8790%22%2C%22destructive_text_color%22%3A%22%23ee686f%22%7D')
    title = await page.title()
    print(title)
    await browser.close()

if __name__ == "__main__":
    asyncio.run(main())
