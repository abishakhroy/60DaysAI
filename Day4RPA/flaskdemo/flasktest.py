import asyncio
from flask import Flask, request, jsonify
from playwright.async_api import async_playwright, TimeoutError as PlaywrightTimeoutError

app = Flask(__name__)

DEFAULT_CHANNEL = "The AI Dude - Tamil"


async def open_youtube_channel(channel_name: str):
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False)  # GUI visible
        page = await browser.new_page()

        # 1) Open YouTube
        await page.goto("https://www.youtube.com", wait_until="domcontentloaded")

        # 2) Handle cookie / consent popups (best effort)
        for btn in ["Accept all", "I agree", "Agree", "Accept the use of cookies"]:
            try:
                await page.get_by_role("button", name=btn).click(timeout=1500)
                break
            except PlaywrightTimeoutError:
                pass

        # 3) Search for the channel
        search_box = page.get_by_role("combobox", name="Search")
        await search_box.click()
        await search_box.fill(channel_name)
        await page.keyboard.press("Enter")

        await page.wait_for_load_state("domcontentloaded")

        # 4) Open the channel
        try:
            await page.get_by_role("link", name=channel_name).first.click(timeout=8000)
        except PlaywrightTimeoutError:
            channel_link = page.locator('a[href^="/@"]:visible').first
            await channel_link.wait_for(state="visible", timeout=15000)
            await channel_link.click()

        # Wait a bit so you can see the channel page
        await page.wait_for_timeout(4000)

        current_url = page.url
        await browser.close()
        return current_url


@app.route("/health", methods=["GET"])
def health():
    return jsonify({"status": "ok"}), 200


@app.route("/open-channel", methods=["POST"])
def open_channel():
    data = request.get_json(silent=True) or {}
    channel_name = data.get("channel_name", DEFAULT_CHANNEL)

    try:
        # Run the async Playwright function inside Flask request
        url = asyncio.run(open_youtube_channel(channel_name))
        return jsonify({
            "success": True,
            "channel_name": channel_name,
            "opened_url": url
        }), 200

    except Exception as e:
        return jsonify({
            "success": False,
            "error": str(e),
            "channel_name": channel_name
        }), 500


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)