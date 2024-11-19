
import urllib, json, re
import urllib.request

from bs4 import BeautifulSoup

def get_wikipedia_page_metadata(page):
    uri = "https://www.wikidata.org/wiki/" + page
    print(page, uri)
    html = ""
    with urllib.request.urlopen(uri) as f:
        html = f.read().decode('utf-8')

    lMetaData = {page : {}}
    
    soup = BeautifulSoup(html, "html.parser")
    x = soup.find_all("span", {"class": "wikibase-sitelinkview-link"})
    for s in x:
        print("XXXXXXXXXXXXXXXXXXX", (type(s), s.text, s))
        y = s.find('a')
        print("XXXXXXXXXXXXXXXXXXX___1", (type(y), y.text, y))
        print("XXXXXXXXXXXXXXXXXXX___2", (y['href'], y['hreflang'], y['title']))
        lLang = y['hreflang']
        lLink = y["href"]
        lTitle = y["title"]
        print(page, lLang , lTitle, lLink)
        lMetaData[page][lLang] = {"Title" : lTitle, "Link" : lLink}
    print("PAGE_METADATA", page, lMetaData)
    lEnglishTitle = lMetaData[page]["en"]["Title"]
    lEnglishTitle = lEnglishTitle.replace("/", "_").replace(" ", "_")
    with open("metadata/wikipedia_pages_metadata_" + page + "_" + lEnglishTitle + ".json", "w") as outfile:
        json.dump(lMetaData, outfile, indent=4)
    return lMetaData


lMetaData = {}
with open("pagepile_json_meta_61569.json", "r") as read_file:
    lWikipediaPages = json.load(read_file)
    print(lWikipediaPages.keys())
    lMetaData = {}
    for page in [x for x in lWikipediaPages["pages"]]:
        lMetaData_page = get_wikipedia_page_metadata(page)
        lMetaData.update(lMetaData_page)

                        
with open("wikipedia_pages_metadata.json", "w") as outfile:
    json.dump(lMetaData, outfile, indent=4)
