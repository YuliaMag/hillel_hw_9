
# HW 4.1 (using regular expressions)
import re
with open("wiki_page.txt", "r") as f:
    text = f.read()

res = re.findall(r"<a.href=\"(.*?)\"", text)
print(res)

# =============================================== #

# HW 4.2 (using string methods)

res = []
tag_a = "<a"

with open("wiki_page.txt") as f:
    for line in f:
        if tag_a in line:
            start_tag_a_index = line.index(tag_a)
            start_href_attr_index = line.index("href=\"", start_tag_a_index)
            end_href_attr_index = line.index("\"", start_href_attr_index + len("href=\""))
            href_value = line[(start_href_attr_index + len("href=\"")): end_href_attr_index]
            res.append(href_value)

print(res)

# line_n = str([i for i in range(len(line)) if line.startswith(tag_a, i)])
