#-*- coding: utf-8 -*-


from datetime import datetime
from flask import render_template, json,  request, jsonify
from Ventilation import app
import simplejson
import yaml
import config
import pydocumentdb.document_client as document_client
import pusher
import sys
reload(sys)  # Reload does the trick!
sys.setdefaultencoding('UTF8')

@app.route('/')
@app.route('/home')
def home():
    

    client = document_client.DocumentClient(config.DOCUMENTDB_HOST, {'masterKey': config.DOCUMENTDB_KEY})
    db = next((data for data in client.ReadDatabases() if data['id'] == config.DOCUMENTDB_DATABASE))
    coll = next((coll for coll in client.ReadCollections(db['_self'])))

    lala = list(client.QueryDocuments(coll['_self'],
            {
                'query': 'SELECT * FROM c'
            }))

    pretty = json.loads(json.dumps(lala))

    query = list(client.QueryDocuments(coll['_self'],
            {
                'query': 'SELECT * FROM c.inside.temp'
            }))

    insideTemp = map(float, simplejson.loads(json.dumps(query)))

    query = list(client.QueryDocuments(coll['_self'],
            {
                'query': 'SELECT * FROM c.outside.temp'
            }))

    outsideTemp = map(float, simplejson.loads(json.dumps(query)))

    query = list(client.QueryDocuments(coll['_self'],
            {
                'query': 'SELECT * FROM c.counter'
            }))

    counter = json.dumps(query)


    return render_template('index.html',  docs = json.dumps(pretty, indent=4),
            insideTemp = insideTemp[-25:],
            outsideTemp = outsideTemp[-25:],
            counter = 50)

@app.route("/show")
def show():

    client = document_client.DocumentClient(config.DOCUMENTDB_HOST, {'masterKey': config.DOCUMENTDB_KEY})
    db = next((data for data in client.ReadDatabases() if data['id'] == config.DOCUMENTDB_DATABASE))
    coll = next((coll for coll in client.ReadCollections(db['_self'])))

    lala = list(client.QueryDocuments(coll['_self'],
            {
                'query': 'SELECT * FROM c'
            }))

    pretty = json.loads(json.dumps(lala))

    query = list(client.QueryDocuments(coll['_self'],
            {
                'query': 'SELECT * FROM c.inside.temp'
            }))

    insideTemp = map(float, simplejson.loads(json.dumps(query)))

    query = list(client.QueryDocuments(coll['_self'],
            {
                'query': 'SELECT * FROM c.outside.temp'
            }))

    outsideTemp = map(float, simplejson.loads(json.dumps(query)))

    query = list(client.QueryDocuments(coll['_self'],
            {
                'query': 'SELECT * FROM c.counter'
            }))

    counter = json.dumps(query)

    return render_template('results.html',
            year=datetime.now().year,
            docs = json.dumps(pretty, indent=4),
            insideTemp = insideTemp[-25:],
            outsideTemp = outsideTemp[-25:],
            counter = 50)

