import re
import check_mail
class User:

    def __init__(self):
        self.address = "default@gmail.com"
        self.password = "admin1"
        self.addr_state, self.pass_state = "default_mail", "default_pass"

    def get_address(self):
        string = input('Please enter your e-mail address: ')
        is_it_proper_mail = check_mail.MailChecker(string)
        if is_it_proper_mail.state:
            address = string
            address_state = "ok"
        else:
            print("Invalid e-mail address. Address set to None")
            address = None
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
