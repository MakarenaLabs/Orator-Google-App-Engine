__author__ = 'Enrico Giordano - MakarenaLabs'

import Models.users as u
#import dependences from models here #


class UsersController:

    def __init__(self):
        pass

    #example of "get" method
    @staticmethod
    def get_profile(id):
        user = u.Users.find(id).to_dict()
        ret = json.dumps(user, cls=de.DateEncoder)
        return ret

