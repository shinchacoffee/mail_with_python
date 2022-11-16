import re
import check_mail
class User:

    def __init__(self, custom_address = False):
        if not custom_address:
            self.address = "nonusablemailacc@gmail.com"
            self.password = "passwordfornonusbalemailacc" #should be somehow encrypted... or at least not in a git?
        else:
            self.address, self.addr_state = self.get_address()
            self.password, self.pass_state = self.get_password()

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
        string = input('Please enter your e-mail password: ')
        return string, "ok"
