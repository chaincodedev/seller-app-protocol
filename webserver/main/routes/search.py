from flask_expects_json import expects_json
from flask_restx import Namespace, Resource, reqparse
from jsonschema import validate

from main import constant
from main.repository.ack_response import get_ack_response
from main.utils.schema_utils import get_json_schema_for_given_path, get_json_schema_for_response

search_namespace = Namespace('search', description='Search Namespace')


@search_namespace.route("/v1/search")
class SearchCatalogues(Resource):
    path_schema = get_json_schema_for_given_path('/search')

    @expects_json(path_schema)
    def post(self):
        response_schema = get_json_schema_for_response('/search')
        resp = get_ack_response(ack=True)
        validate(resp, response_schema)

        # async operation to be done
        # 1. request to BPP client for search catalogs
        # 2. webhook hit(with search catalogs) to BAP protocol provided in context
        return resp
