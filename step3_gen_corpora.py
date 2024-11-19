
import json, os, time

lMetaData = {}
with open("wikipedia_pages_metadata.json", "r") as read_file:
    lMetaData = json.load(read_file)

lLanguages = []

for (lPage, lData) in lMetaData.items():
    lLanguages = lLanguages + [x for x in lData.keys()]
    lLanguages = list(set(lLanguages))

lLanguages = sorted(lLanguages)
print("LANGUAGES", lLanguages)

page_sort_key = lambda x : int(x[1:])
lPages = sorted([page for page in lMetaData.keys()], key = page_sort_key)
print("PAGES" , lPages)

lSubsetLanguages = ["en", "ar", "fr", "zh", "zgh", "bm", "wo"]

for lang in lSubsetLanguages:
    print("GENERATING_CORPORA_FOR_LANG", lang)
    lang_text = ""
    for page in lPages:
        fname = "pages/" + page + "/" + page + "_" + lang + ".txt"
        try:
            with open(fname, "r") as f:
                lang_text = lang_text + f.read()
        except:
            pass
    fname2 = "output_corpora/List_of_articles_every_Wikipedia_should_have_" + lang + ".txt" 
    with open(fname2, "w") as f2:
        f2.write(lang_text)

    
