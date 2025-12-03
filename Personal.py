#################################################################################################
### COMP1811 - CW1 Outlook Simulator                                                          ###
###            Personal Class                                                             ###
###            <describe the purpose and overall functionality of the class defined here>     ###
### Partner B:                                                                                ###
###            <Tahseen Taj>, SID<001494074>                              ###
#################################################################################################

# DO NOT CHANGE CLASS OR METHOD NAMES/SIGNATURES
# replace "pass" with your own code as specified in the CW spec.

from Mail import Mail

# FB.5.a
class Personal(Mail):
    """Only contain personal mails with same output format containing frm,to,date,subject,body,flag,read"""
    # DO NOT CHANGE CLASS NAME OR METHOD NAMES/SIGNATURES
    # Add new method(s) as required in CW spec
    def __init__(self, m_id, frm, to, date, subject, tag, body):  # DO NOT MODIFY Attributes
        super().__init__(m_id, frm, to, date, subject, tag, body)  # Inherits attributes from parent class DO NOT MODIFY

        #Automatically set the tag to the designated folder for Personal emails
        self.tag = "Personal"


        self.body = self.add_stats(body)  #Call the statistics method



    # FB.5.b
    #
    def add_stats(self,body):
        """The "Personal" email type simulates handling private emails. Personal emails have the same
        characteristics, attributes and behaviours as any other email, but are maintained in a special folder """

        # --- Part 1: Replace 'Body' with Sender's UID ---
        # 1. Extract the Sender's UID (text before "@")

        uid = self.frm.split("@")[0]

        modified_body = self.body.replace(self.body,uid,1)

        # 4. Calculate Statistics (Ensure you handle empty word list to avoid division by zero)
        word = body.split()
        word_count = len(word)

        if word_count > 0:
            total_length = sum(len(word) for word in word)
            avg_length = round(total_length / word_count, 2)
            longest_length = max(len(word) for word in word)
        else:
            avg_length = 0
            longest_length = 0

        # 5. Format the statistics string as required [cite: 347, 348]
        stats_string = (
            f"Stats: Word count:{word_count}, "
            f"Average word length:{avg_length}, "
            f"Longest word length:{longest_length}."
        )

        # 6. Return the modified body concatenated with the statistics
        return modified_body + " " + stats_string

    def show_mail(self):
        #executing the printing like the given format
        print("PERSONAL")
        print(f"From:{self.frm}")
        print(f"To:{self.to}")
        print(f"Date:{self._date}")
        print(f"Subject:{self.subject}")
        print(f"Body:{self.body}")
        print(f"Read?{self.read}")