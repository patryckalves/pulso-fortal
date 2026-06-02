#!/usr/bin/env python3
"""Take screenshots of Pulso Fortal prototype pages."""
import asyncio
from playwright.async_api import async_playwright
import os

PAGES = [
    ("home", "https://patryckalves.github.io/pulso-fortal/"),
    ("onde-abrir", "https://patryckalves.github.io/pulso-fortal/onde-abrir.html"),
    ("termometro", "https://patryckalves.github.io/pulso-fortal/termometro.html"),
    ("contracheque", "https://patryckalves.github.io/pulso-fortal/contracheque.html"),
    ("radar-mei", "https://patryckalves.github.io/pulso-fortal/radar-mei.html"),
]

OUT_DIR = "/opt/data/pulso-fortal/docs/prints"
os.makedirs(OUT_DIR, exist_ok=True)

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        
        for name, url in PAGES:
            print(f"📸 {name}...")
            page = await browser.new_page(viewport={"width": 1280, "height": 900})
            await page.goto(url, wait_until="networkidle", timeout=15000)
            await page.wait_for_timeout(1000)  # let charts render
            path = os.path.join(OUT_DIR, f"{name}.png")
            await page.screenshot(path=path, full_page=True)
            print(f"  → {path}")
            await page.close()
        
        await browser.close()
    print("✅ Done!")

asyncio.run(main())
