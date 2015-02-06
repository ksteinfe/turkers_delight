from td_scrapers import *

"""
collate()
After running several scrapers, you will have a very full 'Images' folder and a bunch of .json
Simply go throught the Images folder and delete the ones you don't want until you have 1024
Now run collate and it will make a new json about your remaining images called "Culled_Index.json"
"""
collate()

"""
process_for_web()
this function will calculate the rgb average values of your images, which is very slow.
It will then resize and rename all the images in your collated index ("Culled_Index.json") from collate(), 
into a folder called 'webImages' and create a web-index for tracking your online survey results.
"""
#process_for_web()