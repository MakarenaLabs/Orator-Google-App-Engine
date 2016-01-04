__author__ = 'Enrico Giordano - MakarenaLabs'

from orator import Model
# import dependences here #
import hashlib


class Users(Model):

    #example of table
    __table__ = 'users'

    #example of hidden fields
    __hidden__ = ['password', 'remember_token', 'email', 'updated_at', 'created_at']

    #example of appends
    __appends__ = ['photo_profile']

    #example of fillable
    __fillable__ = ['facebook', 'skype', 'google_plus', 'sesso', 'data_nascita', 'collega_like',
                    'lavoratore_like', 'img_profile']

    #example of functions
    #def uploads(self):
    #    return self.has_many(upload.Upload, 'user_id')

