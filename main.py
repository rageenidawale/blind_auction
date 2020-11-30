from os import system, name
import art

print(art.logo)
print("Welcome to the secret auction program.")

bidding_dictionary = {}
do_continue = True


def clear():
    if name == 'nt':
        _ = system('cls')


def find_highest_bidder(bidding_record):
    highest_bid = 0
    for bidder in bidding_record:
        bidding_amount = bidding_record[bidder]
        if bidding_amount > highest_bid:
            highest_bid = bidding_amount
            winner = bidder
    print(f"The winner is {winner} with a bid of ${highest_bid}")


while do_continue:
    name = input("What is your name?: ")
    bid = int(input("What's your bid?: "))

    bidding_dictionary[name] = bid

    continue_bid = input("Are there any other bidders? 'yes' or 'no'\n")

    if continue_bid == "yes":
        clear()
    else:
        do_continue = False
        find_highest_bidder(bidding_dictionary)
