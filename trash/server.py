from flask import Flask, render_template

from trash.server_socket import socket_io


def create_server():
    server = Flask(__name__)

    server.config["SECRET_KEY"] = "123"

    @server.route('/')
    def index():
        return render_template("newgame.html")

    socket_io.init_app(server)

    return server
