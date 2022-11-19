import user_class
import check_mail
#import content_class
#import attachment_class
#import addressee_class
#import sender_class

class Message:

    def __init__(self, mail_order):

        userData = user_class.User()
        if userData.addr_state and userData.pass_state:
            self.senderMail = userData.address
            self.senderPass = userData.password
            self.user_data_state = True
        else:
            userData.get_address()
            userData.get_password()
            self.senderMail = userData.address
            self.senderPass = userData.password
            if userData.addr_state and userData.pass_state:  # not sure if this is the way since also methods get_. also return values
                print("User data set properly")
                self.user_data_state = True
            else:
                print("User mail or password are not a proper ones.")  # probably want to end here a script or go to exception or sth
                self.user_data_state = False

        self.is_it_only_mail = check_mail.MailChecker(mail_order)
        if self.is_it_only_mail:
            self.receiverMail = mail_order
            self.content = "Please phone me as soon as possible."
            self.attachment = None
            self.status = "ready to send"
        else:
            self.receiverMail = None
            self.content = None
            self.attachment = None
            self.status = "custom order"

    def constructMail(self):

        if not self.user_data_state:
            userData = user_class.User()
            userData.get_address()
            userData.get_password()
            self.senderMail = userData.address
            self.senderPass = userData.password
            if userData.addr_state and userData.pass_state:  # not sure if this is the way since also methods get_. also return values
                print("User data set properly")
                self.user_data_state = True
            else:
                print(
                    "User mail or password are not a proper ones.")  # probably want to end here a script or go to exception or sth
                self.user_data_state = False #it should contain some error break or exception... so not to loop or do in vain

        string = input("Enter the message content")
        self.content = string
        print("Mail properly constructed")
        self.status = "constructed"

    def sendMail(self):
        print("Mail sent successfully")
        self.status = "mail sent successfully"