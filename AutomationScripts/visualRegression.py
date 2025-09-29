from playwright.sync_api import sync_playwright
from PIL import Image
import imagehash


def hash_ss(path):
    return imagehash.phash(Image.open(path))

with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_page()
    page.goto("https://example.com")
    page.screenshot(path="current.png", full_page=True)

    curr = hash_ss("current.png")
    baseline = hash_ss("current1.png")
    print(f"Hamming Difference: {curr - baseline}")
    browser.close()
