from playwright.sync_api import sync_playwright
import pandas as pd

clicks = []
with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://example.com")
    # simulate flows
    page.click("header >> text=Sign in")
    clicks.append({"selector": "header >> text=Sign in", "time": page.evaluate("Date.now()")})
    # ... more flows ...
    browser.close()

df = pd.DataFrame(clicks)
df.to_csv("clickmap.csv", index=False)