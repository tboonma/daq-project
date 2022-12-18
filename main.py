import sys
import os

if not os.path.exists("config.py"):
    print("Configuration 'config.py' not found.  "
          "You may create one from 'config.py.example'.")
    sys.exit(1)

from config import OPENAPI_STUB_DIR

if not os.path.exists(OPENAPI_STUB_DIR):
    print(f"Folder '{OPENAPI_STUB_DIR}' not found.  "
          "Please create the folder and extract zip file "
          "generated by openapi-generator into it.")
    sys.exit(1)

sys.path.append(OPENAPI_STUB_DIR)

try:
    import connexion
    from flask import render_template, request, jsonify
    from flask_cors import CORS
    from ariadne import load_schema_from_path, make_executable_schema, \
    graphql_sync, QueryType
    from ariadne.constants import PLAYGROUND_HTML
except ModuleNotFoundError:
    print("Please install all required packages by running:"
          " pip install -r requirements.txt")
    sys.exit(1)

from openapi_server import encoder
query = QueryType()
app = connexion.FlaskApp(__name__, specification_dir='./', server_args={'static_folder': './clientside/build/static', 'template_folder': './clientside/build'})
flask_app = app.app
CORS(flask_app, resources={r"/*": {"origins": "*"}})
flask_app.json_encoder = encoder.JSONEncoder
app.add_api('openapi/talai-api.yaml',
            arguments={'title': 'KU Talai API'},
            pythonic_params=True)

@flask_app.route('/', defaults={'path': ''})
@flask_app.route('/<path:path>')
def serve(path):
    if path != "" and os.path.exists(flask_app.static_folder + '/' + path):
        return render_template(flask_app.static_folder + '/' + path)
    else:
        return render_template('index.html')

type_defs = load_schema_from_path("schema.graphql")
schema = make_executable_schema(
    type_defs, query
)

@flask_app.route("/graphql", methods=["GET"])
def graphql_playground():
    return PLAYGROUND_HTML, 200

@flask_app.route("/graphql", methods=["POST"])
def graphql_server():
    data = request.get_json()
    success, result = graphql_sync(
        schema,
        data,
        context_value=request,
        debug=app.debug
    )
    status_code = 200 if success else 400
    return jsonify(result), status_code
