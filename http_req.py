import requests

urls = [
    "https://twitter.com/robots.txt",
    "https://en.wikipedia.org/robots.txt"
]

for url in urls:
    response = requests.get(url)
    filename = url.split("//")[1].replace("/", "_") #+ ".txt" назва файлу з URL
    with open(filename, "w", encoding="utf-8") as f:
        f.write(response.text)
    print(f"Saved: {filename}")
print(f"All files have been saved. Total: {len(urls)} files.")