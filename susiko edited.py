# Arrays for breakfast, lunch, and dinner menus
breakfast_menu = ['1.chicken - Rs.300', '2.veg- Rs.200', '3.fish- Rs.250']
lunch_menu = ['1.Egg -Rs.250', '2.prawns- Rs.700', '3.mix -RS.500']
dinner_menu = ['1.bread -Rs.250', '2.pasta-Rs.200', '3.noodles - Rs.300']

#main program
def breakfast(breakfast_menu):#breakfast function
    meal_code = 1
    breakfast_items = []#user's option will be stored here
    final_meal_total = [] #final bill of users will be stored here
    print("code\t meal\t\tprice\n1.\t\tchicken\t\tRs.300\n2.\t\tveg\t\t\tRs.200\n3.\t\tfish\t\tRs.250\n0.Exit")
    while meal_code > 0:

        meal_code = int(input("Enter your meal code :"))
        if meal_code == 1:
            first_item = breakfast_menu[0]
            meal_amount = int(input("Enter number of Chicken packets :"))
            meal_total = 300 * meal_amount#the relevent bill total will be calculated
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
    print("Total bill is Rs. : ", sum(final_meal_total),"if you want to cancel the order give a call to 0711461535")

def lunch(lunch_menu):#lunch function
        meal_code = 2
        lunch_items = []#user's option will be stored here
        final_meal_total = []#final bill of users eill be stored here
        print("code\t meal\t\tprice\n1.\t\tEgg\t\t\tRs.250\n2.\t\tprawns\t\tRs.700\n3.\t\tmix\t\t\tRS.500\n0.Exit")
        while meal_code > 0:
            meal_code = int(input("Enter your meal code :"))
            if meal_code == 1:
                first_item = lunch_menu[0]
                meal_amount = int(input("Enter number of Egg packets :"))
                meal_total = 250 * meal_amount#the  bill relevent tatal will be calculated
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
        print("Total bill is Rs. : ", sum(final_meal_total),"if you want to cancel the order give a call to 0711461535")
def dinner(dinner_menu):#dinner function
        meal_code = 1
        dinner_items = [] #this array is used to store the user option item regarding the meal options
        final_meal_total = [] #to store total bill of the user
        print("code\t meal\t\tprice\n1.\t\tbread\t\tRs.250\n2.\t\tpasta\t\tRs.200\n3.\t\tnoodles\t\tRs.300\n0.Exit")
        while meal_code > 0:
            meal_code = int(input("Enter your meal code : "))
            if meal_code == 1:
                first_item = dinner_menu[0]
                meal_amount = int(input("Enter number of pieces Bread :"))
                meal_total = 250 * meal_amount#the relevent bill total will be calculated
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
        print("Total bill is Rs. : ", sum(final_meal_total),"if you want to cancel the order give a call to 0711461535")


order_no=1
while order_no>0:#the main interface is printed
    print("welcome to Susiko \n ")
    print("(01) for breakfast menu press number one\t- Available from 6.00 am onwards")
    print("(02) for lunch menu press number two\t    - Available from 10.00 am onwards")
    print("(03) for dinner menu press number three\t    - Available from 5.00 pm onwards")
    print("(04) exit press number four")

    select= int(input("select your option:\n"))#to store user's prefered option




    #if condition(the functions are called according to the requested user option
    if(select==1):#the breakfast function is called
        breakfast(breakfast_menu)
    elif(select==2):#the lunch function is called
        lunch(lunch_menu)
    elif(select==3):#the dinner function is called
        dinner(dinner_menu)
    elif(select==4):

        break
    else:
        print("Invalid input.\n Please enter a valid input")



