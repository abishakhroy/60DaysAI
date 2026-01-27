import asyncio
from playwright.async_api import async_playwright

async def run():
    async with async_playwright() as p:
        # 1. Launch Browser
        # Use channel="chrome" or "msedge" if you want to use your local browser
        browser = await p.chromium.launch(headless=False) 
        context = await browser.new_context()
        page = await context.new_page()

        # 2. Navigate and Search
        print("Navigating to Google...")
        # 'wait_until' ensures the page is functionally loaded
        await page.goto("https://www.google.com", wait_until="domcontentloaded")

        # Handle potential "I agree" cookie buttons
        try:
            cookie_btn = page.get_by_role("button", name="Accept all")
            if await cookie_btn.is_visible():
                await cookie_btn.click()
        except:
            pass

        # Perform Search
        search_box = page.get_by_role("combobox", name="Search")
        await search_box.fill("Sri Lanka vs England match news")
        await search_box.press("Enter")

        # 3. Wait for Navigation to search results
        # This waits for the network to be idle after the search
        await page.wait_for_load_state("networkidle")

        # 4. Extract News Headlines
        print("\n--- Latest Headlines ---\n")
        
        # Using a more specific locator for news results
        headlines = await page.locator("h3").all()
        
        for i, headline in enumerate(headlines[:6]):
            text = await headline.inner_text()
            if text:
                print(f"Headline {i+1}: {text}")

        # Keep browser open to see results
        await asyncio.sleep(5)
        await browser.close()

# Run the async function
if __name__ == "__main__":
    asyncio.run(run())