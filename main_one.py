# Activities & Practices
# --------- [Loops] ---------
print("--------- [Loops] ---------")
print("----------------------------------")
# Practise 01
print("Practise #01")
ingredients = ["milk", "sugar", "vanilla extract", "dough", "chocolate"]
for ingredient in ingredients:
    print(ingredient)
print("----------------------------------")
# Practise 02
print("Practise #02")    
# ingredients = ["milk", "sugar", "vanilla extract", "dough", "chocolate"]
# Elegant Loops
# simple for loops in one-line
for ingredient in ingredients: print(ingredient)
print("----------------------------------")
# Practise 03
print("Practise #03") 
six_steps = range(6)
print(six_steps) # range(0, 6)
for temp in range(4):
    print("Learning Loops!")
print("----------------------------------")
# Practise 04
print("Practise #04") 
for temp in range(7):
    print("Loop is on iteration number " + str(temp + 1))
print("----------------------------------")
# Practise 05
print("Practise #05")     
promise = "In Sha Allah I will finish the Loops chapter today or tomorrow at most!"
for n in range(3):
    print(promise)
print("----------------------------------")
# Practise 06
print("Practise #06")
count = 0
while count <= 3:
    print(count)
    count += 1
print("----------------------------------")
# Practise 06
print("Practise #06")
# Elegant loops
# # Similar to for loops
count = 0
while count <= 3: print(count); count += 1
print("----------------------------------")
# Practise 07
print("Practise #07")
count = 0
print("Starting While Loop")
while count <= 3:
    # Print if the condition is still true
    print("Loop Iteration - count <= 3 is still true")
    # Print the current value of count
    print("Count is currently " + str(count))
    # Increment count
    count += 1
    print("--------------------------")
print("While Loop ended")
print("----------------------------------")
# Practise 08
print("Practise #08")
countdown = 10
print("Starting While Loop")
while countdown >= 0:
    print(countdown)
    countdown -= 1
    print("--------")
print("While Loop ended")
print("----------------------------------")
# Practise 09
print("Practise #09")
python_topics = ["variables", "control flow", "loops", "modules", "classes"]
length = len(python_topics)
index = 0

while index < length:
    print("I am learning about " + python_topics[index])
    index += 1
print("----------------------------------")
# Practise 10
print("Practise #10")
students_period_A = ["Alex", "Briana", "Cheri", "Daniele"]
students_period_B = ["Dora", "Minerva", "Alexa", "Obie"]

for student in students_period_A:
    #students_period_A.append(student) // Infinitie loop
    print(student)
print("----------------------------------")
# Practise 11
print("Practise #11")
items_on_sale = ["blue", "striped socks", "knit dress", "red headband", "dinosaurs onesie"]

for item in items_on_sale:
    if item == "knit dress":
        print("Found it") # Found it
print("----------------------------------")
# Practise 12
print("Practise #12")
# items_on_sale = ["blue", "striped socks", "knit dress", "red headband", "dinosaurs onesie"]

for item in items_on_sale:
    print(item)
    if item == "knit dress":
        break
print("End of search!")
print("----------------------------------")
# Practise 13
print("Practise #13")
dog_breeds_available_for_adoption = ["french_bulldog", "dalmation", "shihtzu", "poodle", "collie"]
dog_breed_I_want = "dalmation"

for dog_breed in dog_breeds_available_for_adoption:
    print(dog_breed)
    if dog_breed == dog_breed_I_want:
        print("They have the dog I want!")
        break
print("----------------------------------")
# Practise 14
print("Practise #14")
big_number_list = [1, 2, -1, 4, -5, 5, 2, -9]

for i in big_number_list:
    if i <= 0:
        #print(i) # reverse result -1 -5 -9
        continue
    print(i) # 1 2 4 5 2
print("----------------------------------")
# Practise 15
print("Practise #15")
ages = [12, 38, 34, 26, 21, 19, 67, 41, 17]

for age in ages:
    if age < 18:
        continue
    print(age)
print("----------------------------------")
# Practise 16
print("Practise #16")
project_teams = [["Ava", "Samantha", "James"], ["Lucille", "Zed"], ["Edgar", "Gabriel"]]

for teams in project_teams:
    print(teams)
