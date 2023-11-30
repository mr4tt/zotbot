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
        library_id = os.getenv('LIBRARY_ID')
        library_type = os.getenv('LIBRARY_TYPE')
        api_key = os.getenv('API_KEY')

        self.zotbot = zotero.Zotero(library_id, library_type, api_key)

load_dotenv()
zot = Zot()

collections = zotMethods.getCollections(zot.zotbot)

# loop thru each folder, create a file for it, and add each item into its file
for folder, folderID in collections.items():
    itemsInFolder = zot.zotbot.collection_items(folderID, itemType="-attachment")
    filename = "./files/" + folder + ".md"
    os.makedirs(os.path.dirname(filename), exist_ok=True)

    with open(filename, "w", encoding="utf-8") as folderFile:
        folderFile.write("# " + folder + "\n")
        for item in itemsInFolder:
            title = item["data"]["title"]
            url = item["data"]["url"]
            abstract = item["data"]["abstractNote"].replace("\n", " ")
            abstract = abstract[:351] + "..." if len(abstract) > 350 else abstract

            if not abstract or folder == "videos":
                folderFile.write(f'- [{title}]({url})\n\n')
            else:
                folderFile.write(f'- [{title}]({url}) - {abstract}\n\n')

# get collection names
# make folders for each one 

# cd into each folder
# using the id of the folder, search for things inside it and 

# combine each file together into the readme 