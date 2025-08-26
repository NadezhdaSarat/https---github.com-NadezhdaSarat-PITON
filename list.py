# урок1

my_heigh = 168
print(my_heigh)

my_name = "Nadezhda"
my_name = "Nadezhda Saratovceva"
print(my_name)

pet_name = input("Как зовут вашего питомца? ")
input = "Эльза"
print( "Ваш любимчик - " + pet_name)

def print_python() :
    print("Учу Python!")
print_python()  

def print_letter(let):
    print(let, end='')
    print_letter('С')
    print_letter('т')
    print_letter('у')
    print_letter('д')
    print_letter('е')
    print_letter('н')
    print_letter('т')

#урок2

age = 17

if (age < 18):
    print("ok")

else:
    print("не берем в наш лагерь")

# получить оценку

rate_as_str = input("Оцените работу оператора от 1 до 5:")
rate = int(rate_as_str)
# проверить, что оценка от 1 до 5

if(rate < 1):
    rate = 1

if(rate > 5):
    rate = 5

print(rate)
    # в зависимости от оценки предложить обратную связь    