#! /usr/bin/env python3
from flask import Flask, request
from flask_restful import Resource, Api
from flask_jwt import JWT, jwt_required

from security import authenticate, identity


app = Flask(__name__)
app.secret_key = "MyVerySecretAPKey"
api = Api(app)

jwt = JWT(app, authenticate, identity)  # /auth

reparacoes = [{'id': 1234, 'nome': 'josé manuel da silva pancrácio'}]


class Repairs(Resource):
    def get(self):
        return reparacoes


class Repair(Resource):
    @jwt_required()
    def get(self, num_rep=None):
        if num_rep is None:
            return {'repair': None}, 404
        reparacao = next(filter(lambda x: x['id'] == int(num_rep), reparacoes), None)
        return {'repair': reparacao}, 200 if reparacao else 404

    # create new. if already exists will fail.
    def post(self, num_rep):
        if next(filter(lambda x: x['id'] == int(num_rep), reparacoes), None) is not None:
            return {'message': "Repair already exists!"}, 400  # BAD REQUEST

        data = request.get_json()
        rep_name = num_rep
        rep = {'name:': rep_name, 'num': 123}
        reparacoes.append(rep)
        return rep

    def del_(self):
        pass

    # create new or update an existing one.
    def put(self):
        pass


class Root(Resource):
    def get(self):
        return {'app': 'The amazing NPK Service Web API!'}


class Contacts(Resource):
    def get(self):
        return {'lista_contactos': []}


class Contact(Resource):
    def get(self, nome):
        return {'contacto': nome}

    def post(self):
        pass

    def del_(self):
        pass

    def put(self):
        pass


api.add_resource(Repairs, '/repairs')
api.add_resource(Repair, '/repair', '/repair/<string:num_rep>')

api.add_resource(Contacts, '/contacts')
api.add_resource(Contact, '/contact/<string:nome>')

api.add_resource(Root, '/')


app.run(port=5000, threaded=False)
