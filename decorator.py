'''
    Decorator Design Pattern
        type: Structural
'''

# -----------------------------------------
# decorator pattern


class LoginDecorator:
    def login(self, username, password):
        self.username = username
        self.password = password

        if self.username == 'admin' and self.password == 'admin':
            return True


def check_login(func):
    def inner_login():
        username = input("enter your username: ")
        password = input("enter your password: ")

        l1 = LoginDecorator()
        resault = l1.login(username, password)

        if resault:
            func()
        else:
            print("username or password is incorrect")

    return inner_login
# -----------------------------------------
# main code


class CreateBlog:
    def create(self, name, category):
        self.blog_name = name
        self.blog_category = category

        print(
            f"your blog, {self.blog_name} in {self.blog_category} category created succesfully.")


@check_login
def blog_creator():
    blog_name = input("enter blog name: ")
    blog_category = input("enter blog category: ")
    blog = CreateBlog()
    blog.create(blog_name, blog_category)


# -----------------------------------------
blog_creator()
