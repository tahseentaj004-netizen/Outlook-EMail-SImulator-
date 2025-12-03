#################################################################################################
### COMP1811 - CW1 Outlook Simulator                                                          ###
###            Confidential Class                                                             ###
###            Defines a Confidential email which automatically encrypts its body             ###
###            content and overrides the display method to show encryption details.           ###
### Partner A:                                                                                ###
###            <Samira Uzturk>, SID<001464034-1>                                    ###
#################################################################################################

# DO NOT CHANGE CLASS OR METHOD NAMES
# replace "pass" with your own code as specified in the CW spec.

from Mail import Mail


# FA.5.a
class Confidential(Mail):
    """Represents a specialised email type for messages that are confidential
    Inherits from Mail and automatically encrypts the message body upon creation.
    """

    # DO NOT CHANGE CLASS NAME OR METHOD NAMES/SIGNATURES
    # Add new method(s) as required in CW spec

    def __init__(self, m_id, frm, to, date, subject, tag, body):  # DO NOT MODIFY Attributes
        super().__init__(m_id, frm, to, date, subject, tag, body)  # Inherits attributes from parent class DO NOT MODIFY
        self.body = self.encrypt()  # Overwrite the body with the encrypted version

    # FA.5.b
    def encrypt(self):
        """Encrypts the email message body based on the specified rules:
        1. Each letter becomes its numeric position in the alphabet (A=1, B=2, etc.)
           multiplied by the number of words in the original message body.
        2. Full stops (.) remain unchanged.
        3. Numbers (0-9) are replaced by their corresponding alphabet letters (0=j, 1=a, etc.).
        :rtype: str (the encrypted message body) """

        alphabet = "abcdefghijklmnopqrstuvwxyz"
        number_mapping = "jabcdefghi"  # 0=j, 1=a, 2=b, ... 9=i

        # 1. Calculate the number of words in the original body
        # We replace dots with empty strings to ensure "word." counts as "word"
        words = self.body.replace(".", " ").split()
        count_word = len(words)

        # Initialize the list for the encrypted characters
        encrypted_chars = []

        # Process the body character by character
        for char in self.body:
            char_lower = char.lower()

            # Indentation fixed here: The IF block must be INSIDE the FOR loop
            if char_lower in alphabet:
                # Rule 1: Letter position * word count
                # Python index is 0-based, so we add 1 to make A=1, B=2
                position = alphabet.index(char_lower) + 1
                encrypt_value = str(count_word * position)
                encrypted_chars.append(encrypt_value)

            elif char == '.':
                # Rule 2: Full stops remain unchanged
                encrypted_chars.append(char)

            elif char.isdigit():
                # Rule 3: Numbers are replaced by their corresponding alphabet letters
                index = int(char)
                # Fixed syntax: Use square brackets [] for string indexing, not ()
                encrypted_chars.append(number_mapping[index])

            else:
                # Appends spaces and other punctuation unchanged
                encrypted_chars.append(char)

        # Join the characters back into the encrypted string
        return "".join(encrypted_chars)

    # FA.5.c
    def show_mail(self):
        """Overrides the Mail show_mail() method to display confidential emails
        in the specified format showing the encrypted body.
        """
        print("\nCONFIDENTIAL")
        print(f"From: {self.frm}")
        print(f"Date: {self.date}")
        print(f"Subject: {self.subject}")
        print(f"Encrypted body message: {self.body}")
        print(f"Flagged? {self.flag}")