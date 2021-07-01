print("*"*100) #this line prints 100 Asterick
print("Welcome to Health Suggestion Service")
print("Please Provide Details so that we can suggest you properly")
print("*"*100)  #this line prints 100 Asterick

#code to get the value from user

Name = input("Enter your name: ")
Age = int(input("Enter your age: "))
height = float(input("Enter your height in cm: "))
weight = float(input("Enter your weight in kg: "))
print("Your good name is ",Name)

#conditin for Ages

if Age >= 1 and Age <= 4:
    print("Your age is:",Age,"years and it seems you are Toddler now")
elif Age >=5 and Age <= 12:
    print("Your age is:",Age,"years and it seems you are Child now")
elif Age >=13 and Age <= 19:
        print("Your age is:",Age,"years and it seems you are Teen now") 
elif Age >=20 and Age <= 39:
    print("Your age is:",Age,"years and it seems you are an Adult now")
elif Age >=40 and Age <= 64:
    print("Your age is:",Age,"years and it seems you are Middle Adult now")
elif  Age >=65 :
    print("Your age is:",Age,"years and it seems you are Senior Adult")
elif Age==0:
    print("Invalid age!")
print("*"*100) #this line prints 100 Astericks

#Formula for calculating bmi

BMI = weight / (height/100)**2
print("Your BMI is: {0} \nAccording to your BMI you are: ".format(BMI), end='')

#Conditions for BMI
 
if (BMI <= 18.4): 
    print("Underweight\nHere some key components for you:-\n \nAdding snacks-High-protein and whole-grain carbohydrate snacks can help a person gain weight. \nExamples include peanut butter crackers, protein bars, trail mix, pita chips and hummus, or a handful of almonds.\n \nEating several small meals a day-Sometimes a person may be underweight because they cannot tolerate eating large meals. Instead, a person can eat several small meals throughout the day.\n \nIncorporating additional foods. A person can add calorie-dense food sources to their existing diet, such as putting slivered almonds on top of cereal or yogurt, sunflower or chia seeds on a salad or soup, or nut butter on whole-grain toast.\n \nAvoiding empty calories. Eating high-calorie foods may cause a person to gain weight, but they also have excess fats that could affect a person’s heart and blood vessels. A person should avoid foods that are high in sugar and salt.")
elif BMI <= 24.9:
    print("Healthy\nHere some key components for you:-\nDon’t drink sugar calories\nEat nuts\nAvoid processed junk food (eat real food instead)\nTake care of your gut health with probiotics and fiber.\nEat vegetables and fruits")
elif BMI <= 29.9:
    print("Over weight\nHere some key components for you:-\n \nDiet. A steady weight loss of about one pound a week is the safest way to lose weight. Your doctor can refer you to a registered dietitian if you need help in planning your diet.\n \nRegular exercise such as brisk walking, running, swimming, biking, dancing. The amount of exercise needed to lose weight is different for everyone. Talk to your healthcare professional before you begin any new exercise program.\n \nBehavior modification techniques such as:\nKeep a food diary of everything you eat.\nShop from a list and do not shop when you're hungry.\nTake a different route if you usually pass by a tempting fast food place.")
elif BMI <= 34.9 and BMI <= 39.9:
    print("Obese\nHere some key components for you:-\n \nExercise regularly. You need to get 150 to 300 minutes of moderate-intensity activity a week to prevent weight gain. Moderately intense physical activities include fast walking and swimming.\n \nFollow a healthy-eating plan. Focus on low-calorie, nutrient-dense foods, such as fruits, vegetables and whole grains. Avoid saturated fat and limit sweets and alcohol. Eat three regular meals a day with limited snacking. You can still enjoy small amounts of high-fat, high-calorie foods as an infrequent treat. Just be sure to choose foods that promote a healthy weight and good health most of the time.\n \nKnow and avoid the food traps that cause you to eat. Identify situations that trigger out-of-control eating. Try keeping a journal and write down what you eat, how much you eat, when you eat, how you're feeling and how hungry you are. After a while, you should see patterns emerge. You can plan ahead and develop strategies for handling these types of situations and stay in control of your eating behaviors.")
else:
    print("Severely obese\nHere some key components for you:-\nExercise regularly. You need to get 150 to 300 minutes of moderate-intensity activity a week to prevent weight gain. Moderately intense physical activities include fast walking and swimming.\nFollow a healthy-eating plan. Focus on low-calorie, nutrient-dense foods, such as fruits, vegetables and whole grains. Avoid saturated fat and limit sweets and alcohol. Eat three regular meals a day with limited snacking. You can still enjoy small amounts of high-fat, high-calorie foods as an infrequent treat. Just be sure to choose foods that promote a healthy weight and good health most of the time.\nKnow and avoid the food traps that cause you to eat. Identify situations that trigger out-of-control eating. Try keeping a journal and write down what you eat, how much you eat, when you eat, how you're feeling and how hungry you are. After a while, you should see patterns emerge. You can plan ahead and develop strategies for handling these types of situations and stay in control of your eating behaviors.")
print("*"*100) #this line prints 100 Asterick
print("Thanks for using our service!")