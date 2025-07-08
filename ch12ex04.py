#ch12ex04.py

class Attendee:
    def __init__(self, name, company, state, email):
        self._name = name
        self._company = company
        self._state = state
        self._email = email

    def __str__(self):
        return f"{self._name} {self._company} {self._state} {self._email}"

    def getState(self):
        return self._state

class Speaker(Attendee):
    def __init__(self, name, company, state, email, day, capacity, title):
        self._title = title
        self._day = day
        self._capacity = capacity
        Attendee.__init__(self, name, company, state, email)

    def __str__(self):
        return f'{self._name} presents "{self._title}" on Day {self._day}'
    
class Conference:
    def __init__(self):
        self._attendees = []

    def addAttendee(self, name, company, state, email):
        self._attendees.append(Attendee(name, company, state, email))

    def deleteAttendee(self):
        pass

    def listAttendees(self):
        for attendee in self._attendees:
            print(attendee)

    def listAttendeesByState(self, state):
        for attendee in self._attendees:
            if attendee.getState() == state:
                print(attendee)

    def addSpeaker(self, name, company, state, email, day, capacity, title):
        self._attendees.append(Speaker(name, company, state, email,
                                       day, capacity, title))

def main():
    myConference = Conference()
    file = open('attendees.csv')
    file.readline()
    for line in file:
        data = line.rstrip('\n').split(',')
        if data[4] == 'Yes':
            myConference.addSpeaker(data[0], data[1], data[2], data[3],
                                    data[5], data[6], data[7])
        else:
            myConference.addAttendee(data[0], data[1], data[2], data[3])
    file.close()
    
    print("\nAll Attendees:")
    myConference.listAttendees()
    print("\nAttendees from Maine:\n")
    myConference.listAttendeesByState("ME")


if __name__ == '__main__':
    main()

