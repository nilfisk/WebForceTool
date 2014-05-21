__author__ = 'Kyah'

from werkzeug.wsgi import DispatcherMiddleware
from werkzeug.serving import run_simple

from webforcetool import database, restAPI, webinterface


if __name__ == '__main__':
    database.init()
    api = restAPI.init()
    web = webinterface.init()
    application = DispatcherMiddleware(web, {
        '/api': api
    })
    run_simple('localhost', 5000, application,
               use_reloader=True, use_debugger=True, use_evalex=True)