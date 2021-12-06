'''
    Factory Design Pattern:
        type: Creational
        3 component: creator, product, client
'''

from abc import ABC, abstractmethod

# -------------------------------------------
# creator section


class Creator(ABC):
    @abstractmethod
    def make(self):
        pass

    def editor_file(self):
        editor = self.make()
        resault = editor.product()
        return resault


class Pdf_Creator(Creator):
    def make(self):
        return Pdf_Product()


class Txt_Creator(Creator):
    def make(self):
        return Txt_Product()
# -------------------------------------------
# product section


class Product(ABC):
    @abstractmethod
    def product(self):
        pass


class Pdf_Product(Product):
    def product(sefl):
        return "editing PDF file ..."


class Txt_Product(Product):
    def product(self):
        return "editing TXT file ..."


# -------------------------------------------
# client section
def client(format):
    return format.editor_file()


print(client(Txt_Creator()))