print("----------------------------------")
# Practise 17
print("Practise #17")    
# project_teams = [["Ava", "Samantha", "James"], ["Lucille", "Zed"], ["Edgar", "Gabriel"]]

for teams in project_teams:
    # Loop elements in each sublist
    for student in teams:
        print(student)
print("----------------------------------")
# Practise 18
print("Practise #18")
sales_data = [[12, 17, 22], [2, 10, 3], [5, 12, 13]]

scoops_sold = 0

for location in sales_data:
    print(location)
    for element in location:
        scoops_sold = scoops_sold + element

print(scoops_sold)
print("----------------------------------")
# Practise 19
print("Practise #19")    
numbers = [2, -1, 79, 33, -45]
doubled = []

for number in numbers:
    doubled.append(number * 2)

print(doubled)
print("----------------------------------")
# Practise 20
print("Practise #20")  
# one-line
numbers = [2, -1, 79, 33, -45]
doubled = [num * 2 for num in numbers]
print(doubled)
print("----------------------------------")
# Practise 21
print("Practise #21") 
grades = [90, 88, 62, 76, 74, 89, 48, 57]
scaled_grades = [grade + 10 for grade in grades]
print(scaled_grades)
print("----------------------------------")
# Practise 22
print("Practise #22") 
numbers = [2, -1, 79, 33, -45]
only_negative_doubled = []

for num in numbers:
    if num < 0:
        only_negative_doubled.append(num * 2)

print(only_negative_doubled) # [-2, -90]
print("----------------------------------")
# Practise 23
print("Practise #23")         
# numbers = [2, -1, 79, 33, -45]
negative_doubled = [num * 2 for num in numbers if num < 0]
print(negative_doubled) # [-2, -90]
print("----------------------------------")
# Practise 24
print("Practise #24") 
heights = [161, 164, 156, 144, 158, 170, 163, 157]
can_ride_coaster = [height for height in heights if height > 161]
print(can_ride_coaster) # [164, 170, 163]
print("----------------------------------")
# Practise 25
print("Practise #25")
single_digits = range(10)
squares = []

for item in single_digits:
    print(item)
    squares.append(item**2)

print(squares)

cubes = [item**3 for item in single_digits]
print(cubes)
print("----------------------------------")
# Practise 26
print("Practise #26")
print("----------------------------------")
print("-----[Carly's Clippers]-----")
print("----------------------------------")
# You are the Data Analyst at Carly's Clippers, the newest hair salon on the block. Your job is to go through the lists of data that have been collected in the past couple of weeks. You will be calculating some important metrics that Carly can use to plan out the operation of the business for the rest of the month.
# You have been provided with three lists: hairsyles, prices, and last_week.
# Each index in [hairstyles] corresponds to an associated index in [prices] and [last_week].
hairstyles = ["bouffant", "pixie", "dreadlocks", "crew", "bowl", "bob", "mohawk", "flattop"]
prices = [30, 25, 40, 20, 20, 35, 50, 35]
last_week = [2, 3, 5, 8, 4, 4, 6, 2]
# [Prices and Cuts]
print("-------[Prices and Cuts]-------")
# Carly wants to be able to market her low prices. We want to find out what the average price of a cut is.

# Solution - from user [Moud]
# print("-------[3rd Solution]-------")
total_price = 0
average_price = [total_price := total_price + price for price in prices][-1]/len(prices)
print("Average Haircut Price: " + str(average_price)) 
# Output: Average Haircut Price: 31.875
# Average Haircut Price: 31.875

# my regular ordinary solution
# total_price = 0
# for price in prices:
#     total_price += price
# average_price = "Average Haircut Price: " + str(total_price/len(prices))
# print(average_price) 
# Output: Average Haircut Price: 31.875

# Solution - from user [abc]
# print("-------[1st Solution]-------")
# total_price = 0
# average_price = sum([price/len(prices) for price in prices])
# print("Average Haircut Price: " + str(average_price)) 
# # Output: Average Haircut Price: 31.875

# Solution - from user [r]
# print("-------[2nd Solution]-------")
# total_price = 0
# average_price = [total_price := total_price + price for price in prices]
# print("Average Haircut Price: " + str(total_price/len(prices)))
# # Output: Average Haircut Price: 31.875

