# play_gmail_login.py
import os
from time import time
from playwright.sync_api import sync_playwright, TimeoutError
import pandas as pd

# Read credentials from environment variables (recommended)
EMAIL = os.getenv("GMAIL_EMAIL", "mye-mail@gmail.com")
PASSWORD = os.getenv("GMAIL_PASSWORD", "password")

clicks = []

def log_click(selector, page):
    # store selector and a browser-side timestamp (ms) and a local timestamp (s)
    try:
        js_time = page.evaluate("Date.now()")
    except Exception:
        js_time = None
    clicks.append({
        "selector": selector,
        "js_time_ms": js_time,
        "local_time_s": time()
    })

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False, slow_mo=50)  # slow_mo helps to see actions
    page = browser.new_page()
    try:
        # Open Gmail sign-in
        page.goto("https://mail.google.com/", timeout=30000)
        
        # Fill email (identifier)
        page.wait_for_selector('input[type="email"]', timeout=15000)
        page.fill('input[type="email"]', EMAIL)
        log_click('input[type="email"]', page)
        
        # Click Next after email
        # Use the ID that Google exposes; if it changes you may need to update selector
        page.click('#identifierNext')
        log_click('#identifierNext', page)

        # Wait for password input to appear (Google may show additional interstitials)
        page.wait_for_selector('input[type="password"]', timeout=20000)
        page.fill('input[type="password"]', PASSWORD)
        log_click('input[type="password"]', page)

        # Click Next after password
        page.click('#passwordNext')
        log_click('#passwordNext', page)

        # Wait for Gmail inbox to load — this is heuristic: wait for URL or a known element
        try:
            page.wait_for_url("https://mail.google.com/*", timeout=30000)
        except TimeoutError:
            # As fallback, wait for a known inbox element (subject list / main role)
            page.wait_for_selector('div[role="main"]', timeout=30000)

        print("Login flow completed (or reached post-login page).")
    except TimeoutError as e:
        print("Timeout while trying to perform steps. Google may have shown extra verification/CAPTCHA.")
        print("Exception:", e)
    except Exception as e:
        print("An unexpected error occurred:", e)
    finally:
        browser.close()

# Persist clicks to CSV
df = pd.DataFrame(clicks)
df.to_csv("clickmap_gmail.csv", index=False)
print(f"Saved {len(clicks)} click records to clickmap_gmail.csv")
