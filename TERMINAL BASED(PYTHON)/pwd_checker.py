import string
import getpass

def check_password_strength():
    password = getpass.getpass('\nEnter the password: ')
    strength = 0
    STATUS = ''
    
    # Criteria for password strength
    min_length = 8
    has_lower = any(char.islower() for char in password)
    has_upper = any(char.isupper() for char in password)
    has_digit = any(char.isdigit() for char in password)
    has_special = any(char in string.punctuation for char in password)
    
    # Evaluate strength
    if len(password) >= min_length:
        strength += 1
    if has_lower:
        strength += 1
    if has_upper:
        strength += 1
    if has_digit:
        strength += 1
    if has_special:
        strength += 1

    # Provide feedback based on strength
    if strength <= 2:
        STATUS = "WEAK"
    elif strength == 3:
        STATUS = "WEAK-- with a chance of improvement:)"
    elif strength == 4:
        STATUS = "MODERATE"
    elif strength == 5:
        STATUS = "STRONG"

    print('\nPassword analysis:')
    print(f'Length: {"Sufficient" if len(password) >= min_length else "Insufficient"}')
    print(f'Contains lowercase letters: {"Yes" if has_lower else "No"}')
    print(f'Contains uppercase letters: {"Yes" if has_upper else "No"}')
    print(f'Contains digits: {"Yes" if has_digit else "No"}')
    print(f'Contains special characters: {"Yes" if has_special else "No"}')
    print(f'Password Score: {strength} / 5')
    print(f'STATUS: {STATUS}')
    
    #function to start the process again or exit the program
    def check_pwd_again():
        check_again = input('\nDo you want to check password strength again? (yes/no): ').strip().lower()
        if check_again == 'yes':
            check_password_strength()
        elif check_again == 'no':
            print('\nExiting...')
        else:
            print('ERROR--> Please enter a valid input value')
            check_pwd_again()
            
    check_pwd_again()

if __name__ == '__main__':
    print('---------------- Welcome to Password Strength Checker ----------------')
    check_password_strength()
