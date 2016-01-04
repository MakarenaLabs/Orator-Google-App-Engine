__author__ = 'Enrico Giordano - MakarenaLabs'
import datetime
from time import mktime
from time import localtime
from time import strftime
import json


class DateEncoder(json.JSONEncoder):

    def default(self, obj):
        if isinstance(obj, datetime.datetime):
            return strftime("%Y-%m-%d %H:%M:%S", localtime(int(mktime(obj.timetuple()))))
        return json.JSONEncoder.default(self, obj)
