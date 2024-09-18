import re
from datetime import datetime
import time
User_input=input("Enter Your Name:")

def validate_password(password):
    """Validate the password according to specific criteria."""
    # Check if the password meets the length requirement
    if len(password) < 8:
        return "Password must be at least 8 characters long."

    # Check if the password contains spaces
    if ' ' in password:
        return "Password must not contain spaces."

    # Check for at least one uppercase letter
    if not re.search(r'[A-Z]', password):
        return "Password must contain at least one uppercase letter."

    # Check for at least one lowercase letter
    if not re.search(r'[a-z]', password):
        return "Password must contain at least one lowercase letter."

    # Check for at least one digit
    if not re.search(r'[0-9]', password):
        return "Password must contain at least one digit."

    # Check for at least one special character
    if not re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        return "Password must contain at least one special character."
    
    return "Password is valid."

def get_valid_password():
    """Prompt the user for a valid password until the input is valid."""
    while True:
        password = input("Enter your password: ")
        validation_message = validate_password(password)
        if validation_message == "Password is valid.":
            print("Password accepted.")
            return password
        else:
            print(validation_message) # Example usage
valid_password = get_valid_password()
print(f"Your valid password is: {valid_password}")

print("Waiting for Movements.....")  # Pause the execution for 5 seconds
time.sleep(5)
print("This page was secured.....")
class Gender:
    def __init__(self,name,age,gender):
        self.name=name
        self.age=age
        self.gender=gender
    def gender_info(self):
        print('Name:{}'.format(self.name))
        print('age:{}'.format(self.age))
        print('gender:{}'.format(self.gender))
class Male(Gender):
    def __init__(self, name, age, gender, Matrimonyid,salary):
        super().__init__(name, age, gender) # its super( ) or its an refer to parent class()
        self.Matrimonyid=Matrimonyid
        self.salary=salary
    def Male_info(self):
        print('Matrimony Id:{}'.format(self.Matrimonyid))
        print('Employee Salary:{}'.format(self.salary))
class Female(Gender):
    def __init__(self, name, age, gender,Matrimony_id,salary):
        super().__init__(name, age, gender)
        self.Matrimony_id=Matrimony_id
        self.salary=salary
    def Female_info(self):
        print('employe Id:{}'.format(self.Matrimony_id))
        print("employee salary:{}".format(self.salary))
candidate1=Male('siva',23,'male',123,15000)
print('Male Candiate details:')
print('-------'*5)
candidate1.gender_info()
candidate1.Male_info()
#
candidate2=Female('selvi',21,'female',454,12000)
print('\nFemale Candiate details')
print('-----'*5)
candidate2.gender_info()
candidate2.Female_info()
print('Add the New Candiate:')
class Member:
    def __init__(self):
        self.Member_id=int(input('Create the userid:'))
        self.name=input("Enter the your Name:")
        self.gender=input("gender:")
        self.Email_id=input('Enter the Email Id:')
    def your_details(self):
        print('Plese check your details:')
        print("Id:{}\nName: {}\ngender:{}\nem".format(self.Member_id,self.name,self.gender,self.Email_id))
print('Enter the datas....\n')
for i in range(5):
    students=Member()
    students.your_details()
    print('-'*100)