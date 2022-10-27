import re
class User:

    def __init__(self):
        self.address = "default@gmail.com"
        self.password = "admin1"
        self.addr_state, self.pass_state = "default_mail", "default_pass"

    def get_address(self):
        #string = user_input()
        string = input('Please enter your e-mail address: ')
        mail_templ = r'\b[\w._+-]+@[\w.-]+\.[A-Za-z]{2,3}\b' #my version of regexp
                    #r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b' found on internet... : <
        if re.fullmatch(mail_templ, string):
            address = string
        else:
            print("Invalid e-mail address.")
            address = "asd@asd.asd"
        return address

    def get_password(self):
        #string = user_input()
        string = input('Please enter your e-mail password: ')
        return string

    def set_address(self, address):
        self.address = address

    def set_password(self, password):
        if password.is_string:
            self.password = password
        else:
            self.pass_state = "wrong_pass"
