#!/usr/bin/python
#
# Test Suite For mathquiz.py
#    test_mathquiz.py
#
# Created by: Jason M Wolosonovich
#    6/11/2015
#
# Lesson 13 - Project Attempt 1
"""
test_mathquiz.py: Test suite for mathquiz.py

@author: Jason M. Wolosonovich
"""
import unittest
from random import randint
from mathquiz import MathQuiz


class TestMathQuiz(unittest.TestCase):
    """
    Test suite for mathquiz.py
    """ 
    
    def setUp(self):
        self.quiz_type = 'add'
        self.questions = 5
        self.int_range = (1,10)
        self.low, self.high = self.int_range  
        self.quiz = MathQuiz(quiz_type=self.quiz_type,
                             questions=self.questions,
                             int_range=self.int_range)
        
    
    # replace MathQuiz.input with mock for testing string input
    def mock_input(self,s):
        return randint(self.low,
                       self.high)
    # direct input to be handled by mock
    MathQuiz.input = mock_input
    
    
    def test_good_keywords(self):
        # test allowed values for 'quiz_type'
        for quiz_type in ['add',
                          'subtract',
                          'multiply',
                          'divide']:
            try:
                MathQuiz(quiz_type=quiz_type)
            except AttributeError:
                return "Values for 'quiz_type' should not fail!"
        
        # test different values for 'questions'
        for questions in [1,
                          100,
                          1000]:
            try:
                MathQuiz(questions=questions)
            except AttributeError:
                return "Values for 'questions' should not fail!"
        
        # test different ranges for 'int_range'    
        for int_range in [(1,10),
                          (-1,-100),
                          (-100, 100)]:
            try:
                MathQuiz(int_range=int_range)
            except AttributeError:
                return "Values for 'int_range' should not fail!"
        
         
    def test_bad_keywords(self):
        # tests keyword validation
        self.assertRaises(ValueError, 
                          lambda: MathQuiz(quiz_type='division'))
        self.assertRaises(TypeError, 
                          lambda: MathQuiz(questions='5'))
        self.assertRaises(TypeError, 
                          lambda: MathQuiz(int_range=[1,
                                                      10]))
        self.assertRaises(TypeError, 
                          lambda: MathQuiz(int_range=(1.,
                                                      10.)))
    
      
    def test_change_attributes(self):
        # tests attempts to change attributes after instance-creation
        self.assertRaises(AttributeError, 
                          setattr, 
                          self.quiz, 
                          'quiz_type', 
                          'multiply')   
        self.assertRaises(AttributeError, 
                          setattr, 
                          self.quiz, 
                          'questions', 
                          10)
        self.assertRaises(AttributeError, 
                          setattr, 
                          self.quiz, 
                          'int_range', 
                          (1,100))     


if __name__=="__main__":
    unittest.main()