from flask import Flask
import datetime
import socket

app = Flask(__name__)

@app.route('/api/v1/details', methods=['GET'])
def get_details():
    return {"time": datetime.datetime.today().strftime('%Y-%m-%d %H:%M:%S'),
            "hostname": socket.gethostname()
            }

@app.route('/api/v1/healthz', methods=['GET'])
def health_check():
    return {"status": "OK"}, 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

# '/api/v1/detais'
# '/api/v1/healthz'