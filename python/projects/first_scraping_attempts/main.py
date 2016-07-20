from scraper_engine import *

 with open("input.csv", 'r') as missing_images:
     reader = csv.reader(missing_images, delimiter = ',', quotechar = '"')
     reader.__next__()
     for row in reader:
         card_type = row[0].strip()
         edition = row[1].strip()
         title = row[2].strip()
         if not row[3]:
             variation = None
         if row[3]:
             variation = row[3].strip()
         if not row[4]:
             number = None
         if row[4]:
             number = row[4].strip()
         do_scraping(card_type, edition, title, variation, number)


 for item in url_error_list:
     print(item)

