import os
import requests

SOURCE_URL = os.environ.get("SOURCE_M3U_URL")
OUTPUT_FILE = "goldkingpt.m3u"

if not SOURCE_URL:
    raise RuntimeError("SOURCE_M3U_URL is missing")

response = requests.get(SOURCE_URL, timeout=60)
response.raise_for_status()

content = response.text

if not content.strip().startswith("#EXTM3U"):
    raise RuntimeError("Invalid M3U playlist")

with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
    f.write(content)

print("Playlist updated successfully")
