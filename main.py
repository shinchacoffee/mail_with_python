import message_class
#import user_class
#import content_class
#import attachment_class
#import addressee_class
#import sender_class

my_new_message = message_class.Message()

#if input is only e-mail address then omitt construct_mail
#if my_new_message.status = "need more information" ...

my_new_message.constructMail()
my_new_message.sendMail()
