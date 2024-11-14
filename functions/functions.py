"""
STEP 1: Fix the declaration of the functions below to get the 
tests in test_functions.py to run.
"""

def get_date_of_birth(id_number): 
    """
    STEP 2: Extract the date of birth from the ID number and return it as a string
    """
    #todo
    len(id_number) == 13
    for i in id_number:
        if i in range(0, 5):
            dob = id_number
            return dob
        
    
def get_gender(id_number):
    """
    STEP 3: Extract the gender from the ID number using the formula below and return
    it as a string

    Formula: 1 if the ID number's 7th to 10th digit is less than 5000, the person is
    female and if it is greater than 4999, the person is male.
    """
    #todo
   
    len(id_number) == 13
    for i in id_number:
        if i in range(6, 9):
            if i > 5000:
                return 'female'
            elif i < 4999:
                return 'male'
   
    
def get_citizenship(id_number):
    """
    STEP 4: Extract the citizenship from the ID number using the formula below and 
    return it as a string

    Formula: 1 if the ID number's 11th to 12th digit is less than 01, the person is
    a South African citizen and if it is greater than 01, the person is a non-South 
    African citizen.
    """
    #todo
    len(id_number) == 13
    for i in id_number:
        if i in range(10, 11):
            if i > "01":
                citizenship = get_citizenship
            elif i < "01":
                citizenship != get_citizenship
                return citizenship
                
        
    