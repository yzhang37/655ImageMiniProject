import { io, Socket } from 'socket.io-client';


class SocketioService {
    _socket: Socket | undefined;

    setupSocketConnection() {
        if (this._socket === undefined) {
            this._socket = io();
        }
    }

    get Socket(): Socket {
        this.setupSocketConnection();
        return (this._socket as Socket);
    }

    disconnect() {
        if (this._socket !== undefined) {
            this._socket.disconnect();
        }
    }
}

export default new SocketioService();
