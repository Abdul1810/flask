from flask import Flask, render_template
from flask_restful import Api, Resource

from PIL import Image
import base64
import io

app = Flask(__name__)

img = Image.open("klaus.jpg")
data = io.BytesIO()
img.save(data, "JPEG")
encoded_img_data = base64.b64encode(data.getvalue())

@app.route('/')
def hello_world():
    return render_template("index.html", img_data=encoded_img_data.decode('utf-8'))

api = Api(app)

class Hello(Resource):
    def get(self):
        return { "res": encoded_img_data.decode('utf-8') }, 200

api.add_resource(Hello, '/api')

if __name__ == '__main__':
    app.run(debug=False, host="0.0.0.0")
