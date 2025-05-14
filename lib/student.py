#!/usr/bin/env python

from user import User

class Student(User):
    def __init__(self, first_name, last_name, knowledge=None):
        self.first_name = first_name
        self.last_name = last_name
        self.knowledge = []
        
    
    def learn(self, New_information):
        self.knowledge = (New_information)