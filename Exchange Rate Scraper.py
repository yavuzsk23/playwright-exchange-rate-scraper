import asyncio
from playwright.async_api import async_playwright, TimeoutError as PlaywrightTimeoutError

CURRENCIES = {
    "USD": "US Dollar",
    "EUR": "Euro",
}


async def fetch_exchange_rates():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page()

        print("Connecting to doviz.com...")
        try:
            await page.goto("https://www.doviz.com", timeout=15000)
        except PlaywrightTimeoutError:
            print("Error: the page took too long to load. Check your internet connection.")
            await browser.close()
            return

        results = {}
        for code, label in CURRENCIES.items():
            try:
                selector = f'span[data-socket-key="{code}"]'
                await page.wait_for_selector(selector, timeout=10000)
                results[code] = await page.inner_text(selector)
            except PlaywrightTimeoutError:
                results[code] = None
                print(f"Warning: could not find the exchange rate for {code} (page layout may have changed).")

        await browser.close()

        print("\n" + "=" * 35)
        print("CURRENT EXCHANGE RATES (TRY)")
        print("=" * 35)
        for code, label in CURRENCIES.items():
            value = results.get(code)
            if value:
                print(f"{label} ({code}): {value} TL")
            else:
                print(f"{label} ({code}): unavailable")
        print("=" * 35 + "\n")


if __name__ == "__main__":
    asyncio.run(fetch_exchange_rates())
