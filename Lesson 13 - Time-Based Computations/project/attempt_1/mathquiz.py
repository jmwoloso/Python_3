#!/usr/bin/python
#
# Program-Version Of A Math Quiz
#    mathquiz.py
#
# Created by: Jason M Wolosonovich
#    6/11/2015
#
# Lesson 13 - Project Attempt 1
"""
mathquiz.py: A math quiz!

@author: Jason M. Wolosonovich
"""
# for python 2.x
from __future__ import division 
from random import randint
from time import time




class MathQuizMixin(object):
    """
    Mixin class for mathquiz.py. Contains methods that actually produce
    the questions for each quiz and scores the quiz. Does the
    heavy-lifting for mathquiz.py
    """
    
    def quiz_report(self, questions, times_list, answers_list):
        """
        Formats quiz results and prints them.
        """
        # calculate average time per question
        self.avg_time = round(times_list[-1] / questions, 1)
        # format results output
        for i in range(questions):
            print("Question #{0} took about {1} seconds and was {2}"
                  .format(i+1,
                          round(times_list[i]),
                          answers_list[i]))
        print("You took {0} seconds to finish the quiz"
              .format(round(times_list[-1])))
        print("Your average time was {0} seconds per question"
              .format(self.avg_time))
        
       
    def get_question(self, quiz_type, int_range):    
        """
        Internal. Question generator function.
        """
        # get low and high values for creating randints
        self.low, self.high = int_range
        while True:
            # generate random integers for each question
            int1 = randint(self.low, self.high)
            int2 = randint(self.low, self.high)
            
            # lookup dict
            quiz_type_lookup = {'add': ['plus',
                                        int1 + int2],
                                'subtract': ['minus',
                                             int1 - int2],
                                'multiply': ['times',
                                             int1 * int2],
                                'divide': ['divided by',
                                           int1 // int2]
                                }
            
            # send question back and gather response
            yield (input("What is {0} {1} {2}? "\
                         .format(int1,
                                 quiz_type_lookup[quiz_type][0],
                                 int2)),
                   # also send back correct answer
                   quiz_type_lookup[quiz_type][1])
    
    
    def start_quiz(self, quiz_type, questions, int_range):
        """
        Internal use. Starts the quiz.
        """
        # get quiz start time
        self._quiz_start = time()
        # initialize question generator
        self._question = self.get_question(quiz_type,
                                           int_range)
        while self._counter < questions:
            
            # get question start time
            self.start = time()
            # get question/answer combo
            self._response, self._answer = next(self._question)
            # get question end time
            self.stop = time()
            if int(self._response) == self._answer:
                # append 'right' if answered correctly
                self._answers_list.append('right')
                print("{0} is right!".format(int(self._response)))
                
            else:
                # append 'wrong' if answered incorrectly
                self._answers_list.append('wrong')
                print("{0} is wrong!".format(int(self._response)))
            # get time it took to finish question            
            self._times_list.append(self.stop - self.start)
            # increment counter and loop move to next iteration
            self._counter += 1
        
        # get quiz end time
        self._quiz_stop = time()
        # calculate how long quiz took
        self._times_list.append(self._quiz_stop - self._quiz_start)
        # process results and format output, then display results
        self._quiz_report = self.quiz_report(self._questions,
                                             self._times_list,
                                             self._answers_list)
        
            
          
class MathQuiz(MathQuizMixin):
    """
    MathQuiz class. After initializing a MathQuiz instance,
    (e.g. quiz = MathQuiz()), use the start() method to 
    begin the quiz (e.g. quiz.start())
    
    Options for **kwargs:
    
        'quiz_type': str; specifies the type of math quiz; choose one of 
                          'add', 'subtract', 'multiply' or 'divide'
                          default='add'
        
        Note: 'divide' is the equivalent of floor division 
               (e.g. 3 // 4 == 0; 
                     4 // 3 == 1)
    
        'questions': int; number of questions to generate 
                          default=5
        
        'int_range': tuple; specifies the range (low, high) inclusive
                                for generating random integers for each
                                question.
                            default=(1,10)
        
    """
    
    def __init__(self, quiz_type='add', questions=5, int_range=(1,10)):
        """
        Generates a new math quiz (MathQuiz instance)
        
        """
        # create instancce variables
        self.quiz_type = quiz_type
        self.questions = questions
        self.int_range = int_range
        # deifne containers
        self._answers_list = []
        self._times_list = []
        self._counter = 0
        
               
    @property
    def quiz_type(self):
        return self._quiz_type
    
    @quiz_type.setter
    def quiz_type(self, value):
        # can only be set upon instantiation
        if hasattr(self, 'quiz_type'):
            raise AttributeError("'quiz_type' can only be set once for an instance")
        # test that it is a string
        if not isinstance(value, str):
            raise TypeError("'quiz_type' must be of type 'str'")
        # make sure that the string is a valid option
        if value not in ['add',
                         'subtract',
                         'multiply',
                         'divide']:
            raise ValueError("'quiz_type' must be one of 'add', "+\
                             "'subtract', 'multiply', 'divide'")
        self._quiz_type = value
     
        
    @property
    def questions(self):
        return self._questions
    
    @questions.setter
    def questions(self, value):
        # can only be set during instantiation
        if hasattr(self, 'questions'):
            raise AttributeError("'questions' can only be set once for an instance")
        # make sure it is an int
        if not isinstance(value, int):
            raise TypeError("'questions' must be of type 'int'")
        self._questions = value
    
        
    @property
    def int_range(self):
        return self._int_range
    
    @int_range.setter
    def int_range(self, value):
        # can only be set during instantiation
        if hasattr(self, 'int_range'):
            raise AttributeError("'int_range' can only be set once for an instance")
        # get low, high from int_range for validation
        low, high = value
        # make sure it is a tuple
        if not isinstance(value, tuple):
            raise TypeError("'int_range' must be of type 'tuple'")
        # make sure each item in the tuple is an int
        if not isinstance(low, int) or not isinstance(high, int):
            raise TypeError("tuple values must be of type 'int'")
        self._int_range = value
    
        
    def start(self):
        # start the quiz!       
        self._start_quiz = self.start_quiz(self._quiz_type,
                                           self._questions,
                                           self._int_range) 
        
           
def main():
    """
    Main loop for mathquiz.py when run directly.
    """
    MathQuiz()


if __name__=="__main__":
    main()    