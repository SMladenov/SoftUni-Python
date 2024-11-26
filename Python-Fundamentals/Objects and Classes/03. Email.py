#Email

class Email:
    def __init__ (self, sender, receiver, content):
        self.sender = sender
        self.receiver = receiver
        self.content = content
        self.is_sent = False
    def send (self):
        self.is_sent = True
    def get_info (self):
        return f"{self.sender} says to {self.receiver}: {self.content}. Sent: {self.is_sent}"

listMails = []
cmd = input()

while cmd != "Stop":
    cmdSplit = cmd.split(' ')
    listMails.append(cmdSplit)
    cmd = input()

indexes = [int(i) for i in input().split(', ')]

for index, i in enumerate(listMails):
    sender = i[0]
    receiver = i[1]
    content = i[2]
    
    mail = Email(sender, receiver, content)

    if index in indexes:
        mail.send()

    print (f"{mail.get_info()}")