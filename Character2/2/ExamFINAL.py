import random


class Person:
    def __init__(self, name, health=10, mood=10, money=0, popular=0):
        self.name = name
        self.health = health
        self.mood = mood
        self.money = money
        self.popular = popular

    def __str__(self):
        return f'{self.name}: Health = {self.health}, Mood = {self.mood}, Money = {self.money}, Popularity = {self.popular}'

    def change_state(self, health=0, mood=0, money=0, popular=0):
        self.health += health
        self.mood += mood
        self.money += money
        self.popular += popular
        if self.health <= 0:
            raise Exception(f'{self.name}: GOD? God: Yes son, you DIE.')
        if self.mood <= 0:
            raise Exception(f'{self.name}: I am the best, right? Me: NUH UH.')
        if self.money < 0:
            raise Exception(f'{self.name}: NO NO NO, I AM POOR.')
        if self.popular < 0:
            raise Exception(f'{self.name}: Why am I not popular?')


people = [Person(name) for name in ['Hakari', 'Toji', 'Gege', 'Gojo', 'Yuta', 'Sukuna', 'Mahito', 'Jogo']]
actions = [{"health": -2, "mood": -3, "money": 5, "popular": 5}, {"health": 2, "mood": 3, "money": -1, "popular": -3}]

while people:
    for person in people[:]:
        action = random.choice(actions)
        try:
            person.change_state(**action)
            print(person)

            if person.money >= 1000:
                print(f'{person.name}: HEY MOM, I AM A MILLIONAIRE!')
                people = []
                break

            if person.popular >= 300:
                print(f'{person.name}: HEY, I AM POPULAR NOW!')
                people = []
                break

        except Exception as e:
            print(e)
            people.remove(person)

    if len(people) == 1:
        print(f'{people[0].name}: Nah, I`d win!')
        break
