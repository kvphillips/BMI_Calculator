#defining and creating empty lists to append values to
names = ["Katie", "Alec", "Matthew", "Christina", "Alyson", "Dave"]
heights = []
weights = []
body_mass_indexes = []
underweight = 0
overweight = 0
normal_weight = 0

#prompts user for each person's height and weight from the list "names"
for name in names:
    print("What height is", name,"?")
    print("What weight is", name,"?")
    height = eval(input("Enter height in inches here:"))
    weight = eval(input("Enter weight in pounds here:"))

#computes user input and calculates BMI from weight and height
#it then appends those values to make another list called body_mass_indexes
    body_mass_index = int((weight*703)/(height**2))
    body_mass_indexes.append(body_mass_index)

#outputs user's BMI and tells you whether they are underweight,
#overweight, or a normal weight
# += 1 counts the totals of each of the if, elif or else statements
for n, b in zip(names, body_mass_indexes):
    if (b <= 18):
        underweight += 1
        print(n,"'s BMI is", b,"and is underweight")

    elif (b >= 25):
        overweight += 1
        print(n,"'s BMI is", b,"and is overweight")

    else:
        normal_weight += 1
        print(n,"'s BMI is", b,"and is a normal weight")

#outputs these totals from each if, elif or else statement
print("Total number of people that are underweight:", underweight)
print("Total number of people that are overweight:", overweight)
print("Total number of people that are normal weight:", normal_weight)




