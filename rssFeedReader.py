import feedparser

url = "https://www.nairaland.com/feed"

file = feedparser.parse(url)

for entry in file.entries:
    # print(entry)
    print("title: ", entry.title)
    print("title_detail: ", entry.title_detail.value)
    print("link: ", entry.link)
    print("\n", entry.summary)
    print("----------------------------")
    print("\n\n")

