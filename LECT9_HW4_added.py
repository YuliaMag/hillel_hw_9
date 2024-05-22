# HW 4.2 (using string methods)
res = []
with open("wiki_page.txt") as f:
    for line in f:
        start_index = 0
        while start_index != -1:
            start_index = line.find("<a ", start_index)
            if start_index == -1:
                break
            else:
                start_index = line.find("href=\"", start_index) + len("href=\"")
                end_index = line.find("\"", start_index)
                href_value = line[start_index: end_index]
                res.append(href_value)
                start_index = end_index
print(res)