@app.route('/create')
def create():
    
    client = document_client.DocumentClient(config.DOCUMENTDB_HOST, {'masterKey': config.DOCUMENTDB_KEY})

    # Attempt to delete the database.  This allows this to be used to recreate
    # as well as create
    try:
        db = next((data for data in client.ReadDatabases() if data['id'] == config.DOCUMENTDB_DATABASE))
        client.DeleteDatabase(db['_self'])
    except:
        pass

    # Create database
    db = client.CreateDatabase({ 'id': config.DOCUMENTDB_DATABASE })
    # Create collection
    collection = client.CreateCollection(db['_self'],{ 'id': config.DOCUMENTDB_COLLECTION }, { 'offerType': 'S1' })
    # Create collection for latest entry

    collection = client.CreateCollection(db['_self'],{ 'id': config.DOCUMENTDB_COLLECTION_LATEST }, { 'offerType': 'S1' })

    #create initial document
    document = client.CreateDocument(collection['_self'],
        { #'id': config.DOCUMENTDB_DOCUMENT,
          'counter': 1,
          'inside': {
                    "temp" : 29.6,
                    "rel-humid": 0.47,
                    "abs-humid":13.96
                },
          'outside': {
                    "temp" : 32.6,
                    "rel-humid": 0.37,
                    "abs-humid":10.00
                },
          "fan": {
              "active": False,
              "override": False,
              "eco-mode": False
            }
          })

    document = client.CreateDocument(collection['_self'],
        { #'id': config.DOCUMENTDB_DOCUMENT,
          
          'counter': 2,
          'inside': {
                    "temp" : 30.6,
                    "rel-humid": 0.45,
                    "abs-humid":13.98
                },
          'outside': {
                    "temp" : 32.6,
                    "rel-humid": 0.37,
                    "abs-humid":10.00
                }
          ,
          "fan": {
              "active": False,
              "override": False,
              "eco-mode": False
            }
          })

    document = client.CreateDocument(collection['_self'],
        { #'id': config.DOCUMENTDB_DOCUMENT,
          
          'counter': 3,
          'inside': {
                    "temp" : 29.0,
                    "rel-humid": 0.50,
                    "abs-humid":13.90
                },
          'outside': {
                    "temp" : 32.6,
                    "rel-humid": 0.37,
                    "abs-humid":10.00
                },
          "fan": {
              "active": False,
              "override": False,
              "eco-mode": False
            }
          })

    document = client.CreateDocument(collection['_self'],
        { #'id': config.DOCUMENTDB_DOCUMENT,
          
          'counter': 4,
          'inside': {
                    "temp" : 29.1,
                    "rel-humid": 0.47,
                    "abs-humid":13.89
                },
          'outside': {
                    "temp" : 32.6,
                    "rel-humid": 0.37,
                    "abs-humid":10.00
                },
          "fan": {
              "active": False,
              "override": False,
              "eco-mode": False
            }
          })

    document = client.CreateDocument(collection['_self'],
        { #'id': config.DOCUMENTDB_DOCUMENT,
          
          'counter': 5,
          'inside': {
                   "temp" : 29.7,
                    "rel-humid": 0.47,
                    "abs-humid":13.89
                },
          'outside': {
                    "temp" : 32.6,
                    "rel-humid": 0.37,
                    "abs-humid":10.00
                },
          "fan": {
              "active": False,
              "override": False,
              "eco-mode": False
            }
          })

  
    document = client.CreateDocument(collection['_self'],
        { #'id': config.DOCUMENTDB_DOCUMENT,
          
          'counter': 6,
          'inside': {
                    "temp" : 29.5,
                    "rel-humid": 0.43,
                    "abs-humid":13.91
                },
          'outside': {
                    "temp" : 32.6,
                    "rel-humid": 0.37,
                    "abs-humid":10.03
                },
          "fan": {
              "active": False,
              "override": False,
              "eco-mode": False
            }
          })

    document = client.CreateDocument(collection['_self'],
        { #'id': config.DOCUMENTDB_DOCUMENT,
          
          'counter': 7,
          'inside': {
                    "temp" : 30.3,
                    "rel-humid": 0.42,
                    "abs-humid":13.91
                },
          'outside': {
                    "temp" : 32.7,
                    "rel-humid": 0.37,
                    "abs-humid": 11.00
                },
          "fan": {
              "active": False,
              "override": False,
              "eco-mode": False
            }
          })

    document = client.CreateDocument(collection['_self'],
        { #'id': config.DOCUMENTDB_DOCUMENT,
          
          'counter': 8,
          'inside': {
                    "temp" : 29.6,
                    "rel-humid": 0.43,
                    "abs-humid":13.91
                },
          'outside': {
                    "temp" : 32.6,
                    "rel-humid": 0.37,
                    "abs-humid":10.20
                },
          "fan": {
              "active": False,
              "override": False,
              "eco-mode": False
            }
          })

    document = client.CreateDocument(collection['_self'],
        { #'id': config.DOCUMENTDB_DOCUMENT,
          
          'counter': 9,
          'inside': {
                    "temp" : 29.3,
                    "rel-humid": 0.42,
                    "abs-humid":13.87
                },
          'outside': {
                    "temp" : 32.6,
                    "rel-humid": 0.37,
                    "abs-humid":10.10
                },
          "fan": {
              "active": False,
              "override": False,
              "eco-mode": False
            }
          })

    document = client.CreateDocument(collection['_self'],
        { #'id': config.DOCUMENTDB_DOCUMENT,
          
          'counter': 10,
          'inside': {
                    "temp" : 29.5,
                    "rel-humid": 0.43,
                    "abs-humid":13.91
                },
          'outside': {
                    "temp" : 32.8,
                    "rel-humid": 0.32,
                    "abs-humid":10.80
                },
          "fan": {
              "active": False,
              "override": False,
              "eco-mode": False
            }
          })


 

    return render_template('create.html',
        title='Create Page',
        year=datetime.now().year,
        message='You just created a new database, collection, and document.  Your old votes have been deleted')



