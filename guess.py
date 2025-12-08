import random
def congrats_message():
    print("You guessed it! May all the wishes you received come true!")
messages = ["May everyday of yours be joyful!", "Never forget that you are amazing", "I care about you deeply",
            "I hope this year will be great for you", "You are extremely smart and capable", "You are truly special",
            "Let all of your dreams come true", "I am proud of you", "I admire you",
            "I am wishing you the best of luck, always"]

def guessing_game():
    correct_answer = random.randint(1, 10)
    random.shuffle(messages)
    message_index = 0
    while True:
        try:
            number = int(input("Please, choose a number between 1 and 10:\n"))
            if 1 <= number <= 10:
                break
            else:
                print("Number must be between 1 and 10 :(")
        except ValueError:
            print("Choose a number, not something else, please :(")
    while number != correct_answer:
        if message_index < len(messages):
            print(messages[message_index])
            message_index += 1
        else:
            print("You are the best!")
        while True:
            try:
                number = int(input("Please, choose a number between 1 and 10:\n"))
                if 1 <= number <= 10:
                    break
                else:
                    print("Number must be between 1 and 10 :(")
            except ValueError:
                print("Choose a number, not something else, please :(")
    congrats_message()