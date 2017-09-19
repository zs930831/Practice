#!/usr/bin/python
# -*- coding: UTF-8 -*-
# 加上object为新式类，不加为经典类
class Animal(object):
    def __init__(self, name, gender):
        self.name = name
        self.gender = gender

    def tell(self):
        print("i am %s, i am %s" % (self.name, self.gender))

    def show(self):
        print ("im animal")


class People(Animal):
    # def __init__(self, name, gender, age):
    #     super(People, self).__init__(name, gender)
    #     self.age = age

    # def tell(self):
    #     print("i am %s, i am %s,i am %s years old" % (self.name, self.gender, self.age))

    def show(self):
        print ("im people")
A=People("zs","male")
A.tell()
A.show()