from urlparse import urlparse 
import json
  
from pyramid.config import Configurator
from pyramid.renderers import JSON

import pymongo
from bson import json_util

from talatat.models import Root


class MongoJSONRenderer: 
    def __init__(self, info): 
        pass

    def __call__(self, value, system): 
        request = system.get('request') 
        if request is not None: 
            if not hasattr(request, 'response_content_type'): 
                request.response_content_type = 'application/json' 
        return json.dumps(value, default=json_util.default)
    
def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    config = Configurator(settings=settings, root_factory=Root)
    config.add_renderer('json', MongoJSONRenderer)
    #config.add_renderer('json', JSON(indent=4))
    #config.include('pyramid_chameleon')
    #config.add_static_view('static', 'static', cache_max_age=3600)
    
    db_url = urlparse(settings['mongo_uri'])
    config.registry.db = pymongo.Connection(
       host=db_url.hostname,
       port=db_url.port,
    )

    def add_db(request):
       db = config.registry.db[db_url.path[1:]]
       if db_url.username and db_url.password:
           db.authenticate(db_url.username, db_url.password)
       return db
        
    config.add_request_method(add_db, 'db', reify=True)
    config.scan('.views')
    return config.make_wsgi_app()
