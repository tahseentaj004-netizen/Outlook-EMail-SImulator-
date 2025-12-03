#################################################################################################
### COMP1811 - CW1 Outlook Simulator                                                          ###
###            MailboxAgent Class                                                             ###
###            <describe the purpose and overall functionality of the class defined here>     ###
### Partner A:                                                                                ###
###            <Tahseen Taj>, SID<001494074>                              ###
### Partner B:                                                                                ###
###            <Samira Ozturk>, SID<001464034-1>                              ###
#################################################################################################

# DO NOT CHANGE CLASS OR METHOD NAMES
# replace "pass" with your own code as specified in the CW spec.

from Mail import Mail
from Confidential import Confidential
from Personal import Personal


class MailboxAgent:
    """<This is the documentation for MailboxAgent. Complete the docstring for this class."""
    def __init__(self, email_data):                       # DO NOT CHANGE
        self._mailbox = self.__gen_mailbox(email_data)    # data structure containing Mail objects DO NOT CHANGE

        # Calculate the highest existing ID in the mailbox to ensure uniqueness
        max_id = 0
        for mail in self._mailbox:
            if mail.m_id > max_id:
                max_id = mail.m_id
        
        # Set the next available ID to be one higher than the max
        self.next_m_id = max_id + 1

    # Given email_data (string containing each email on a separate line),
    # __gen_mailbox returns mailbox as a list containing received emails as Mail objects
    @classmethod
    def __gen_mailbox(cls, email_data):                   # DO NOT CHANGE
        """ generates mailbox data structure
            :ivar: String
            :rtype: list  """
        mailbox = []
        for e in email_data:
            msg = e.split('\n')
            mailbox.append(
                Mail(msg[0].split(":")[1], msg[1].split(":")[1], msg[2].split(":")[1], msg[3].split(":")[1],
                     msg[4].split(":")[1], msg[5].split(":")[1], msg[6].split(":")[1]))
        return mailbox
# FEATURES A (Partner A)
    #
    # # FA.1 retrieve email with get_email()
    # # Loops through Mail objects in mailbox
    # # Returns matching Mail and None if ID not found
    def get_email(self, m_id):
          for mail in self._mailbox:  # looks in mailbox
              if mail.m_id == str(m_id):  # ensure string comparison
                  return mail
          return None  # only reached if not found
            

    # FA.3
    # 
    def del_email(self, m_id):
        """  """
        for mail in self._mailbox:
            if mail.m_id == m_id:      #Check the 'm_id' attribute of the individual 'mail' object
                mail.tag = bin
                print(f"Email {m_id} moved successfully to the bin")
                return True     
        print(f"Error {m_id} not found")
        return False

    # FA.4
    def filter(self, frm):
        filtered = [mail for mail in self._mailbox if mail.frm.lower() == frm.lower()]

        # list comprehension filters by sender
        if not filtered:
            print(f"No email found from {frm}")
        else:
            for mail in filtered:  # display using show_mail()
                mail.show_email()

        return filtered  # return list for further use


    # FA.5
    def sort_date(self):
        def get_date(mail):  # extract from mail object
            return mail.date

        # use get_date to decide what to sort by
        self._mailbox.sort(key=get_date, reverse=True)  # newest first
        return self._mailbox


