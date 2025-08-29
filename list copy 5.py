from user import User
from card import Card

alex = User("Alex")
mark = User("Mark")
marta = User("Marta")
nadezhda = User("Nadezhda")
vika = User("Vika")
denis = User("Denis")

alex.sayName()
alex.setAge(33)
alex.sayAge()

card = Card("1234 5678 8765 4321", "03/28", "Alex F")

alex.addCard(card)
alex.getCard().pay(1000)