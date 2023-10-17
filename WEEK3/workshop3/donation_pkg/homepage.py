def show_homepage():
    print("        === DonateMe Homepage ===         ")
    print("------------------------------------------")
    print("| 1.    Login     | 2.     Register      |")
    print("------------------------------------------")
    print("| 3.    Donate    | 4.    Show Donations |")
    print("------------------------------------------")
    print("|                5. Exit                 |")
    print("------------------------------------------")


def donate(username):
    donation_amt = float(input("Enter amount to donate:"))
    donation_string = f"{username} donated £{donation_amt}"
    print(f"Thank you for your donation {username}")
    return donation_string

def show_donation(donation):
    print("\n ----- All Donations ------")
    if donation == []:
        print('Currently, there are no donations.')
    else: 
        for i in donation:
            print(i)