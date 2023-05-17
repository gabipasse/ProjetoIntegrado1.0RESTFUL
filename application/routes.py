from bson import json_util
from flask_restful import Resource
import json
import base64

from application import app, api, CarbonFree


class checarDados(Resource):
    def get(self):

        dadosRetornar = []

        for areaDado in CarbonFree.VistoriaDados.find({}):

            for key, value in areaDado["geoData"].items():
                dadosRetornar.append({key: str(value)})

            with open(os.environ.get('PATH_BOT') + areaDado["pathJPG"],
                      'rb') as file:

                jpg_bytes = file.read()

            base64_encoded_bytes = base64.b64encode(jpg_bytes).decode('utf-8')

            dadosRetornar.append({"jpgImg": base64_encoded_bytes})

        return json.loads(json_util.dumps(dadosRetornar))


class checarUsuarios(Resource):
    def get(self):
        dadosRetornar = []

        for usuarioDado in CarbonFree.UsuariosQR.find({}):
            dadosRetornar.append(usuarioDado)

        return json.loads(json_util.dumps(dadosRetornar))
    

api.add_resource(checarDados, "/checarDados")

api.add_resource(checarUsuarios, "/checarUsuarios")


@app.route('/')
def hello_world():

    return "Use /checarDados or /checarUsuarios!"
