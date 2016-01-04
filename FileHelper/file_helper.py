__author__ = 'Enrico Giordano - MakarenaLabs'

from google.appengine.api import images
import google.appengine.ext.blobstore as blobstore


class FileHelper():
    @staticmethod
    def get_image(name, size=None, crop=False, secure_url=None):
        key = blobstore.create_gs_key("your GS dir/"+name)
        img = images.get_serving_url(key, size, crop, secure_url)
        return img

    @staticmethod
    def get_profile_img(self, name):
        return self.get_image(name=name, size=200, crop=200, secure_url=True)

    @staticmethod
    def get_thumb(self, name):
        return self.get_image(name=name, size=400, crop=400, secure_url=True)
