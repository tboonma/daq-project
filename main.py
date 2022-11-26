import sys
import os
from flask_cors import CORS

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
    from flask import render_template
except ModuleNotFoundError:
    print("Please install all required packages by running:"
          " pip install -r requirements.txt")
    sys.exit(1)

from openapi_server import encoder

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
