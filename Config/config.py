__author__ = 'Enrico Giordano - MakarenaLabs'

import os


class Config():

    @staticmethod
    def get_config(self):
        if os.getenv('SERVER_SOFTWARE') and os.getenv('SERVER_SOFTWARE').startswith('Google App Engine/'):
            config = {
                'default': 'mysql',
                'mysql': {
                    'driver': 'mysql',
                    'host': 'localhost',
                    'database': 'your DB',
                    'user': 'your_user',
                    'password': '',
                    'unix_socket': '/cloudsql/your_app_ID:ybtdb',
                    'prefix': ''
                }
            }

        else:
            config = {
                'default': 'mysql',
                'mysql': {
                    'driver': 'mysql',
                    'host': 'localhost',
                    'database': 'your DB',
                    'user': 'your_user',
                    'password': 'your_password',
                    'prefix': ''
                }
            }

        return config

