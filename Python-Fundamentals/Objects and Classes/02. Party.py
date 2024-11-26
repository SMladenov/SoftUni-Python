#Party

class Party:
    def __init__(self):
        self.people = []

partyList = Party()

cmd = input()

while cmd != "End":
    partyList.people.append(cmd)
    cmd = input()

print (f"Going: {', '.join(partyList.people)}\nTotal: {len(partyList.people)}")