#chapter8

# Add an additional requirement for a valid password-it must contain at least one of these special characters: !, @, #, or $
# Create a loop in the appropriate place in the program so if the user enters an invalid password, the program will ask them to enter a new password until they have entered a valid password.

# Chapter 8 password validation program: Ask the user to enter a new password and indicate if the password is valid or invalid
# Password requirements: must be at least 8 characters long, have one upper case, and one digit
def hasUpperCase(pw):    
    upperFound = False   
# Test each character in the password and see if we find an uppercase character. Set the flag to true if we find one    
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
    return pwValid
    
def main():    
    pw = input("Please enter your new password: ")    
    
    if isPasswordValid(pw) == True:        
        print("Thank you for entering a valid password")    
    else:        
        print("Your password did not meet the minimum requirements")
main()