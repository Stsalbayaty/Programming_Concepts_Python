#chapter8

#

# Chapter 8 password validation program: Ask the user to enter a new password and indicate if the password is valid or invalid
# Password requirements: must be at least 8 characters long, have one upper case, and one digit, and a special character

def hasUpperCase(pw):    
    upperFound = False   
    for ch in pw:        
        if ch.isupper() == True:            
            upperFound = True    
            
    return upperFound
def hasDigit(pw):    
    digitFound = False    
# Test each character and see if we find a digit    
    for ch in pw:        
        if ch.isdigit() == True:            
            digitFound = True 

    return digitFound

def hasSpecialCharacter(pw): 
    specialCharacter = ["!", "@", "#", '$'] 
    specialFound = False
    for ch in pw: 
        if any(ch in specialCharacter for ch in pw): 
            specialFound = True

    return specialFound


def isPasswordValid(pw):    
    pwValid = True    
    if len(pw) < 8:        
        print("Your password must be at least 8 characters long")       
        pwValid = False   

    if hasUpperCase(pw) == False:        
        print("Your password must contain at least one uppercase character")        
        pwValid = False   

    if hasDigit(pw) == False:        
        print("Your password must contain at least one digit")        
        pwValid = False   

    if  hasSpecialCharacter(pw) == False:
        print("Your password must contain at least one of these special characters: !, @, #, or $")
        pwValid = False

    return pwValid
    
def main():    
    pw = input("Please enter your new password: ")    
    
       
    while isPasswordValid(pw) != True:
        pw = input("Please enter a valid password ")

main()






