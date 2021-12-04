import uuid
import os
from flask import Flask, request, abort, send_file
from base58 import b58encode
from errors import ApiTaskFailNoFileField, ApiTaskFailFileIsEmpty

from util import fail_result, success_result, ensure_path

FLICKR_ALPHABET = b'123456789abcdefghijkmnopqrstuvwxyzABCDEFGHJKLMNPQRSTUVWXYZ'


app = Flask(__name__)
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
    temp_dir = ensure_path('temp')
    return os.path.join(temp_dir, filename)


@app.route('/img/<task_id>', methods=["GET"])
def access_temp_img(task_id: str):
    temp_dir = ensure_path('temp')
    file_path = os.path.join(temp_dir, task_id)
    if os.path.exists(file_path) and os.path.isfile(file_path):
        return send_file(file_path, task_id)
    else:
        abort(404)


if __name__ == '__main__':
    print(__name__)
    app.run(host="0.0.0.0", port=8088, debug=True)

