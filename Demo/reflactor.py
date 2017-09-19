#!/usr/bin/python
# -*- coding: UTF-8 -*-
class Dog(object):
    def __init__(self,name):
        self.name=name
    def eat(self,food):
        print("%s is eating %s"%(self.name,food))

def bulk(self):
    print ("%s is yelling"%self.name)
dog=Dog("Tom")
#python 3.x用input
choice=raw_input(">>>>:").strip()
if hasattr(dog,choice):
    func=getattr(dog,choice)
    func("bone")
else:
    setattr(dog,choice,bulk)
    #delattr(dog,choice)
    getattr(dog,choice)(dog)