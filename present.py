import art
import guess
import birthday_date
birthday_date.date_check()
answer = "yes"
name = input("What's your name?\n").lower()
name_error_messages = ["This code wasn't written for you, sorry!", "Are you sure that's a correct name?",
                       "Maybe there's a typo somewhere?"]
while answer != "no":
    attempts_yes_no = 3
    while answer != "yes" and attempts_yes_no != 0:
        answer = input(f"You have {attempts_yes_no} attempts left.\nPlease, choose yes or no:\n").lower()
        attempts_yes_no -= 1
    if attempts_yes_no == 0:
        print("Bye. ;(")
        exit()
    elif answer == "no":
        break
    if answer == "yes":
        attempts_name = 3
        name_error_index = 0
        while name != "kamil" and attempts_name != 0:
            print(name_error_messages[name_error_index])
            name_error_index += 1
            name = input(f"You have {attempts_name} attempts left.\nTry a different name or type EXIT:\n").lower()
            attempts_name -= 1
        if name == "exit" or attempts_name == 0:
            print("Bye. ;(")
            exit()
        if name == "kamil":
            print("Happy birthday, lovely!")
            guess.guessing_game()
            art.birthday_art()
            print("Thank you for playing with me! I hope you enjoyed your little gift!")
        answer = input("Wanna play again (yes/no)?\n").lower()
        if answer == "no":
            print("Bye-bye! Have a great day!")
            exit()