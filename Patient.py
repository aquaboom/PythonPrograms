#Create a class patient with the attributes as Name, Patient Number and Phone Number. Also create a function to introduce the patient.

class Patient:
    def __init__(self,name,patientNumber,phoneNumber):  # This is a default constructor of the Class Patient
        self.name=name
        self.patientNumber=patientNumber
        self.phoneNumber=phoneNumber
    
    def introduce_self(self):
        print("My name is"+ self.name +"and my patient number is"+ self.patientNumber)
        
        
obj=Patient("Sonali",1,334-33-9280)
obj2=Patient("Trump",2,334-00-8880)
obj.introduce_self()
obj2.introduce_self()


Output:
My name is Sonali and my patient number is 1
My name is Trump and my patient number is 2