print("----------------------------------")
# The average price is more expensive than Carly thought it would be! She wants to cut all prices by 5 dollars.
new_prices = [price - 5 for price in prices]
print("Cutting all prices by 5 dollars:")
print(new_prices)
print("-------[Revenue]-------")
# Caryl really wants to make sure that Caryl's Clippers is a profitable endeavor. She first wants to know how much revenue was brought in last week + average daily revenue.
total_revenue = 0
total_revenue1 = sum([prices[i] * last_week[i] for i in range(len(hairstyles))])
print("Total Revenue: " + str(total_revenue1))
average_daily_revenue = total_revenue1 / 7
print("Average Daily Revenue: " + str(average_daily_revenue))
# Carly thinks she can bring in more customers by advertising all of the haircuts she has that are under 30 dollars.
cuts_under_30 = [hairstyles[i] for i in range(len(hairstyles)) if new_prices[i] < 30]
print("Cuts under $30: " + str(cuts_under_30))
print("----------------------------------")
# Practise 27
print("Practise #27")
# Create a function named divisible_by_ten() than takes a list of numbers named nums as a parameter.
# Return the count of how many numbers in the list are divisible by 10.
print("-------[Divisible By Ten]-------")
def divisible_by_ten(nums):
    counter = 0
    for num in nums:
        if num % 10 == 0:
            counter += 1
        else:
            continue
    return counter

print(divisible_by_ten([10, 5, 4, 8, 3, 20])) # Output: 2
print(divisible_by_ten([20, 25, 30, 35, 40])) # Output: 3
print("----------------------------------")
# Practise 28
print("Practise #28")
print("-------[Greetings]-------")
# Create a function named add_greetings() which takes a list of strings named names as a parameter.
# In the function, create an empty list that will contain each greeting. Add the string 'Hello, ' in front of each name in names and append the greeting to the list.
# Return the new list containing the greetings.
def add_greetings(names):
    new_list = []
    for name in names:
        new_list.append("Hello, " + name)
    return new_list

print(add_greetings(["Mohammad", "Khaled", "Ayman"]))
print("----------------------------------")
# Practise 29
print("Practise #29")
print("-------[Delete Starting Even Numbers]-------")


# Write a function called delete_starting_evens() that has a parameter named lst.
# The function should remove elements from the front of lst until the front of the list is not even. The function should then return lst.
# For example if lst started as [4, 8, 10, 11, 12, 15], then delete_starting_evens(lst) should return [11, 12, 15].
# Make sure your function works even if every element in the list is even!

def delete_evens(lst):
    while (len(lst) > 0 and lst[0] % 2 == 0):
        lst = lst[1:]
    return lst   

print(delete_evens([4, 11, 15, 12, 8, 10])) # Output: [11, 15]
print(delete_evens([4, 8, 10])) # Output: []
print(delete_evens([7, 11, 15, 12, 8, 45])) # Output: [7, 11, 15, 45]



# def delete_evens(lst):
#     result = list(filter(lambda n: n % 2 == 1, lst))
#     return result 
# Output:
# [11, 15]
# []
# [7, 11, 15, 45]



# Solution fron user - يوسف 
# >>> list(filter(lambda n: n % 2 == 1, lst))
# [1, 3, 9]

# >>> lst = [1,2,3,9,10]

# def is_even(f_e:int)-> bool:
#     '''
#     Parameter:
#     f_e -- First Element of the list
#     It will check if the arguement is an even number or not.
    
#     >>> is_even(4)
#     True
#     >>> is_even(3)
#     False
#     >>> is_even(6)
#     True
#     '''
#     return f_e%2==0
# def delete_start_events(lst:list)-> list:
#     '''
#     It will just take the a list and delete the even number from the start of it
#     >>> [1,2,3,4]
#     [1,2,3,4]
#     >>> [14,12,15, 16, 18]
#     [15, 16, 18]
#     >>> [16,12,24]
#     []
#     '''
#     for i in lst:
#         if is_even(i):
#             del lst[0]
#     return lst



