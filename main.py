
"""
    Welcome to Elite 101 this program is a starter for your chatbot project.
    The starter prompts the user to enter their name and then greets them with a personalized message.

    Functions:
        get_user_name(): Prompts the user to enter their name and returns it.
        greet_user(name): Prints a greeting message using the provided name.
        main(): Main function that orchestrates the user input and greeting process.

    Execution:
        When the script is run directly (not imported as a module), it will execute the main() function.
"""


def get_user_name():
    return input("Please enter your name: ")

def greet_user(name):
    print(f"Hello, {name}!")

def main():
    user_name = get_user_name()
    greet_user(user_name)

if __name__ == "__main__":
    main()
    
def start_conversation ():
   while True: 
    name = input("What is your name? ") 
    age = input("How old are you? ") 
    print(f"Hello, {name}!") 
    consent = input("Would you like to continue our conversations? (yes/no) ") 
    if consent.lower() == 'no': 
        print("Goodbye!") 
        break 
    else: 
        help_response = input("Can I help you? (yes/no) ").strip().lower() 
        if help_response.lower() == 'yes': 
            curious = input("How can I help?") 
        
        else: 
            print("Have a good day, goodbye.")
            break 
def menu ():
    print('Below are instructions to navigatng this conversation')
    print('1. Start conversation')
    print('2. Exit')
    choice = input('Pick the number of the option that you would like.')
    if choice == '1':
        start_conversation()
    elif choice == '2':
        print('Goodbye')
        return
    
menu()
    
    
    
    
