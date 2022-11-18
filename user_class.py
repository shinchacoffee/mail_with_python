import re
import check_mail
import check_pass
class User:

    def __init__(self, custom_address = False):
        if not custom_address:
            self.address = "nonusablemailacc@gmail.com"
            self.addr_state = True
            self.password = "passwordfornonusbalemailacc" #should be somehow encrypted... or at least not in a git?
            self.pass_state = True
        else:
            self.address, self.addr_state = self.get_address()
            self.password, self.pass_state = self.get_password()

    def get_address(self):
        string = input('Please enter your e-mail address: ')
        is_it_proper_mail = check_mail.MailChecker(string)
        if is_it_proper_mail.state:
            address = string
            address_state = True
        else:
            print("Invalid e-mail address. Address set to None")
            address = None
            address_state = False
        return address, address_state

    def get_password(self):
        string = input('Please enter your e-mail password: ')
        is_it_proper_pass = check_pass.PassChecker(string)
        if is_it_proper_pass:
            password = string
            password_state = True
        else:
            password = "pas"
            password_state = False
        return password, password_state