from datetime import timedelta
from functools import update_wrapper

from flask import Flask, jsonify
app = Flask(__name__)
verification_required = True

@app.route('/')
def f():
    return 'Raspberry Pi App running'

@app.route('/mode')
def get_status():
	# Return verify or photos
	resp = 'verify' if verification_required else 'photos'
    resp = jsonify(resp)
    resp.headers.add('Access-Control-Allow-Origin', '*')

	if verification_required:
		verification_required = False

	return resp

@app.route('/code')
def get_code():
	return '999 136'


@app.route('/get_images')
def get_images():
	sample_data = {
		'images': [
            {
                'img': 'https://i.pinimg.com/originals/62/20/d2/6220d255154fad0c911a3cb4c0072031.jpg'
			},
			{
                'img': 'https://i.pinimg.com/originals/8b/a1/01/8ba101bc0e6fb061e79bef8c7bac97cc.jpg'
			}
		]
    }

	return jsonify(sample_data)

if __name__ == '__main__':
	try:
		app.run(host='0.0.0.0', port=8080)
	except:
		app.run(port=8080)
