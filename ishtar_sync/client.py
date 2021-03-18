import selectors
import logging
from networking_object import NetworkingObject, AuthError, create_msg


class Client(NetworkingObject):
    def __init__(self, addr, port, password):
        self.startup(addr, port, password)

    def startup(self, addr, port, password):
        # Reinitialize buffers and set blocking to True, getting rid of any old, outdated messages and ensuring
        # the initial state of the connection
        self.sock.setblocking(True)
        self.input_buffer = ""
        self.output_buffer = [create_msg("auth", password)]

        logging.info("Client attempting to connect to %s:%s", addr, port)
        self.sock.connect((addr, port))
        self.sock.setblocking(False)
        self.sel.register(self.sock, selectors.EVENT_READ | selectors.EVENT_WRITE)
        logging.info("Client connected.")

    # Run externally to the object to control the loop's timing
    def io_loop(self):
        for key, mask in self.sel.select(timeout=1):
            connection = key.fileobj

            if mask and selectors.EVENT_WRITE and self.output_buffer:
                logging.debug("Client is outputting...")
                logging.debug("Current state of output_buffer: %s", self.output_buffer)
                for msg in self.output_buffer:
                    logging.debug("1")
                    connection.sendall(msg)
                    logging.info("Client sent message %s", msg)
                self.output_buffer.clear()

            if mask and selectors.EVENT_READ:
                logging.debug("Client is inputting...")
                logging.debug("Current state of input_buffer: %s", self.input_buffer)
                msgs = self.get_msg(connection)
                for category, msg in msgs:
                    logging.info("Client reading message %s | %s", category, msgs)
                    if not self.authed and category == "auth":
                        if msg == "correct":
                            logging.info("Client auth succeeded!")
                            self.authed = True
                        elif msg == "incorrect":
                            logging.info("Client auth failed.")
                            raise AuthError
                    if self.authed:
                        if category == "command" and msg == "go":
                            logging.info("Client received go command.")
                            return True

    def ready(self):
        logging.info("Client is ready.")
        self.add_to_output_buffer("command", "ready")
