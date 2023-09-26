#Задание2
name = input("Имя:")
country = input("Страна:")
place_of_residence = input("Город, в котором проживаете:")
year = int(input("Возраст:"))
gender = input("Ваш пол:")
year_now = 2023
if gender == "женский" or gender == "Женский":
    print("Уважаемая", name,"!",
          "\nНа сегодняшний день Вы проживаете в стране", country, "в городе",
          place_of_residence, "и вы родились в", (year_now - year))
else:
    print("Уважаемый", name,"!","\nНа сегодняшний день Вы проживаете в стране", country, "в городе",
          place_of_residence, 'и вы родились в', (year_now - year))