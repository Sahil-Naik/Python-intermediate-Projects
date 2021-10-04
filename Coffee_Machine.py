# Machine Mechanism
# This Program is a replica of real-life coffee machine, it's working is kept as close to real as possible.
# This coffee machine is a coin operated vendor machine.

def mach():         # mach = Machine
    # Coffee material left
    mlk = 300  # ml
    cof_bn = 200  # gm
    wtr = 500  # ml

    # Pricing of flavours
    lat = 10  # Rs.
    xpre = 15  # Rs.
    capa = 25  # Rs.
    
    # mlk = Milk, lat = Latte, xpre = Espresso, capa = Cappuccino, cof_bn = Coffee Beans, wtr = Water

    # The while condition checks whether, there is sufficient coffee materials to process the given order.
    # Insert coin is nothing but, it asks you to enter the exact value of your order. It also gives back your change it you insert excess money.
    # Once the machine is out of materials, it ask user to refill again or not.
    # Each order has it's own requirement of material, over-time the machine might ran out of any of the 3 materials, and hence won't work until refilled.
    
    while mlk >= 55 and cof_bn >= 25 and wtr >= 60:
        mac = input("\nLatte : 10\nCappuccino : 25\nEspresso : 15\nType end to quit!\nSelect one Flavour : ").upper()
        if mac == 'REPORT':
            print("\nMilk :",mlk,"ml\nCoffee beans :",cof_bn,"gm\nWater :",wtr,"ml")
        elif mac == 'LATTE':
            coin = int(input("Insert coin! "))
            if coin >= 10:
                mlk = mlk - 50
                cof_bn = cof_bn - 10
                wtr = wtr - 50
                print("Here's you Latte")
                print("Your change is Rs.",coin-lat)
            else:
                print("Insufficient coins")
        elif mac == 'CAPACINO':
            coin = int(input("Insert coin! "))
            if coin >= 25:
                mlk -= 55
                cof_bn -= 25
                wtr -= 60
                print("Here's you Capacino")
                print("Your change is Rs.",coin-capa)
            else:
                print("Insufficient coins")
        elif mac == 'XPRESSO':
            coin = int(input("Insert coin! "))
            if coin >= 15:
                mlk -= 45
                cof_bn -= 10
                wtr -= 50
                print("Here's you Xpresso")
                print("Your change is Rs.",coin-xpre)
            else:
                print("Insufficient coins")
        elif mac == 'end':
            print("\nHave a nice day!")
            break
    else:
        print("Material out-of-stock!")
        refl = input("Insufficient Materials!\nRefill again? y/n : ").upper()
        if refl == 'Y':
            mlk += 500
            cof_bn += 250
            wtr += 550
            mach()

strt = input("Start the machine? y/n : ").upper()
if strt == 'Y':
    mach()
else:
    print("Not today!")
