import hashlib
from flask import Flask, request, jsonify, Response

app = Flask(__name__)

hash_values = {}

@app.route('/messages', methods=['POST'])
def messages():
    """ messages route endpoint
        - - -
        post:
            description: Post string messages data
            :data
                description: dict of message
                schema:
                    {
                        "message": "foo"
                    }
            :return
                200:
                    description: dict of digest of message to be returned
                    schema:
                    {
                        "digest": "2c26b46b68ffc68ff99b453c1d30413413422d706483bfa0f98a5e886266e7ae"
                    }
    """
    req_data = request.get_json()
    messages = req_data['message']

    hash_object = hashlib.sha256(messages.encode('utf-8',errors = 'strict'))
    hex_dig = hash_object.hexdigest()

    hash_values[hex_dig] = messages

    return jsonify({'digest': hex_dig})


@app.route('/messages/<shadig>', methods=['GET'])
def messages_sha(shadig):
    """ messages sha digest endpoint
        - - -
        get:
            description: query original message with sha digest
            :parameter
                description: value digest of the message
            :return
                200:
                    description: dict of original message
                    schema:
                    {
                        "message": "foo"
                    }
                404:
                    description: error message
                    schema:
                    {
                        "err_msg": "Message not found"
                    }
    """

    if shadig in hash_values:
        return jsonify({'message': hash_values[shadig]})
    else:
        return jsonify({'err_msg': 'Message not found'}), 404


if __name__ == '__main__':
    app.run(host='0.0.0.0')
