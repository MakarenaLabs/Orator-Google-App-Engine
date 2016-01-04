from bottle import Bottle, request
from orator import DatabaseManager, Model
from Config.config import Config
from FileHelper.file_helper import FileHelper
#import controllers#
from Controllers.users_controller import UsersController
import logging
import sys

db = DatabaseManager(Config.get_config(self=0))
Model.set_connection_resolver(db)
bottle = Bottle()


def exec_command(controller, method, other="", input=None):
    try:
        if input is None:
                if other != "":
                    return eval(controller + "." + method + "('" + other + "')")
                else:
                    return eval(controller + "." + method + "()")
        else:
            return eval(controller + "." + method + "(" + input + ")")
    except:
        logging.error('%s', sys.exc_info())


#examples of routing
@bottle.route('/<controller>/<method>', method='GET')
def show_multiple(controller="", method=""):
    return exec_command(controller=controller, method=method)


@bottle.route('/<controller>/<method>/<other>', method='GET')
def show_single_or_other(controller="", method="", other=""):
    return exec_command(controller=controller, method=method, other=other)


@bottle.route('/<controller>/<method>', method='POST')
def create(controller="", method=""):
    return exec_command(controller=controller, method=method, input=request.query)


@bottle.route('/<controller>/<method>/id', method='DELETE')
def delete(controller="", method="", id=""):
    return exec_command(controller=controller, method=method, other=id)


@bottle.route('/<model>/<method>/id', method='PUT')
def update(controller="", method="", id=""):
    return exec_command(controller=controller, method=method, other=id)


# Define an handler for 404 errors.
@bottle.error(404)
def error_404(error):
    """Return a custom 404 error."""
    return '404 Error'

@bottle.error(500)
def error_404(error):
    """Return a custom 500 error."""
    return 'Data Service Error'

