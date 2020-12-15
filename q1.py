travel_history = input('Please tell us about your recent traveled country?\n')
age = int(input('What is your age? \n'))
symptoms = input('Tell us about your symptoms \n')

travel_countries = ['china', 'korea', 'iran', 'italy', 'none']
symptoms_array = ['shortness of breath', 'fever', 'cough', 'none']

travel_weight = 0
age_weight = 0
symptoms_weight = 0

if travel_history == travel_countries[0]:
    travel_weight = 40
elif travel_history == travel_countries[1]:
    travel_weight = 30
elif travel_history == travel_countries [2]:
    travel_weight = 20
elif travel_history == travel_countries [3]:
    travel_weight = 10
elif travel_history == travel_countries [4]:
    travel_weight = 0

if age>60:
    age_weight = 20
elif 61<age<51:
    age_weight = 10
elif age<50:
    age_weight = 5

if symptoms == symptoms_array[0]:
    symptoms_weight = 50
elif symptoms == symptoms_array[1]:
    symptoms_weight = 40
elif symptoms == symptoms_array[2]:
    symptoms_weight = 30
elif symptoms == symptoms_array[3]:
    symptoms_weight = 0

total_weight = travel_weight + age_weight + symptoms_weight
print(total_weight)

if total_weight <= 50:
    print("You don’t need any medical tests \n")
elif total_weight>50 and total_weight <=60:
    print("We suggest you to have COVID-19 tested \n")
elif total_weight>60:
    print("You are strongly recommended to have COVID-19 tested")