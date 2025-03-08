# Ken Wabibi 27Feb25 

'''
                                          Patient Charges
The purpose of the program write a class named Patient that has attributes for the following data:

First name, middle name, and last name
Address, city, state, and ZIP code
Phone number

Then write a class named Procedure that represents a medical procedure that has been performed on a patient. The Procedure class should have attributes for the following data.

Name of the procedure
Date of the procedure
Name of the practitioner who performed the procedure
Charges for the procedure

Then, create three instances of the Procedure class, with the following data input from the keyboard.

 '''

class Patient:
    def __init__(self, first_name, middle_name, last_name, address, city, state, zip_code, phone_number, emergency_name, emergency_phone):
        # Initialize all attributes of the Patient class
        self.first_name = first_name
        self.middle_name = middle_name
        self.last_name = last_name
        self.address = address
        self.city = city
        self.state = state
        self.zip_code = zip_code
        self.phone_number = phone_number
        self.emergency_name = emergency_name
        self.emergency_phone = emergency_phone

        # Getter Methods for the Patient Class 
    def get_first_name(self):
        return self.first_name
    
    def get_middle_name(self):
        return self.middle_name
    
    def get_last_name(self):
        return self.last_name
    
    def get_address(self):
        return self.address
    
    def get_city(self):
        return self.city
    
    def get_state(self):
        return self.state
    
    def get_zip_code(self):
        return self.zip_code
    
    def get_phone_number(self):
        return self.phone_number
    
    def get_emergency_name(self):
        return self.emergency_name
    
    def get_emergency_phone(self):
        return self.emergency_phone

    # Setter Methods 
    def set_first_name(self, first_name):
        self.first_name = first_name
    
    def set_middle_name(self, middle_name):
        self.middle_name = middle_name
    
    def set_last_name(self, last_name):
        self.last_name = last_name
    
    def set_address(self, address):
        self.address = address
    
    def set_city(self, city):
        self.city = city
    
    def set_state(self, state):
        self.state = state
    
    def set_zip_code(self, zip_code):
        self.zip_code = zip_code
    
    def set_phone_number(self, phone_number):
        self.phone_number = phone_number
    
    def set_emergency_name(self, emergency_name):
        self.emergency_name = emergency_name
    
    def set_emergency_phone(self, emergency_phone):
        self.emergency_phone = emergency_phone

class Procedure:
    def __init__(self, procedure_name, procedure_date, practitioner_name, charges):
        # Initialize all attributes of the Procedure class
        self.procedure_name = procedure_name
        self.procedure_date = procedure_date
        self.practitioner_name = practitioner_name
        self.charges = charges

    # Getter Methods for Procedure Class 
    def get_procedure_name(self):
        return self.procedure_name
    
    def get_procedure_date(self):
        return self.procedure_date
    
    def get_practitioner_name(self):
        return self.practitioner_name
    
    def get_charges(self):
        return self.charges
    
    # Setter Methods for the Procedure Class
    def set_procedure_name(self, procedure_name):
        self.procedure_name = procedure_name
    
    def set_procedure_date(self, procedure_date):
        self.procedure_date = procedure_date
    
    def set_practitioner_name(self, practitioner_name):
        self.practitioner_name = practitioner_name
    
    def set_charges(self, charges):
        self.charges = charges

# Main program to input data
def main():
    # Input details for the Patient instance
    print("Enter Patient Details:")
    first_name = input("First Name: ")
    middle_name = input("Middle Name: ")
    last_name = input("Last Name: ")
    address = input("Address: ")
    city = input("City: ")
    state = input("State: ")
    zip_code = input("ZIP Code: ")
    phone_number = input("Phone Number: ")
    emergency_name = input("Emergency Contact Name: ")
    emergency_phone = input("Emergency Contact Phone: ")

    # Create an instance of Patient
    patient = Patient(first_name, middle_name, last_name, address, city, state, zip_code, phone_number, emergency_name, emergency_phone)

    print("\nPatient information receive.")

    # Input details for three Procedure instances
    procedures = []
    for i in range(3):
        print(f"\nEnter details for Procedure {i+1}:")
        procedure_name = input("Procedure Name: ")
        procedure_date = input("Procedure Date (YYYY-MM-DD): ")
        practitioner_name = input("Practitioner Name: ")
        charges = float(input("Procedure Charges: "))
        
        # Create an instance of Procedure
        procedure = Procedure(procedure_name, procedure_date, practitioner_name, charges)
        procedures.append(procedure)
    
    print("\nProcedure details receive.")

    print("\nProcedures:")
    for i, procedure in enumerate(procedures, 1):
        print(f"Procedure {i}: {procedure.get_procedure_name()} on {procedure.get_procedure_date()} by {procedure.get_practitioner_name()}")
        print(f"Charges: ${procedure.get_charges()}")
        

if __name__ == "__main__":
    main()

