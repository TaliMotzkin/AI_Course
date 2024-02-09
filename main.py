from search import search
from pancake_state import pancake_state
from heuristics import *
import time
import random

if __name__ == '__main__':
    #
    # goal_state = "4,3,2,1"
    # pancake_input = "1,2,4,3"
    # sum = [13, 16, 23, 31, 36]
    # pancake_state1 = pancake_state(pancake_input)
    # search_result = search(pancake_state1, advanced_heuristic, goal_state)

    # goal_state2 = "7,6,5,4,3,2,1"
    # pancake_input2 = "7,6,4,5,1,2,3"
    # pancake_state2 = pancake_state(pancake_input2)
    # search_result2 = search(pancake_state2, base_heuristic, goal_state2)
    #
    lst = list(range(1, 9))

    for i in range(len(lst)):
        lst[i] = str(lst[i])

    '''
    goal
    '''
    goal_lst = lst.copy()
    goal_lst.reverse()
    goal = ','.join(goal_lst)

    '''
    random lists
    '''
    for i in range(9):
        lst1 = lst.copy()
        random.shuffle(lst1)
        state = ','.join(lst1)
        goal_state = goal
        pancake_input = state
        start2 = time.time()
        pancake_state2 = pancake_state(pancake_input)
        search_result2 = search(pancake_state2, advanced_heuristic, goal_state)
        end2 = time.time()
        print(f"10 pancakes: {state} time: {end2 - start2} goal: {goal}")

    # lst = list(range(1, 14))
    #
    # for i in range(len(lst)):
    #     lst[i] = str(lst[i])
    #
    # '''
    #     goal
    #     '''
    # goal_lst = lst.copy()
    # goal_lst.reverse()
    # goal = ','.join(goal_lst)
    #
    # '''
    # random lists
    # '''
    # for i in range(10):
    #     lst1 = lst.copy()
    #     random.shuffle(lst1)
    #     state = ','.join(lst1)
    #     goal_state = goal
    #     pancake_input = state
    #     start2 = time.time()
    #     pancake_state2 = pancake_state(pancake_input)
    #     search_result2 = search(pancake_state2, advanced_heuristic, goal_state)
    #     end2 = time.time()
    #     print(f"11 pancakes: {state} time: {end2 - start2} goal: {goal}")

    # start1 = time.time()
    # pancake_state1 = pancake_state(pancake_input)
    # search_result1 = search(pancake_state1, base_heuristic, goal_state)
    # end1 = time.time()
    # print(end1 - start1)
    # for i in (search_result1):
    #     print(i.state.get_state_str())





    # start3= time.time()
    # goal_state1 = "8,7,6,5,4,3,2,1"
    # pancake_state3 = pancake_state("2,4,5,6,8,7,1,3")
    # search_result3 = search(pancake_state3, advanced_heuristic, goal_state1)
    # end3 = time.time()
    # print(f"time: {end3 - start3}")

    # start3 = time.time()
    # pancake_state3 = pancake_state('1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20')
    # search_result3 = search(pancake_state3, advanced_heuristic, '20,19,18,17,16,15,14,13,12,11,10,9,8,7,6,5,4,3,2,1')
    # end3 = time.time()
    # print(f"time: {end3 - start3}")
    # for i in (search_result3):
    #     print(i.state.get_state_str())



