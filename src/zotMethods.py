# TODO: sorting?

# get all items from your Zotero library (prints type and ID)
def getAllItems(zot):
    items = zot.everything(zot.items())
    itr = 1
    for item in items:
        print('Item: %s | Key: %s' % (item['data']['itemType'], item['data']['key']))
        print(itr)
        itr+= 1

# search by title or author (but i think most things in my lib dont have author)
def getItemByTitle(zot, search: str, itemType=None):
    items = zot.everything(zot.items(q=search))
    itr = 1
    for item in items:
        print(item)
        print('Item: %s | Key: %s | Title: %s | URL: %s' % (item['data']['itemType'], item['data']['key'], item["data"]["title"], item["data"]["url"]))
        print(itr)
        itr+= 1

# returns dict of {folder : folder ID}
def getCollections(zot) -> dict:
    collection = {}
    col = zot.collections()

    for folder in col:
        collection[folder["data"]["name"]] = folder["data"]["key"]
    
    return collection
