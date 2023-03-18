class Attendee:
    def __init__(self,name,company,country,email):
        self.name = name
        self.company = company
        self.country = country
        self.email = email
    def getInfo(self):
        return {"Name":self.name, "Company":self.company, "Country":self.country,"Email":self.email}



class Conference:
    def __init__(self,name,location,dates):
        self.name = name
        self.location = location
        self.dates = dates
        self.attendees = []
        print("Conference \"" + self.name +  "\" is created.")

    def addAttendee(self,attendee):
        self.attendees.append(attendee)
        print("Attendee " + attendee.name + " is added to the list of conference participants.")

    def removeAttendee(self, attendee):
        if attendee in self.attendees:
            self.attendees.remove(attendee)
            print("Attendee " + attendee.name + "is removed from the list of conference participants.")
        else:
            print("There is noone named as" + attendee.name)

    def displayAttendees(self):
        print('-'*80)
        print("Name\t" + "\t\t Company \t\t"+ "\t\t Country \t\t"+ "\t\t Email \t\t")
        print('-'*80)
        for attendee in self.attendees:
            print(attendee.name, end = '\t\t\t')
            print(attendee.company, end = '\t\t\t\t ')
            print(attendee.country, end = '\t\t\t\t')
            print(attendee.email, end = '\n')
    
    def checkAttendee(self,name):
        for attendee in self.attendees:
            if attendee.name == name:
                print(f"{name} is attending the conference.")
        else:
            print(f"{name} is not attending the conference.")

    def displayAttendeesFromCountry(self,country):
        print('-'*80)
        print("Name\t" + "\t\t Company \t\t"+ "\t\t Country \t\t"+ "\t\t Email \t\t")
        print('-'*80)
        for attendee in self.attendees:
            if attendee.country == country:
                
                print(attendee.name, end = '\t\t\t')
                print(attendee.company, end = '\t\t\t\t ')
                print(attendee.country, end = '\t\t\t\t')
                print(attendee.email, end = '\n')
        

        
        


def main(filename):
    conference1 = Conference("National conference on computing", "Seoul", "22-25 December, 2020")
    for line in open(filename):
        parts = line.split(", ")
        attendee = Attendee(parts[0], parts[1], parts[2], parts[3].strip())
        conference1.addAttendee(attendee)
    conference1.displayAttendees()
    attendee = Attendee("Gerald", "D&G", "USA", "gerald@mail.com")

    print("Gerald Info: ", attendee.getInfo())
    print(conference1.checkAttendee("Gerald"))
    print(conference1.removeAttendee(attendee))

    conference1.displayAttendees()
    print(conference1.checkAttendee("Lisa"))

    print("\nDisplaying attendees from Estonia:")
    conference1.displayAttendeesFromCountry("Estonia")

main("attendees.txt")