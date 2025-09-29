from playwright.sync_api import sync_playwright
import json

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    context = browser.new_context()
    page = context.new_page()

    # Intercept and mock a specific API endpoint
    def handle(route, request):
        if "api/items" in request.url:
            # Simulate a slow, partial response (or 500)
            route.fulfill(
                status=500,
                headers={"Content-Type": "application/json"},
                body=json.dumps({"error": "simulated failure"})
            )
        else:
            route.continue_()

    page.route("**/*", handle)
    page.goto("https://www.hotmail.com")
    # trigger the UI path that calls /api/items
    page.click("button#load-items")
    print(page.locator("#alert").inner_text())
    browser.close()