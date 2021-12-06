'''
    Proxy Design Pattern
        type: Structural
'''


class DataBase:
    def show(self):
        print("all data in database...")


class Proxy:
    admin_password = 'admin password'

    def check_admin(self):
        password = input("enter password: ")
        if password == self.admin_password:
            print("welcome, you can access to database")
            my_db = DataBase()
            my_db.show()
        else:
            print("sorry, yout can't access to database")


def operator():
    p = Proxy()
    p.check_admin()


operator()
