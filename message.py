"""
This is the message module and supports all the REST actions for the
message collection
"""

# System modules
from datetime import datetime

# 3rd party modules
from flask import make_response, abort


def get_timestamp():
    return datetime.now().strftime(("%Y-%m-%d %H:%M:%S"))


# Data to serve with our API
MESSAGE = {
    1: {
        "message": "Hi,                 Note: This is default Messge",
        "id": 1,
        "timestamp": get_timestamp(),
    },
    2: {
        "message": "Hello,              Note: This is default Messge",
        "id": 2,
        "timestamp": get_timestamp(),
    }
}


def read_all():
    """
    This function responds to a request for /api/message
    with the complete lists of message
    :return:        json string of list of message
    """
    # Create the list of message from our data (static)
    return [MESSAGE[key] for key in sorted(MESSAGE.keys())]


def read_one(id):
    """
    This function responds to a request for /api/message/{id}
    with one matching id from message
    :param id:   id of message to find
    :return:        message matching id
    """
    # Does the id exist in message?
    if id in MESSAGE:
        message = MESSAGE.get(id)

    # otherwise, nope, not found
    else:
        abort(
            404, "Message with id {id} not found".format(id=id)
        )

    return message


def create(messages):
    """
    This function creates a new message in the message structure
    based on the passed in message data
    :param messages:  message to create in message structure
    :return:        201 on success, 406 on message exists
    """
    id = messages.get("id", None)
    message = messages.get("message", None)

    # Does the message exist already?
    if id not in MESSAGE and id is not None:
        MESSAGE[id] = {
            "id": id,
            "message": message,
            "timestamp": get_timestamp(),
        }
        post_message = { "message": "I received your message, I will reply when I can" }

        # return MESSAGE[id], 201
        return post_message, 201


    # Otherwise, they exist, that's an error
    else:
        abort(
            406,
            "Message with id {id} already exists".format(id=id),
        )
