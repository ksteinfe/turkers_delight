Image Scrapers
===============
1. In your main directory, edit google_scrape.py, instagram_scrape.py or both to perform your scrape. Images are saved to a subfolder "/img".
2. Manually remove and/or edit images in this subfolder to arrive at your selected 1024 collection for this week.
3. Back up in your main directory, run python collate.py to collate your images and produce a single summary JSON.
4. Next, run python process_for_web.py to produce web-sized images and a reformatted JSON file, which are saved in the subfolder "/webimg". These are small images - and the ones you should submit for class, and that you may allow to hang out on the class GIT.
5. Once satisfied with your scrape, and before you commit your changes to GIT, move the contents of the /img folder to somewhere else on your computer (don't sync these files to GIT).
6. Repeat. You may run multiple scrapes in this manner to try different things out.
7. When you've settled on a good set of 1024 images, copy these to a directory called img_1028 at the top level of your Student Project folder.  See my folder for an example.