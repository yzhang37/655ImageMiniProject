import uuid
import os
import argparse
from flask import Flask, request, abort, send_file
from base58 import b58encode

from errors import ApiTaskFailNoFileField, ApiTaskFailFileIsEmpty
from util import fail_result, success_result, ensure_path

FLICKR_ALPHABET = b'123456789abcdefghijkmnopqrstuvwxyzABCDEFGHJKLMNPQRSTUVWXYZ'

# parse command line options before launching.
parser = argparse.ArgumentParser(description='CS655 Image Recognition Daemon')
parser.add_argument("--hostname", "-i", type=str, default="0.0.0.0",
                    help="Setting the hostname running the server")
parser.add_argument("--port", "-p", type=int, default=80, help="Setting the server port")
parser.add_argument("--debug", "-g", action="store_true", default=False,
                    help="Whether to use debug mode.")
parser.add_argument("--dir-temp", dest="temp", type=str, default="temp", help="Store temporary files in a directory")

command_line_args = parser.parse_args()
# 运行后端服务器所需的变量
backend_server_hostname = command_line_args.hostname
backend_server_port = command_line_args.port
backend_server_use_debug = command_line_args.debug
temp_image_dir = command_line_args.temp

app = Flask(__name__)
# random choose a system generated number as secret key.
app.secret_key = os.urandom(16)


@app.route('/api/task', methods=["POST", "OPTIONS"])
def handle_picture():
    if request.method == 'POST':
        # 读取 forms 中的 file 数据，并进行存储
        if 'file' not in request.files:
            return fail_result(ApiTaskFailNoFileField)

        file = request.files['file']
        # 如果用户没有选择文件，浏览器将提交一个没有文件名的空 file。
        if file.filename == "":
            return fail_result(ApiTaskFailFileIsEmpty)

        # 生成一个任务 id，供前端使用
        uuid_byte = uuid.uuid4().bytes
        short_uuid = b58encode(uuid_byte, FLICKR_ALPHABET)
        str_uuid = short_uuid.decode()

        # 这一步要保存文件
        file.save(get_temp_name(str_uuid))

        # 最后，返回任务 id 给前端
        return success_result(task_id=str_uuid)

    elif request.method == 'OPTIONS':
        return """Usage:
  Upload a new picture (to submit an image recognition task). Manager will return a task id from the front end.
- METHOD: POST
- Parameter Format: Form data/FILE
- Return Format: JSON
- Return Data: { "task_id": <task_id, type: string, format: base58 of an random generated uuid> }
"""


def get_temp_name(filename: str):
    ok_temp_dir = ensure_path(temp_image_dir)
    return os.path.join(ok_temp_dir, filename)


@app.route('/upload/<task_id>', methods=["GET"])
def access_temp_img(task_id: str):
    file_path = get_temp_name(task_id)
    if os.path.exists(file_path) and os.path.isfile(file_path):
        return send_file(file_path, task_id)
    else:
        abort(404)


@app.route('/', defaults={'path': 'index.html'})
@app.route('/<path:path>', methods=["GET"])
def frontend(path: str):
    return app.send_static_file(path)


def run_backend_server():
    print(f"!!! Server run on {backend_server_hostname}:{backend_server_port}{', as debug mode' if backend_server_use_debug else ''}")
    print(f"!!! Directory used to store files is '{temp_image_dir}'")
    app.run(host=backend_server_hostname, port=backend_server_port, debug=backend_server_use_debug)


if __name__ == '__main__':
    run_backend_server()
