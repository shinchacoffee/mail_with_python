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
            address_state = "ok"
        else:
            print("Invalid e-mail address. Address set to asd@asd.asd")
            address = "asd@asd.asd"
            address_state = "wrong mail"
        return address, address_state

    def get_password(self):
        #string = user_input()
        string = input('Please enter your e-mail password: ')
        return string

    def set_address(self, address):
        self.address = address(0)
        self.addr_state = address(1)

    def set_password(self, password):
        if password.is_string:
            self.password = password
            self.pass_state = "ok"
        else:
            self.pass_state = "wrong pass"
