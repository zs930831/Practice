#!/usr/bin/python
# -*- coding: UTF-8 -*-
class Flight(object):
    def __init__(self, name):
        self.flight_name = name
    def check_flightstatus(self):
        print ("the flight is %s" % (self.flight_name))
        return 0
    @property
    def flightstatus(self):
        status = self.check_flightstatus()
        if (status == 0):
            print("ready to fly")
        elif status == 1:
            print("already fly")

    @flightstatus.setter
    def flightstatus(self, status):
        print ("change flight status into %s" % (status))


f = Flight("CA222")
f.flightstatus
f.flightstatus = 1
