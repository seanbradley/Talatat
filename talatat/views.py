from pyramid.view import view_config

CITIES = {
    'paris': {
        'name': 'Paris',
        'population': '2,234,105'
    },
    'sf': {
        'name': 'San Francisco',
        'population': '812,826'
    }
}

MUSICIANS = {
    "sean": {
        "name":"Sean", 
        "instrument":"Violin",
        "instrument_maker":"Melanson", 
        "conservatory":"Eastman",
        "referral":"Heifetz",
        "reviews": [{
        "stars": 5,
        "body": "I love this violinist!",
        "author": "joe@example.com",
        "createdOn": 1397490980837
        }, {
        "stars": 5,
        "body": "Amazing musician!",
        "author": "tim@example.com",
        "createdOn": 1397490980837
        }], 
        "ontour":"false", 
        "canbook":"true"
    },
    "rachel": {
        "name":"Rachel", 
        "instrument":"Electric Violin",
        "instrument_maker":"Yamaha", 
        "conservatory":"The Hague",
        "referral":"Kremer",
        "reviews": [{
        "stars": 5,
        "body": "So beautiful!",
        "author": "sarah@example.com",
        "createdOn": 1397490980837
        }, {
        "stars": 5,
        "body": "Exquisite player!",
        "author": "natasha@example.com",
        "createdOn": 1397490980837
        }], 
        "ontour":"false", 
        "canbook":"true"
    },
    "dima": {
        "name":"Dima", 
        "instrument":"Viola",
        "instrument_maker":"Guarneri", 
        "conservatory":"Moscow",
        "referral":"Primrose",
        "reviews": [{
        "stars": 5,
        "body": "Such a rich tone!",
        "author": "sam@example.com",
        "createdOn": 1397490980837
        }, {
        "stars": 3,
        "body": "Jokes around on the job.",
        "author": "eddie@example.com",
        "createdOn": 1397490980837
        }],  
        "ontour":"false", 
        "canbook":"true"
    },
    "judy": {
        "name":"Judy", 
        "instrument":"Cello",
        "instrument_maker":"Stradivarius", 
        "conservatory":"USC",
        "referral":"Ma",
        "reviews": [{
        "stars": 5,
        "body": "Never seen such a good-looking cellist!",
        "author": "blaze@example.com",
        "createdOn": 1397490980837
        }, {
        "stars": 2,
        "body": "This cellist is such a flirt.",
        "author": "susie@example.com",
        "createdOn": 1397490980837
        }],  
        "ontour":"false", 
        "canbook":"true"
    }
}

@view_config(route_name='musician', renderer='json')
def get_musician(request):
    name = request.matchdict['name']
    return MUSICIANS[name]

@view_config(route_name='musicians', renderer='json')
def list_musicians(request):
    return MUSICIANS
