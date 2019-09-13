# coding=utf-8

# Third-party Imports
from flask      import Flask, jsonify, request
from flask_cors import CORS

# Custom Imports
from .entities.entity import Session, engine, Base
from .entities.plugin import Plugin, PluginSchema

# Init flask
app = Flask(__name__)
CORS(app)

# Generate DB Schema
Base.metadata.create_all(engine)

# Start Session
session = Session()

# Routing

# GET plugins
@app.route('/')
@app.route('/plugins')
def getPlugins():
    # fetch from DB
    session = Session()

    pluginObjects = session.query(Plugin).all()

    # JSONify
    schema = PluginSchema(many=True)
    plugins = schema.dump(pluginObjects)

    # Serialize
    session.close()
    return jsonify(plugins)

# POST Request
@app.route('/plugins', methods=['POST'])
def addPlugin():
    # mount object
    postedPlugin = PluginSchema(only=('title', 'description'))\
        .load(request.get_json())

    plugin = Plugin(**postedPlugin.data, created_by="HTTP POST Request")

    # persistance
    session = Session()

    session.add(plugin)
    session.commit()

    # return created plugin
    newPlugin = PluginSchema().dump(plugin).data
    session.close()

    return jsonify(newPlugin), 201


# ./Routing