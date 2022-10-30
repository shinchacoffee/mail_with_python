class Attachment:

    def __init__(self):
        self.file = "file.file"
        self.attachment_state = "no file"

    def get_file(self):
        # string = user_input()
        string = input("Please give file path for attachment: ")
        return string, "ok"

    def set_paths(self, address):
        self.file = address(0)
        self.attachment_state = address(1)