# FEATURES B (Partner B)
    # FB.1
    # 
    def show_emails(self):
        """ showing table type format for displaying all emails as given in the coursework  """

        if not self._mailbox:
            print("No Emails")    #Display if there are no emails in mailbox
            return
        
        #print the header of the table as coursework
        print(f"Id: |From:               |To:                 |Date:       |Subject:      |Tag:   |Body:")


         # Print each email row
        for mail in self._mailbox:
             print(f"{mail.m_id:<3} |"
                f"{mail.frm:<20}|"
                f"{mail.to:<20}|"
                f"{mail.date:<12}|"
                f"{mail.subject:<13}|"
                f"{mail.tag:<8}|"
                f"{mail.body}")
    
    
    # FB.2
    # 
    def mv_email(self, m_id, tag):
        """Implement the mv_email(m_id, tag) stub. Given an email ID, m_id and tag (the folder name to move 
           the email to), move that email to the folder indicated in tag. To simulate moving an email to a different 
           folder, replace the existing _tag value for that email with the value passed in the tag argument.  """
        #Moves an email to a new folder by updating its tag attribute.
        # Retrieve the mail for the provided mail id 
        mail_found = False
    # 1. Loop through the mailbox to find the matching email ID
    # Assuming self.mailbox is the list containing all Mail objects
        for mail in self._mailbox:
            # Check if the current email's ID matches the provided m_id
            if mail.m_id == m_id:
            
                # 2. Simulate moving the email by replacing the tag value
                # Update the object's attribute directly
                mail.tag = tag
            
            print(f"Successfully moved email ID {m_id} to folder: '{tag}'.")
            mail_found = True
            
            # Since the email is found and updated, we can stop the loop
            break 
    
    # 3. Check if the email was found and moved
        if mail_found:
            return True
        else:
               # If the loop finished without finding a match, print an error and return False
            print(f"Error: Email ID {m_id} not found in mailbox.")
            return False
    
    
    
    # FB.3
    def mark(self, m_id, m_type):
        """Implement the mrk(m_id, mrk_type) stub. Given an email ID, m_id, mark that email as mark_type 
           (read or flagged). This simulates an email shown as read in the mailbox or one that is flagged for follow
            up at a later time.   """
        
        mail_found = False
        mark_type = m_type.lower()    #standardazing the input 

        for mail in self._mailbox:
            #check if the m_id provided is in the mailbox
            if mail.m_id == m_id:
                
                #check if the mail is read or not 
                if mark_type == "read":
                    mail.read = True 
                    print(f"Email id {mail.m_id} marked as READ")
                #check if it is flagged or not and update it for follow up
                elif mark_type == "flagged":
                    mail.read = True 
                    print(f"EMail id {mail.m_id} marked as Flagged")

                else: 
                    print("Error, Invalid mail type. Should be 'READ' or 'FLAGGED'")
                    return False
                mail_found == True
                break         #end of loop
        
        if mail_found:
            return True
        else: 
            print("Invalid Emaid ID")
            return False


    # FB.4
    # 
    def find(self, date):
        """Implement the find(date) stub. Given a specific date, date as a string, return a list of all the emails 
           received on that date. This simulates searching the mailbox for all emails received on a particular date.   """
        
        input_date = date.strip()
        
        # 1. Initialize an empty list to store all Mail objects that match the date.
        email_list = []
    
         #check if the mails are upto that date 
        for mail in self._mailbox:
            # 3. Check if the input date matches the email's date attribute.
            if input_date == mail.date:   
                # 4. If a match is found, add the entire Mail object to the results list.
                email_list.append(mail) 
        
        # 5. After checking all emails, check if the list of results is empty.    
        if not email_list:
            print(f"No Emails found on that date: {date}")
        
        ## 6. Return the list of matching emails (it will be an empty list if no matches were found).
        return email_list

    
    # FB.5
    # 
    def sort_from(self):
        """ Sorts the mailbox list in-place by the sender's email address (frm). """
        if not  self._mailbox:
            print("Mailbox not empty")
            return
        
        # .lower(): ensures the sort is case-insensitive (A vs a)
        self._mailbox.sort(key=lambda mail: mail.frm.lower())
        
        print("Mailbox successfully sorted by Sender.")


# FEATURE 6 (Partners A and B)
    # 
    def add_email(self, frm, to, date, subject, tag, body):
        """ To simulate new emails sent to the mailbox, implement the add_email(frm,to,date,subject, 
        tag,body) stub given the email data. The code must also generate a unique m_id.  
        This method should create an appropriate object type (general Mail, Confidential or Personal) based on 
        the given tag and add it to the mailbox, _mailbox data structure. For example, create a Confidential 
        object when the tag is "conf", a Personal object when the tag is "prsnl", or a general Mail object  
        for any other tag. """
        # code must generate unique m_id
        new_id = self.next_m_id

        new_email = None # add new email object in thesee variable
        match tag.lower():
            # FA.6
            case 'conf':     # executed when tag is 'conf'
                # FA.6 - Create Confidential object (Partner A focus)
                new_email = Confidential(new_id, frm, to, date, subject, tag, body)
            # FB.6
            case 'prsnl':    # executed when tag is 'prsnl'
                new_email = Personal(new_id, frm, to, date, subject, tag, body)
            # FA&B.6
            case _:          # executed when tag is neither 'conf' nor 'prsnl'
                new_email = Mail(new_id, frm, to, date, subject, tag, body)
        if new_email:
        # Append the new object to the mailbox list (assuming self.mailbox is the structure)
            self._mailbox.append(new_email)
        
        # Increment the counter for the next email to ensure uniqueness
            self.next_m_id += 1 
        
            print(f"New email ID {new_id} (Type: {new_email.__class__.__name__}) added successfully.")
            return new_email
    
        return None # Should only happen if an unexpected error occur
        

