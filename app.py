weight = 85
height = 1.85
 
bmi = weight / (height ** 2)

input( " what is your height?" )
input( "what is your weight?")
print ( bmi)

if bmi < 18.5:
    print("underweight")
    if bmi >= 25:
     print( " overweight")
else:
 print( " normal weight ")    
