from pyzotero import zotero
from dotenv import load_dotenv
import os
import zotMethods

"""
Instantiating a Zotero bot for API calls
"""
class Zot():
    """
    Creates zotbot
    Vars: 
        library_id (str): env var of your library id
        library_type (str): user or group 
        api_key (str): Zotero API key
    """
    def __init__(self) -> None:
        library_id = os.environ.get['LIBRARY_ID']
        library_type = os.environ.get['USER_TYPE']
        api_key = os.environ.get['API_KEY']

        self.zotbot = zotero.Zotero(library_id, library_type, api_key)

load_dotenv()
zot = Zot()

# create files for each Zotero collection
collections = zotMethods.getCollections(zot.zotbot)
os.makedirs(os.path.dirname("../files/"), exist_ok=True)

# creating TOC 
with open("../README.md", "w", encoding="utf-8") as readme:
    readme.write("Collection of interesting things I've gathered from around the internet.\n")
    readme.write("To view a single category, check the files/ folder.\n\n")
    readme.write("# Table of Contents\n")
    for folderName in collections.keys():
        readme.write(f"- [{folderName}](#{folderName})\n")

# loop thru each folder, create a file for it, and add each item into its file
for folder, folderID in collections.items():
    itemsInFolder = zot.zotbot.collection_items(folderID, itemType="-attachment")
    filename = "../files/" + folder + ".md"

    # print each item and description to correct category file
    with open(filename, "w+", encoding="utf-8") as folderFile:
        folderFile.write("# " + folder + "\n")
        for item in itemsInFolder:
            title = item["data"]["title"]
            url = item["data"]["url"]
            abstract = item["data"]["abstractNote"].replace("\n", " ")
            abstract = abstract[:351] + "..." if len(abstract) > 350 else abstract

            if not abstract or folder == "videos" or folder == "crochet":
                folderFile.write(f'- [{title}]({url})\n\n')
            else:
                folderFile.write(f'- [{title}]({url}) - {abstract}\n\n')

        # append to README
        with open("../README.md", "a", encoding="utf-8") as readme:
            folderFile.seek(0)
            readme.write(folderFile.read())