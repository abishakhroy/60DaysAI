import asyncio
from playwright.async_api import async_playwright, TimeoutError as PlaywrightTimeoutError

CHANNEL_NAME = "The AI Dude - Tamil"

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False)
        page = await browser.new_page()

        # 1️⃣ Open YouTube
        await page.goto("https://www.youtube.com", wait_until="domcontentloaded")

        # 2️⃣ Handle cookie / consent popups (best effort)
        for btn in ["Accept all", "I agree", "Agree", "Accept the use of cookies"]:
            try:
                await page.get_by_role("button", name=btn).click(timeout=1500)
                break
            except PlaywrightTimeoutError:
                pass

        # 3️⃣ Search for the channel
        search_box = page.get_by_role("combobox", name="Search")
        await search_box.click()
        await search_box.fill(CHANNEL_NAME)
        await page.keyboard.press("Enter")

        await page.wait_for_load_state("domcontentloaded")

        # 4️⃣ Open the channel
        # First try: click channel with exact name
        try:
            await page.get_by_role("link", name=CHANNEL_NAME).first.click(timeout=8000)
        except PlaywrightTimeoutError:
            # Fallback: click first channel-style link (/@handle)
            channel_link = page.locator('a[href^="/@"]:visible').first
            await channel_link.wait_for(state="visible", timeout=15000)
            await channel_link.click()

        # ✅ Stop here (channel page is open)
        await page.wait_for_timeout(4000)
        await browser.close()

if __name__ == "__main__":
    asyncio.run(main())