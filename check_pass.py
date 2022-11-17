import re

class PassChecker:

    def __init__(self, password = "pas"):
        self.mail_templ = r'\b[\w!@#$%^&*()._+-]{4,}\b' #my version of regexp im not sure of...
                         #r'[A-Za-z0-9@#$%^&+=]{8,}' found on internet... : <
        self.state = re.fullmatch(self.mail_templ, password)