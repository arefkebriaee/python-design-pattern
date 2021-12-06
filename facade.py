'''
    Facade Design Pattern
        type: Structural
'''


class Ingredient:
    def buying(self):
        return 'go to market and buying all ingredients'


class Transfer:
    def transfer(self):
        return 'transform ingredients to kitchen'


class Prepare:
    def preparing(self):
        return 'preparing ingredients'


class Cook:
    def cooking(self):
        return 'your food is cooking'


class Serv:
    def serving(self):
        return 'your food is ready.'

# ------------------------------------------------
# facade


class Restaurant:
    def cooking_food(self):
        i = Ingredient()
        i1 = i.buying()

        t = Transfer()
        t1 = t.transfer()

        p = Prepare()
        p1 = p.preparing()

        c = Cook()
        c1 = c.cooking()

        s = Serv()
        s1 = s.serving()

        return 'enjoy your food'

# ------------------------------------------------
# with useing facade design pattern:


r = Restaurant()
print(r.cooking_food())

# ------------------------------------------------
# without useing facade design pattern:


# i = Ingredient()
# print(i.buying())

# t = Transfer()
# print(t.transfer())

# p = Prepare()
# print(p.preparing())

# c = Cook()
# print(c.cooking())

# s = Serv()
# print(s.serving())
