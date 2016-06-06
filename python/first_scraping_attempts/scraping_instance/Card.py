import urllib.request
import os
import re
import shutil


class Card:
    """ A magic card. """
    slugRe = re.compile('[^a-zA-Z\-]')
    adjacentHyphensRe = re.compile(r"([-]){2,}")
    errors = [('edition', 'title', 'error')]
    abbreviations = {
        'Eternal Masters': 'ema/cards',
        }



    def __init__(self, **kwargs):
        self.title = kwargs['title']
        self.edition = kwargs['edition'] if 'edition' in kwargs else 'Eternal Masters'
        self.variation = kwargs['variation'] if 'variation' in kwargs else ''
        self.title_slug = self.get_slug(self.title)
        self.edition_slug = self.get_slug(self.edition)
        self.save_location = "{}/{}.jpg".format(self.edition_slug, self.title_slug)
        self.directory = '/'.join(self.save_location.split('/')[0:-1])
        self.foreign_name_slug = self.get_foreign_name_slug()
        self.foreign_edition_slug = self.get_foreign_edition_slug()
        self.static = kwargs['static'] if 'static' in kwargs else ''
        self.url = kwargs['url'] if 'url' in kwargs else self.get_url()


    def get_slug(self, attribute):
        slug = getattr(self, attribute).strip()
        slug = slug.replace(" ", "-").lower()
        slug = slugRe.sub('', slug)
        slug = adjacentHypensRe.sub("-", slug)
        return slug


    def get_foreign_edition_slug(self):
        return abbreviations[self.edition]


    def get_url(self):
        if self.static:
            return "{}/{}/{}.jpg".format(self.static,
                                         self.foreign_edition_slug,
                                         self.foreign_name_slug)
        if not self.static:
            pass


    def get_foreign_name_slug(self):
        """ At present, this procedure is explicitly for mythicspoilers.com """
        foreign_slug = self.name_slug.replace('-', '')
        return foreign_slug


    def download(self):
        """ Handles the request, download, and saving. """
        #download prework -- check if exists, mkdir
        if os.path.isfile(self.save_location):
            print("++ (already saved) ", self.save_location)
            return
        os.makedirs(self.directory, exist_ok=True)

        #download core function -- make request, save
        try:
            req = urllib.request.Request(self.url)
            req.add_header('User-agent',
                           'Python 3.4.3; Jordan M.; jmcqueen@cardkingdom.com')
            with urllib.request.urlopen(req) as response, open(self.save_location, 'wb') as out_file:
                shutil.copyfileobj(response, out_file)
                print("++ ", self.save_location)
                response.close()
        except Exception as error:
            print("-- ", error)
            errors.append((self.edition, self.title, self.url, error))
        finally:
            try:
                response.close()
            except NameError:
                pass

