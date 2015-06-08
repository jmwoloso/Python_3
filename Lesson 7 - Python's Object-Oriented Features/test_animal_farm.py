#!/usr/bin/python
#
# Test Suite For animal_farm.py
#    test_animal_farm.py
#
# Created by: Jason M Wolosonovich
#    6/04/2015
#
# Lesson 7 - Exercise 1
"""
test_animal_farm.py: Test suite for animal_farm.py

@author: Jason M. Wolosonovich
"""
import unittest
from animal_farm import Animal, Pig, Dog, Chicken

class TestAnimals(unittest.TestCase):
    
    def test_base_animal_class(self):
        """
        Test the basics of the Animal class
        """
        animal = Animal("Orwell")
        self.assertRaises(NotImplementedError, animal.sound)
        self.assertFalse(animal.has_wings())
        
    def test_pig(self):
        """
        Tests the inhabitants of the farm
        """
        pig = Pig("Napoleon")
        self.assertEqual(pig.sound(), "oink!")
        self.assertFalse(pig.has_wings())
        
    def test_dog(self):
        dog = Dog("Bluebell")
        self.assertEqual(dog.sound(), "woof!")
        self.assertFalse(dog.has_wings())
        
    def test_chicken(self):
        chicken = Chicken("Kulak")
        self.assertEqual(chicken.sound(), "bok bok!")
        self.assertTrue(chicken.has_wings())
        
if __name__=="__main__":
    unittest.main()