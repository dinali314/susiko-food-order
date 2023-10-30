#main program
def breakfast(breakfast_menu):
    meal_code = 1
    breakfast_items = []
    final_meal_total = []
    print("1.chicken - Rs.300', '2.veg- Rs.200','3.fish- Rs.250',0.Exit")
    while meal_code > 0:

        meal_code = int(input("Enter your meal code :"))
        if meal_code == 1:
            first_item = breakfast_menu[0]
            meal_amount = int(input("Enter number of Chicken packets :"))
            meal_total = 300 * meal_amount
            breakfast_items.append(str(breakfast_menu[0]) + '* Number of Packets' + str(meal_amount))
            final_meal_total.append(meal_total)
        elif meal_code == 2:
            second_item = breakfast_menu[1]
            meal_amount = int(input("Enter number of Veg Packets :"))
            meal_total = 200 * meal_amount
            breakfast_items.append(str(breakfast_menu[1]) + '* Number of Packets' + str(meal_amount))
            final_meal_total.append(meal_total)
        elif meal_code == 3:
            third_item = breakfast_menu[2]
            meal_amount = int(input("Enter number of Fish Packets :"))
            meal_total = 250 * meal_amount
            breakfast_items.append(str(breakfast_menu[2]) + '* Number of Packets' + str(meal_amount))
            final_meal_total.append(meal_total)
        else:
            print(breakfast_items)
    print("Total bill is : ", sum(final_meal_total))


def lunch(lunch_menu):
        meal_code = 2
        lunch_items = []
        final_meal_total = []
        print("1.Egg -Rs.250', '2.prawns- Rs.700','3.mix -RS.500,'0.Exit")
        while meal_code > 0:
            meal_code = int(input("Enter your meal code :"))
            if meal_code == 1:
                first_item = lunch_menu[0]
                meal_amount = int(input("Enter number of Egg packets :"))
                meal_total = 250 * meal_amount
                lunch_items.append(str(lunch_menu[0]) + '* Number of Packets' + str(meal_amount))
                final_meal_total.append(meal_total)
            elif meal_code == 2:
                second_item = lunch_menu[1]
                meal_amount = int(input("Enter number of Prawns Packets :"))
                meal_total = 700 * meal_amount
                lunch_items.append(str(lunch_menu[1]) + '* Number of Packets' + str(meal_amount))
                final_meal_total.append(meal_total)
            elif meal_code == 3:
                third_item = lunch_menu[2]
                meal_amount = int(input("Enter number of mix Packets :"))
                meal_total = 500 * meal_amount
                lunch_items.append(str(lunch_menu[2]) + '* Number of Packets' + str(meal_amount))
                final_meal_total.append(meal_total)
            else:
                print(lunch_items)
        print("Total bill is : ", sum(final_meal_total))
def dinner(dinner_menu):
        meal_code = 1
        dinner_items = []
        final_meal_total = []
        print("1.bread -Rs.250', '2.pasta-Rs.200','3.noodles - Rs.300")
        while meal_code > 0:
            meal_code = int(input("Enter your meal code : "))
            if meal_code == 1:
                first_item = dinner_menu[0]
                meal_amount = int(input("Enter number of pieces Bread :"))
                meal_total = 250 * meal_amount
                dinner_items.append(str(dinner_menu[0]) + '* Number of Packets' + str(meal_amount))
                final_meal_total.append(meal_total)
            elif meal_code == 2:
                second_item = dinner_menu[1]
                meal_amount = int(input("Enter number of pasta packets :"))
                meal_total = 200 * meal_amount
                dinner_items.append(str(lunch_menu[1]) + '* Number of Packets' + str(meal_amount))
                final_meal_total.append(meal_total)
            elif meal_code == 3:
                third_item = dinner_menu[2]
                meal_amount = int(input("Enter number of noodles packets :"))
                meal_total = 300 * meal_amount
                dinner_items.append(str(dinner_menu[2]) + '* Number of Packets' + str(meal_amount))
                final_meal_total.append(meal_total)
            else:
                print(dinner_items)
        print("Total bill is : ", sum(final_meal_total))


order_no=1
while order_no>0:
    print("welcome to Susiko  ")
    print("(01) for breakfast menu press number one\t- Available from 6.00 am onwards")
    print("(02) for lunch menu press number two\t    - Available from 10.00 am onwards")
    print("(03) for diner menu press number three\t    - Available from 5.00 pm onwards")
    print("(04) exit press number four")
    select= int(input("select your option:"))

    # Arrays for breakfast, lunch, and dinner menus
    breakfast_menu = ['1.chicken - Rs.300', '2.veg- Rs.200','3.fish- Rs.250']
    lunch_menu = ['1.Egg -Rs.250', '2.prawns- Rs.700','3.mix -RS.500']
    dinner_menu =['1.bread -Rs.250', '2.pasta-Rs.200','3.noodles - Rs.300']



    #if condition
    if(select==1):
        breakfast(breakfast_menu)
    elif(select==2):
        lunch(lunch_menu)
    elif(select==3):
        dinner(dinner_menu)
    elif(select==4):
        break
    else:
        print("Invalid input.\n Please enter a valid input")