@app.route("/latest")
def new():
   
    client = document_client.DocumentClient(config.DOCUMENTDB_HOST, {'masterKey': config.DOCUMENTDB_KEY})
    db = next((data for data in client.ReadDatabases() if data['id'] == config.DOCUMENTDB_DATABASE))

    coll = next((coll for coll in client.ReadCollections(db['_self']) if coll['id'] == config.DOCUMENTDB_COLLECTION_LATEST))

    query = list(client.QueryDocuments(coll['_self'],
            {
                'query': 'SELECT * FROM c'
            }))
      
    return json.dumps(query)
    
@app.route("/insert", methods=['GET', 'POST'])
def insert():

    client = document_client.DocumentClient(config.DOCUMENTDB_HOST, {'masterKey': config.DOCUMENTDB_KEY})
    db = next((data for data in client.ReadDatabases() if data['id'] == config.DOCUMENTDB_DATABASE))
    coll = next((coll for coll in client.ReadCollections(db['_self'])))

    temporaryJson = simplejson.loads(json.dumps(request.json))
    
    documents = list(client.QueryDocuments(coll['_self'],   {'query': 'SELECT * FROM c.counter'  }))
    #documents = documents[:2-1]
    #del documents[-2:]

    ints = map(int, simplejson.loads(json.dumps(documents)))

    temporaryJson['counter'] = max(ints) + 1
    temporaryJson['date'] = datetime.now().isoformat()

    created_document = client.CreateDocument(coll['_self'],temporaryJson)

    # add entry to collection latest
    
    #get collection
    coll_latest = next((coll for coll in client.ReadCollections(db['_self']) if coll['id'] == config.DOCUMENTDB_COLLECTION_LATEST))
    created_document = client.CreateDocument(coll_latest['_self'],temporaryJson)

    return render_template('index.html'), 200

@app.route("/fanOn")
def fanOn():

    p = pusher.Pusher(app_id='128311',
      key='873a24ad290781cb445c',
      secret='497979490241f4842d2d')

    p.trigger(u'ventilation_channel', u'v_on', {u'message' : u'v_on'})
    
    return render_template('index.html',
    message='fan is now on')

@app.route("/off")
def fanOff():

    p = pusher.Pusher(app_id='128311',
      key='873a24ad290781cb445c',
      secret='497979490241f4842d2d')
    
    p.trigger(u'ventilation_channel', u'off', {u'message' : u'off'})
    
    return render_template('index.html',
    message='fan is now off')

@app.route("/eOn")
def eOn():

    p = pusher.Pusher(app_id='128311',
      key='873a24ad290781cb445c',
      secret='497979490241f4842d2d')
    
    p.trigger(u'ventilation_channel', u'e_on', {u'message' : u'e_on'})
    
    return render_template('index.html',
    message='fan is now on economy mode')

@app.route("/eOff")
def eOff():

    p = pusher.Pusher(app_id='128311',
      key='873a24ad290781cb445c',
      secret='497979490241f4842d2d')
    
    p.trigger(u'ventilation_channel', u'e_on', {u'message' : u'e_off'})
    
    return render_template('index.html',
    message='fan is now off')

