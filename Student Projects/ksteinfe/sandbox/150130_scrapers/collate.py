from td_scrapers import *

"""
collate()
After running several scrapers, you will have a very full 'Images' folder and a bunch of .json
Simply go throught the Images folder and delete the ones you don't want until you have 1024
Now run collate and it will make a new json about your remaining images called "culled_index.json"
"""
collate()
