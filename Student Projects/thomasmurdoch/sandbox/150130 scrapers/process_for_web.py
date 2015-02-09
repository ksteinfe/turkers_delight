from td_scrapers import *

"""
process_for_web()
this function will calculate the rgb average values of your images, which is very slow.
It will then resize and rename all the images in your collated index ("Culled_Index.json") from collate(), 
into a folder called 'webImages' and create a web-index for tracking your online survey results.
"""
process_for_web()