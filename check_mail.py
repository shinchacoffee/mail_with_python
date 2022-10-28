import re

class MailChecker:

    def __init__(self, address = "a@a.a"):
        self.mail_templ = r'\b[\w._+-]+@[\w.-]+\.[A-Za-z]{2,3}\b' #my version of regexp
                         #r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b' found on internet... : <
        self.state = re.fullmatch(self.mail_templ, address)