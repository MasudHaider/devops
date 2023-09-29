from flask import Flask, jsonify, request
import time

app = Flask(__name__)

time.sleep(2)
log_file = 'D:/SWC/DevOps/hgmdha/ex1/service2/logs/service2.log'
log_file = ''


@app.route('/', methods=['POST'])
def receive_message():
    incoming_message = request.data.decode('utf-8')
    
    if incoming_message == "STOP":
       shutdown_server()
       return

    local_address = request.host
    remote_address = f"{request.remote_addr}:{request.environ.get('REMOTE_PORT')}"

    # log entry for service2.log
    full_log_message = f"{incoming_message} {local_address} {remote_address}"


    # write to service2.log
    with open('D:/SWC/DevOps/hgmdha/ex1/service2/logs/service2.log', 'a') as log_file: 
        log_file.write(full_log_message + "\n")

    if incoming_message == "STOP":
        shutdown_server()
    
    return jsonify({"address": local_address})


def shutdown_server():
    """Helper function to shut down the Flask server."""
    func = request.environ.get('werkzeug.server.shutdown')
    if func is None:
        raise RuntimeError('Not running with the Werkzeug Server')
    func()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)