from flask import Flask, jsonify
from flask_restful import Resource, Api
from flask.ext.cors import CORS
from suggester import Suggester

WORD_LIST = 'wordlist.txt'

app = Flask(__name__)
CORS(app)
api = Api(app)
suggester = None

# Build a prefix tree for all words we have
def build_prefix_tree(wordlist):
    word_list = open(wordlist).read().splitlines()
    suggester = Suggester()
    suggester.update_trie(word_list)
    return suggester

class Suggestion(Resource):
    def get(self, prefix):
        results = []
        for item in suggester.search_prefix(prefix):
            results.append({'value': item})
        return jsonify(results)

api.add_resource(Suggestion, '/suggestion/<string:prefix>')

if __name__ == '__main__':
    suggester = build_prefix_tree(WORD_LIST)
    app.run()