def date_check():
    date = input("Hi-hi! First things first! What day is it today?(DD-MM):\n")
    dates_before = ["07-08","07.08", "07 08", "0708", "08-08", "08.08", "08 08", "0808", "09-08", "09.08", "09 08",
                    "0908"]
    expected_date = ["10-08", "10.08", "10 08", "1008"]
    unexpected_date = ["Are you sure the format is right?", "Try another date, maybe?", "One more try!"]
    unexpected_date_index = 0
    attempts_date = 3
    while date not in expected_date and date not in dates_before and attempts_date != 0:
        print(unexpected_date[unexpected_date_index])
        unexpected_date_index += 1
        date = input(f"You have {attempts_date} attempt left.\nPlease, type the date like DD-MM:\n")
        attempts_date -= 1
    if attempts_date == 0:
        print("Bye. ;(")
        exit()
    if date in dates_before:
        print("Ah-ah! The special day didn't come yet! Wait for a couple days!")
        exit()
    else:
        print("Yay! Today IS the day!")