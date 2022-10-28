import re

class Addressee:

    def __init__(self):
        self.address = "none"
        self.addr_state = "no mail"

    def get_address(self):
        #string = user_input()
        string = input('Please enter your e-mail address: ')
        state_of_mail = MailChecker(string)

        #it is red-lighting my MailChecker class... not sure why : <

        if state_of_mail:
            address = string
            address_state = "ok"
        else:
            print("Invalid e-mail address. Address set to asd@asd.asd")
            address = "asd@asd.asd"
            address_state = "wrong mail"
        return address, address_state

    def set_address(self, address):
        self.address = address(0)
        self.addr_state = address(1)