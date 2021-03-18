import selectors
import logging
from networking_object import NetworkingObject, AuthError, ParseError, ShutdownError, parse_msg, create_msg


class Host(NetworkingObject):
    def __init__(self, port, password):
        self.password = password
        self.host_ready = False
        self.client_ready = False
        self.go_flag = False

        self.sock.bind(('', port))  # Blank string for host allows it to connect externally

        self.startup()

    def startup(self):
        # Reinitialize buffers and authed, getting rid of any old, outdated messages and ensuring
        # the initial state of the connection
        self.authed = False
        self.host_ready = False
        self.client_ready = False
        self.go_flag = False
        self.input_buffer = ""
        self.output_buffer = []

        # Listen on socket
        logging.info("Host listening on socket...")
        self.sock.listen(1)
        connection, addr = self.sock.accept()
        connection.setblocking(False)
        self.sel.register(connection, selectors.EVENT_READ | selectors.EVENT_WRITE)
        logging.info("Host connected to %s", connection.getpeername())

    # Run externally to the object to control the loop's timing
    def io_loop(self):
        for key, mask in self.sel.select(timeout=1):
            logging.debug("Host is selecting...")
            connection = key.fileobj
            connection.setblocking(False)

            if self.client_ready and self.host_ready:
                self.add_to_output_buffer("command", "go")
                self.client_ready = False
                self.host_ready = False
                self.go_flag = True

            if mask and selectors.EVENT_WRITE and self.output_buffer:
                logging.debug("Host is outputting...")
                logging.debug("Current state of output_buffer: %s", self.output_buffer)
                i = 0
                for msg in self.output_buffer:
                    connection.sendall(msg)
                    logging.info("Host sent message %s", msg)
                    if self.go_flag:
                        logging.info("Host sent go command.")
                        self.go_flag = False
                        self.output_buffer.pop(i)
                        return True  # We're leaving stuff in the buffer, but it'll get picked up later
                    i += 1
                self.output_buffer.clear()

            if mask and selectors.EVENT_READ:
                logging.debug("Host is inputting...")
                logging.debug("Current state of input_buffer: %s", self.input_buffer)
                msgs = self.get_msg(connection)
                for category, msg in msgs:
                    logging.info("Host parsing message %s | %s", category, msg)
                    if not self.authed and category == "auth":
                        if msg == self.password:
                            logging.info("Host completed auth.")
                            self.authed = True
                            self.add_to_output_buffer("auth", "correct")
                        else:
                            logging.info("Host rejected auth.")
                            self.add_to_output_buffer("auth", "incorrect")
                    # Could be an elif, but this allows it to parse the next message in the same loop if authed earlier
                    if self.authed:
                        if category == "command" and msg == "ready":
                            logging.info("Host received client ready command.")
                            self.client_ready = True

    def ready(self):
        logging.info("Host is ready.")
        self.host_ready = True

