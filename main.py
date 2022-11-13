import message_class
#import user_class
#import content_class
#import attachment_class
#import addressee_class
#import sender_class

mail_order = input('Enter target e-mail for default message or e-mail+ for custom one: ')

my_new_message = message_class.Message(mail_order)

if my_new_message.status == "remake": #maybe it can be implemented in terms of exceptions?
    my_new_message.constructMail()

if my_new_message.status == "ready to send":
    my_new_message.sendMail()