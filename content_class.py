class Content:

    def __init__(self):
        self.message_content = ""
        self.ending = ""
        self.message_state = "wrong message"

    def get_message(self):
        string = input('Please enter message you want to send: ')
        self.message_content = string
        self.message_state = "ok"

    def set_message(self):
        return self.message_content + self.ending