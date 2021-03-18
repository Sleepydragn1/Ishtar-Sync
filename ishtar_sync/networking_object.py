import socket
import selectors


# Assumes message is already decoded
def parse_msg(msg):
    if msg[0] == "a":
        return "auth", msg[1:]  # Removes first character (category)
    elif msg[0] == "c":
        return "command", msg[1:]
    elif msg[0] == "e":
        return "error", msg[1:]
    else:
        raise ParseError("Parsed message with wrongful category")


def create_msg(category, msg):
    created_msg = ""
    if category == "auth":
        created_msg += "a"
    elif category == "command":
        created_msg += "c"
    elif category == "error":
        created_msg += "e"
    else:
        # Should be uncaught since I shouldn't be creating messages with wrongful categories
        raise ParseError("Created message with wrongful category")

    return (created_msg + msg + "|").encode()


class NetworkingObject:
    sel = selectors.DefaultSelector()
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    input_buffer = ""
    output_buffer = []
    authed = False

    def get_msg(self, connection):
        try:
            data = connection.recv(256)
            if data:
                self.input_buffer += data.decode()

                terminator_index = self.input_buffer.find("|")
                output = []
                while terminator_index != -1:
                    try:
                        output.append(parse_msg(self.input_buffer[0:terminator_index]))  # Get msg, add to output
                    except ParseError:
                        # Ignore message if it cannot be parsed
                        pass

                    self.input_buffer = self.input_buffer[terminator_index + 1:]  # Remove msg + terminator from buffer
                    terminator_index = self.input_buffer.find("|")

                return output
            # Empty data means the connection was closed
            else:
                self.close_connection(connection)
                return [False]
        except socket.error as e:
            # TODO: Better error handling, with more specific errors
            # Allows it to skip .recv() if it'll block
            # Empty string won't trigger the for statement
            return ""

    def add_to_output_buffer(self, category, msg):
        self.output_buffer.append(create_msg(category, msg))

    def close_connection(self, connection):
        self.sel.unregister(connection)
        connection.close()  # TODO: Check if this closes self.sock too, because that'd be a problem
        raise ShutdownError

    def cleanup(self):
        self.sel.close()
        self.sock.close()


class AuthError(Exception):
    pass


class ParseError(Exception):
    pass


class ShutdownError(Exception):
    pass
