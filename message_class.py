import user_class
#import content_class
#import attachment_class
#import addressee_class
#import sender_class

class Message:

    def __init__(self):
        self.senderMail = "nonusablemailacc@gmail.com"
        self.senderPass = "passwordfornonusbalemailacc" #should be somehow encrypted... or at least not in a git?
        self.receiverMail = "nonusablemailacc@gmail.com"
        self.content = "Please phone me as soon as possible."
        self.attachment = None
        self.status = "not sent"

    def constructMail(self):
        self.status = "constructed"

    def sendMail(self):
        self.status = "mail sent successfully"