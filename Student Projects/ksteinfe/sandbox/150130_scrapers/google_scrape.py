from td_scrapers import *
import td_scrapers.google_image_scrape as Google_scraper


"""
Maximum is 800-1000, please enter a limit as an int
you can enter any search string as it would appear as a url param
"runners" or "runners+legs" etc.
"""
#Google_scraper.scrape(searchstring, limit)
Google_scraper.scrape("cup+saucer", 3, brow="Firefox")

