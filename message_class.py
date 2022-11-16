import user_class
import check_mail
#import content_class
#import attachment_class
#import addressee_class
#import sender_class

class Message:

    def __init__(self, mail_order):
        self.senderMail = "nonusablemailacc@gmail.com"
        self.senderPass = "passwordfornonusbalemailacc" #should be somehow encrypted... or at least not in a git?
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
        self.status = "constructed"

    def sendMail(self):
        self.status = "mail sent successfully"