from td_scrapers import *
import td_scrapers.instascrape as IG_scraper

"""
Maximum is around 1200, please enter a limit as an int
Enter any valid instagram hashtag, you will get images in the most recent appearance.
Make sure your limit is under or equal to the total amount of images.
"""
#IG_scraper.scrape(searchstring, limit)
IG_scraper.scrape("hawkerfood", 10)
