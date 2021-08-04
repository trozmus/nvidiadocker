import argparse
from flask import Flask, jsonify, request
from flask import render_template, send_from_directory
import os
import re
#import joblib
import socket
import json
from datetime import datetime
import torch





app = Flask(__name__)

@app.route('/', methods=['GET'])
def main():
    now = datetime.now()
    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
    try: 
        if not torch.cuda.is_available():
            msg =  "Cuda is available"
            device_id = torch.cuda.current_device()
            gpu_properties = torch.cuda.get_device_properties(device_id)
            noCuda = torch.cuda.device_count()
    except:    
        return jsonify(msg = 'Hello World', status = 'OK', dataAndTime = dt_string, message = msg)


    return jsonify(msg = 'Hello World', status = 'OK', dataAndTime = dt_string, message = msg, device=device_id, noCuda=noCuda)


if __name__ == '__main__':

    ## parse arguments for debug mode
    ap = argparse.ArgumentParser()
    ap.add_argument("-d", "--debug", action="store_true", help="debug flask")
    args = vars(ap.parse_args())

    if args["debug"]:
        app.run(debug=True, port=8080)
    else:
        app.run(host='0.0.0.0', threaded=True ,port=8080)


''' 
          gpu_properties.name,
          gpu_properties.major,
          gpu_properties.minor,
          gpu_properties.total_memory / 1e9))
'''

