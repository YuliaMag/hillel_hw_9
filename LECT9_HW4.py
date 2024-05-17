
# HW 4.1 (using regular expressions)
import re
with open("wiki_page.txt", "r") as f:
    text = f.read()
res = re.findall(r"\d{3}.*?\D\d{3}", text)
print(res)

# =============================================== #

# HW 4.2 (using string methods)
with open("wiki_page.txt", "r") as f:
    text = f.read()

res = []

for line in text.split(" "):
    if "href=" in line and line.startswith("href=") and line.endswith("\""):
        ln = line.removeprefix("href=\"").removesuffix("\"")
        res.append(ln)

print(res)

