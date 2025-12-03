The solution utilizes a modular class design separated into three layers: the Controller (Interpreter.py), the 
Manager (MailboxAgent), and the Data/Model (Mail hierarchy). 
Inheritance is implemented to adhere to the "DRY" (Don't Repeat Yourself) principle. The Mail class serves as 
the superclass, defining shared attributes like sender, date, and subject. The Personal and Confidential classes 
inherit these via super().__init__, allowing them to extend functionality (e.g., encryption logic in Confidential) 
without redefining basic state. 
Polymorphism is achieved through method overriding, specifically show_mail(). The MailboxAgent manages a 
heterogeneous list of email objects. When it iterates through this list to display messages, it calls show_mail() 
on generic objects. Python’s dynamic binding ensures the correct specific version executes—masking the body 
for Confidential objects while showing it for Personal objects—removing the need for complex if/else type
checking in the Interpreter. 
Encapsulation is central to the MailboxAgent. This class encapsulates the list of email objects, exposing public 
methods for sorting and filtering while hiding the internal data structure from Interpreter.py. 
To improve this design, I would implement data hiding by making attributes private (e.g., self.__body). 
Currently, attributes are public, meaning Interpreter.py could accidentally mutate a Confidential email's body 
after encryption. Accessors (getters) would better secure the data integrity. 
