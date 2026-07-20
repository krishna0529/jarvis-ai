class CommandParser:

    def parse(self, text):

        words = text.split()

        return {
            "command": words[0] if words else "",
            "arguments": words[1:]
        }