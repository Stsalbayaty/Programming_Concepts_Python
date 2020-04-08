mealCharge = float(input("Enter the cost of the meal: $"))

taxAmt = mealCharge * .07 

tipAmt = mealCharge * .2

totalMeal = mealCharge + taxAmt + tipAmt

print ("For a meal charge of $" + str(mealCharge)  + " the tax will be $" + str(taxAmt)  + " and the tip amount will be $" + str(tipAmt)  + " for a total bill of $" + str(totalMeal))