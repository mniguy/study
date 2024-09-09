# 01
url = input("URL: ").strip()

username = url.removeprefix("https://twitter.com/", "")
print(f"Username: {username}")

# 02
# re.sub(pattern, repl, string, count=0, flags=0)
import re

url = input("URL: ").strip()

if matches := re.search(r"^https?://(?:www\.)?twitter\.(.+)/(.+)$", url, re.IGNORECASE):
    if matches.group():
        print(f"Username:", matches.group(1))