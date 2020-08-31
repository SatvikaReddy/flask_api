from flask_restful import Resource,reqparse
from flask_jwt_extended import jwt_required,get_jwt_claims
from db import query

class Routes(Resource):
    @jwt_required
    def get(self):
        # vendorid=get_jwt_claims()['vendorid']
        try:
            return query(f"""SELECT * FROM gpstrackerdb.Routes;""",return_json=False),200
        except:
            return {"message": "An error occurred while accessing Routes table."},500