print("----------------------------------")
# Practise 30
print("Practise #30")
print("-------[Odd Indices]-------")
# Create a function named odd_indices() that has one parameter named lst.
# The function should create a new empty list and add every element from lst that has an odd index. The function should then return this new list.
# For example, odd_indices([4, 3, 7, 10, 11, -2]) should return the list [3, 10, -2].
def odd_indices(lst):
    new_list = []
    for i in range(1, len(lst), 2):
        new_list.append(lst[i])
    return new_list    

print(odd_indices([4, 3, 7, 10, 11, -2])) # [3, 10, -2]
print("----------------------------------")
# Practise 30
print("Practise #30")
print("-------[Exponents]-------")
# Create a function named exponents() that takes two lists as parameters named bases and powers. Return a new list containing every number in bases raised to every number in powers.
# For example, consider the following code.
# exponents([2, 3, 4], [1, 2, 3])
# the result would be the list [2, 4, 8, 3, 9, 27, 4, 16, 64]. It would first add two to the first. Then two to the second. Then two to the third, and so on.
def exponents(bases, powers):
    new_list = []
    for base in bases:
        for power in powers:
            new_list.append(base ** power)
    return new_list

print(exponents([2, 3, 4], [1, 2, 3])) # [2, 4, 8, 3, 9, 27, 4, 16, 64]
print("----------------------------------")
# Practise 31
print("Practise #31")
print("-------[Larger Sum]-------")
# Create a function named larger_sum() that takes two lists of numbers as parameters named lst1 and lst2.
# The function should return the list whose elements sum to the greater number. If the sum of the elements of each list are equal, return lst1.
def larger_sum(lst1, lst2):
    sum1 = 0
    sum2 = 0
    for n in lst1:
        sum1 += n
    for n in lst2:
        sum2 += n
    if sum1 >= sum2:
        return lst1
    else:
        return lst2

print(larger_sum([1, 9, 5], [2, 3, 7])) # [1, 9, 5]
print("----------------------------------")
# Practise 32
print("Practise #32")
print("-------[Over 9000]-------")
# Create a function named over_nine_thousand() that takes a list of numbers named lst as a parameter.
# The function should sum the elements of the list until the sum is greater than 9000. When this happens, the function should return the sum. If the sum of all of the elements is never greater than 9000,the function should return total sum of all the elements. If the list is empty, the function should return 0.
# For example, if lst was [8000, 900, 120, 5000], then the function should return 9020.
def over_nine_thousand(lst):
    counter = 0
    for n in lst:
        counter += n
        if counter > 9000:
            break
    return counter    

print(over_nine_thousand([8000, 900, 120, 5000]))
print("----------------------------------")
# Practise 33
print("Practise #33")
print("-------[Max Num]-------")
# Create a function named max_num() that takes a list of numbers named nums as a parameter.
# The function should return the largest number in nums
def max_num(nums):
    max_num = nums[0]
    for num in nums:
        if num > max_num:
            max_num = num
    return max_num    

print(max_num([80, 70, 50, 54])) # 80      
print(max_num([80, 70, 50, 100])) # 100
print("----------------------------------")
# Practise 34
print("Practise #34")
print("-------[Same Values]-------")
# Write a function named same_values() that takes two lists of numbers of equal size as parameters.
# The function should return a list of the indices where the values were equal in lst1 and lst2.
# For example, the following code should return [0, 2, 3]
# same_values([5, 1, -10, 3, 3], [5, 10, -10, 3, 5])
def same_values(lst1, lst2):
    new_list = []
    for i in range(len(lst1)):
        if lst1[i] == lst2[i]:
            new_list.append(i)
    return new_list        

print(same_values([5, 1, -10, 3, 3], [5, 10, -10, 3, 5])) #indices are [0, 2, 3]
print("----------------------------------")
# Practise 35
print("Practise #35")
print("-------[Reversed List]-------")
# Create a function named reversed_list() that takes two lists of the same size as parameters named lst1 and lst2.
# The function should return True if lst1 is the same as lst2 reversed. The function should return False otherwise.
# For example, reversed_list([1, 2, 3], [3, 2, 1]) should return True.
def reversed_list(lst1, lst2):
    for i in range(len(lst1)):
        if lst1[i] != lst2[len(lst2) - 1 - i]:
            return False
    return True

print(reversed_list([1, 2, 3], [3, 2, 1])) # True
print(reversed_list([1, 5, 3], [3, 2, 1])) # False
  

