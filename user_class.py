import check_mail
import check_pass
class User:

    def __init__(self, custom_address = False):
        userdatafile = open(".usermaildata", "r")
        if not custom_address:
            self.address = userdatafile.readline()
            self.addr_state = True
            self.password = userdatafile.readline() #should be somehow encrypted?
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
            password = None
            password_state = False
        return password, password_state