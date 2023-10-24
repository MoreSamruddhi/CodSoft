import random

def generate_password(username, password_length):
    """Generates a random password of the specified length, including the username.

    Args:
        username: The user's username.
        password_length: The desired length of the password.

    Returns:
        A random password of the specified length, including the username.
    """

    characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()-+"

    password = username
    for i in range(password_length - len(username)):
        password += random.choice(characters)

    return password

def main():
    """Prompts the user for their username and desired password length, and then generates a random password of that length, including the username. The user can choose to generate multiple passwords."""

    username = input("Enter your username: ")

    password_length = int(input("Enter the desired length of the password: "))

    while True:

        password = generate_password(username, password_length)

        print("The generated password is:", password)

        continue_choice = input("Continue (yes/quit)? ")

        if continue_choice == "quit":
            print("Thank You!!!")
            break

if __name__ == "__main__":
    main()
