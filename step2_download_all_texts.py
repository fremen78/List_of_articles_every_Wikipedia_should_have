import json, os, time

lMetaData = {}
with open("wikipedia_pages_metadata.json", "r") as read_file:
    lMetaData = json.load(read_file)

lLanguages = []

for (lPage, lData) in lMetaData.items():
    lLanguages = lLanguages + [x for x in lData.keys()]
    lLanguages = list(set(lLanguages))

lLanguages = sorted(lLanguages)
print(lLanguages)

def save_link_internal(page_txt, filename):
    with open(filename, "w") as f1:
        f1.write(page_txt)

def save_link(page, lLink, filename):
    lDir = os.path.dirname(filename)
    os.makedirs(lDir , exist_ok = True)
    if(os.path.isfile(filename)):
        print("SAVE_LINK_FILE_ALREADY_EXISTS", (page, filename))
        return
    import wikipedia
    try:
        print("SAVE_LINK", (page, filename))
        lWikiPage = lLink.split("/")[-1]
        page_txt = wikipedia.page(lWikiPage).content
        save_link_internal(page_txt, filename)
    except Exception as ex:
        print("SAVE_LINK_FAILURE", (page, filename, str(ex)))
        

def downlaod_all_pages_for_one_lang(lang):
    import wikipedia
    print("WIKIPEDIA_LANGAUES", wikipedia.languages())
    wikipedia.set_lang(lang)
    for (lPage, lData) in lMetaData.items():
        if(lData.get(lang) is not None):
            lLink = lData[lang]["Link"]
            # lang_full = wikipedia.languages()[lang]
            filename =  "pages/" + lPage + "/" + lPage + "_" + lang +  ".txt"
            save_link(lPage, lLink, filename)


# downlaod_all_pages_for_one_lang('fr')
from multiprocessing import Pool

with Pool(64) as p:
    p.map(downlaod_all_pages_for_one_lang, lLanguages)

