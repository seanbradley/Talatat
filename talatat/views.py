import json

from pyramid.view import view_config, forbidden_view_config, notfound_view_config
from pyramid.response import Response
from pyramid.httpexceptions import HTTPNotFound

from talatat.models import Root, Musician, Musicians

import logging
log = logging.getLogger(__name__)

#index page
@view_config(context=Root, renderer='json')
def index(context, request):
    return {'info': 'Concert Talent API'}

#GET a list of all musicians
@view_config(request_method='GET', context=Musicians, renderer='json')
def list_musicians(context, request):
    return context.retrieve()

#GET a specific musician
@view_config(request_method='GET', context=Musician, renderer='json')
def get_musician(context, request):
    r = context.retrieve()

    if r is None:
        raise HTTPNotFound()
    else:
        return r

#UPDATE a musician
@view_config(request_method='PUT', context=Musician, renderer='json')
def update_musician(context, request):
    context.update(request.json_body, True)

    return Response(
        status='202 Accepted',
        content_type='application/json; charset=UTF-8')

#CREATE a musician
@view_config(request_method='POST', context=Musicians, renderer='json')
def create_musician(context, request):
    context.create(request.json_body)

    return Response(
        status='201 Created',
        content_type='application/json; charset=UTF-8')

#DELETE a musician
@view_config(request_method='DELETE', context=Musician, renderer='json')
def delete_musician(context, request):
    context.delete()

    return Response(
        status='202 Accepted',
        content_type='application/json; charset=UTF-8')

#ERROR--not found
@notfound_view_config()
def notfound(request):
    
    return Response(
        body=json.dumps({'message': 'The requested musician or musicians cannot be found!'}),
        status='404 Not Found',
        content_type='application/json')

#ERROR--forbidden
@forbidden_view_config()
def forbidden(request):
    
    return Response(
        body=json.dumps({'message': 'You are not authorized to access this data.'}),
        status='401 Unauthorized',
        content_type='application/json')
