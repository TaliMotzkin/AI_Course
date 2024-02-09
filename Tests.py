from heuristics import *
from unittest import TestCase
from pancake_state import *
from search import *
import time

class TestPancake(TestCase):
    def test_basic(self):
        pancake_input1 = pancake_state("1,3,2,4")
        pancake_input2 = pancake_state("4,3,2,1")
        pancake_input3 = pancake_state("4,2,3,1")
        pancake_input4 = pancake_state("5,4,3,1,2")
        pancake_input5 = pancake_state("5,3,4,1,2")

        self.assertEqual(base_heuristic(pancake_input1), 10, msg="Error in __base1__")
        self.assertEqual(base_heuristic(pancake_input2), 0, msg="Error in __base2__")
        self.assertEqual(base_heuristic(pancake_input3), 6, msg="Error in __base3__")
        self.assertEqual(base_heuristic(pancake_input4), 3, msg="Error in __base4__")
        self.assertEqual(base_heuristic(pancake_input5), 10, msg="Error in __base5__")


    def test_g_match(self):
        pancake_input1 = pancake_state("1,3,2,4,6,5,7,9,8")
        goal_input1 = "9,8,7,6,5,4,3,2,1"
        our_heuristic1 = advanced_heuristic(pancake_input1)
        real_value1 = search(pancake_input1, advanced_heuristic, goal_input1)[1]

        self.assertLess(our_heuristic1,real_value1 , msg=f'if our value:{our_heuristic1} bigger then the real:{real_value1}' )

        # pancake_input2 = pancake_state("8,9,5,6,7,3,2,1,4")
        # goal_input2 = "9,8,7,6,5,4,3,2,1"
        # our_heuristic2 = advanced_heuristic(pancake_input2)
        # real_value2 = search(pancake_input2, advanced_heuristic, goal_input2)[1]
        #
        # self.assertLess(our_heuristic2, real_value2,
        #                  msg=f'if our value:{our_heuristic2} bigger then the real:{real_value2}')
        #
        # pancake_input3 = pancake_state("9,8,7,6,4,3,5,2,1")
        # goal_input3 = "9,8,7,6,5,4,3,2,1"
        # our_heuristic3 = advanced_heuristic(pancake_input3)
        # real_value3 = search(pancake_input3, advanced_heuristic, goal_input3)[1]
        #
        # self.assertLess(our_heuristic3, real_value3,
        #                  msg=f'if our value:{our_heuristic3} bigger then the real:{real_value3}')

class TimerTest(TestCase):
    def setUp(self):
        # Start the timer
        self.start_time = time.time()

    def test_base(self):
        # Example test
        pancake_input5 = pancake_state("5,3,4,1,2")
        self.assertEqual(base_heuristic(pancake_input5), 10, msg="Error in __base5__")

    def tearDown(self):
        # Stop the timer
        t = time.time() - self.start_time
        print(f"{self.id()}: {t:.3f} seconds")

    def test_neighboors(self):
        pancake_input1 = pancake_state("1,3,2")
        res1 = pancake_input1.get_neighbors()

        pancake_input2 = pancake_state("4,3,2,1")
        res2 = pancake_input2.get_neighbors()

        pancake_input2 = pancake_state("1,2")
        re3 = pancake_input2.get_neighbors()

        pancake_input2 = pancake_state("5,6,3,4,1,2")
        res4 = pancake_input2.get_neighbors()

        self.assertEqual(res1, [(pancake_state("2,3,1"),6),(pancake_state("1,2,3"),5)], msg="Error in __base1__")
        self.assertEqual(res2, [(pancake_state("1,2,3,4"),10),(pancake_state("4,1,2,3"),6), (pancake_state("4,3,1,2"),3)], msg="Error in __base1__")
        self.assertEqual(re3, [(pancake_state("2,1"),3)], msg="Error in __base1__")
        self.assertEqual(res4, [(pancake_state("2,1,4,3,6,5"),21),(pancake_state("5,2,1,4,3,6"),16), (pancake_state("5,6,2,1,4,3"),10), (pancake_state("5,6,3,2,1,4"),7), (pancake_state("5,6,3,4,2,1"),3)], msg="Error in __base1__")

