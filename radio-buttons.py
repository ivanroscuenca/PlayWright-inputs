import asyncio
from playwright.async_api import async_playwright, expect

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False)
        context = await browser.new_context()
        await context.tracing.start(screenshots=True, snapshots=True, sources=True)
        page = await context.new_page()
        await page.set_viewport_size({"width": 1800, "height": 1200})
        await page.goto("https://demoqa.com/radio-button")

        #---Actions---
        await page.check("#yesRadio", force=True)
        await page.screenshot(path="screenshots/radioButton.png")

        #---Assertions---
        await expect(page.locator("#yesRadio")).to_be_checked()
        await expect(page.locator(".text-success")).to_have_text("Yes")

        #---Stopping Tracing---
        await context.tracing.stop(path="logs/traceRadioButtons.zip")

        #---Closing browser---
        await browser.close()

asyncio.run(main())

