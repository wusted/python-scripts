#!/usr/bin/python3

def checkout():
    total = 0
    count = 0
    moreItems = True
    while moreItems:
        price = float(input("Enter price of item (0 when done): "))
        if price != 0 and price > 0:
            count = count + 1
            total = total + price
            print("Subtotal: $ ", f"{total:.2f}")
        elif price < 0:
            print("error, negative number not allowed and not be counted, proceed... ")
        else:
            moreItems = False
    if count == 0:
        print("error, cant compute an average without data, try again... ")
    else:
        average = total/count
        print("Total items: ", f"{count:.2f}" )
        print("Total $: ", f"{total:.2f}")
        print("Average price per item: $", f"{average:.2f}")

checkout()

    
