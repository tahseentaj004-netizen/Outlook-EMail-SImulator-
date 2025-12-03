#################################################################################################
### COMP1811 - CW1 Outlook Simulator                                                          ###
###            Mail Class                                                             ###
### The Mail class represents a single email within the Outlook Simulator. 
### It stores all information related to an email, including:
### a unique message ID (m_id)
### sender and receiver addresses (frm, to)
### the date and subject of the email
### the folder the email is stored in (tag)
### the body/content of the message
### whether the email has been read or not (read flag)
### whether the email is marked as important (flag)
###
### The class provides property methods to access or update these values safely,
### and includes show_email() and __str__() to display the email in readable formats.
### Overall, this class acts as a structured data model for an email inside the simulator.
# ### Partner A:                                                                                ###
###            <Tahseen Taj>, SID<001494074>                              ###
### Partner B:                                                                                ###
###            <Samira Ozturk>, SID<001464034-1>                              ###
#################################################################################################

# DO NOT CHANGE CLASS OR METHOD NAMES
# replace "pass" with your own code as specified in the CW spec.

class Mail:
    """Taking mail class to enter id,from,to,date,subject,tag,body """
    # DO NOT CHANGE CLASS OR METHOD NAMES
    def  __init__(self,m_id,frm,to,date,subject,tag,body):
        self._m_id = int(m_id)
        self._frm = frm
        self._to = to
        self._subject = subject
        self._date = date
        self._tag = tag      # reference to Outlook mail folder email is stored in
                             # e.g. tag0 = inbox, tag1 = bin, tag2 = private, tag3 = bank_acct, tag4 = COMP1811, etc.
        self._body = body
        self._flag = False   # Boolean indicating whether email is important
        self._read = False   # Boolean indicating whether the email is read or not.

    # Format should be done from pretty print.
    def __str__(self):
        return f"m_id:{self.m_id}\tfrom:{self.frm}\t|{self.to}\t|{self.date}|{self.subject}|{self.tag}|{self.read}|{self.flag}"

    @property
    def m_id(self):
        return self._m_id

    @property
    def frm(self):
        return self._frm

    @property
    def to(self):
        return self._to

    @property
    def date(self):
        return self._date


    @property
    def body(self):
        return self._body


    @body.setter
    def body(self, value):
        self._body = value

    @property
    def subject(self):
        return self._subject

    @property
    def tag(self):
        return self._tag

    @property
    def read(self):
        return self._read

    @property
    def flag(self):
        return self._flag

    @tag.setter
    # Pre: value in tags.
    def tag(self, value):
        self._tag = value

    @read.setter
    def read(self,value):
        self._read = value

    @flag.setter
    def flag(self,value):
        self._flag = value

# FEATURES A (Partner A)
    # FEATURES A (Partner A)
    # FEATURE A2 display attributes, sets e
    # returns the formated string for late
    # Opens email feature.
    # show_email(): Placeholder for formatt
    def show_email(self):
        self._read = True

        print(f"EMAIL ID: {self._m_id}")
        print(f"From:               {self._frm}")
        print(f"To:                 {self._to}")
        print(f"Date:               {self._date}")
        print(f"Subject:            {self._subject}")
        print(f"Tag:                {self._tag}")
        print(f"Flagged:            {self._flag}")
        print(f"Read:               {self._read}")
        print("BODY:")
        print(self._body)

        return {
            "m_id": self._m_id,
            "from": self._frm,
            "to": self._to,
            "subject": self._subject,
            "date": self._date,
            "tag": self._tag,
            "flag": self._flag,
            "read": self._read,
            "body": self._body,
        }
m = Mail(35,"email9@gre.ac.uk","email74@gre.ac.uk","28/5/2025","subject95","tag0","Body139") #taking arguments for eevery parametre of class
m.show_email()   #calling show_mail to print the arguments in that format.
