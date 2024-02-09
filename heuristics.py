import heapq
def base_heuristic(_pancake_state):
    heuristic_val = 0
    list_pancakes = _pancake_state.state_list
    max_pancake = _pancake_state.N

    for i in range(max_pancake):
        if int(list_pancakes[i]) == max_pancake - i:
            i += 1
            continue
        heuristic_val = (max_pancake -i)*(max_pancake -i+1) // 2
        break
    return heuristic_val


def advanced_heuristic(_pancake_state):
    ##by the position
    val = _pancake_state.heuristics_dict.get(_pancake_state.get_state_str())
    if val:
        return val
    heuristic_val = 0
    list_pancakes = list(map(int, _pancake_state.state_list))
    list_for_dict = ','.join(map(str, list_pancakes))
    max_pancake = _pancake_state.N
    sorted_list = list(range(max_pancake, 0, -1))
    i = 0
    counter = 0
    while i < max_pancake - 1:
        if list_pancakes[i] == max_pancake - i:
            i += 1
            continue
        else:
            if counter == 1:
                heuristic_val += (max_pancake - i) * (max_pancake - i + 1) // 2
                break
            maximum = sorted_list[i]
            index_maximum = list_pancakes.index(maximum)
          #  print(f'maximum val  is {maximum} at index {index_maximum}')

            if index_maximum < max_pancake - 1:
                heuristic_val += sum(list_pancakes[index_maximum:])
            heuristic_val += (max_pancake - i) * (max_pancake - i + 1) // 2
            counter += 1

          #  print(f'hur val is {heuristic_val}')

            flip = list_pancakes[:index_maximum] + list_pancakes[index_maximum:][::-1]
            flop = flip[:i] + flip[i:][::-1]
          #  print(f'after flip {flip} flop is:{flop}')
            list_pancakes = flop
            i += 1
    _pancake_state.heuristics_dict[list_for_dict] = heuristic_val
  #  print(_pancake_state.heuristics_dict)
    return heuristic_val

    ###by the maximum
    # val = _pancake_state.heuristics_dict.get(_pancake_state.get_state_str())
    # if val:
    #     return val
    # heuristic_val = 0
    # list_pancakes = list(map(int, _pancake_state.state_list))
    # list_for_dict = ','.join(map(str,list_pancakes))
    # max_pancake = _pancake_state.N
    # sorted_list = list(range(max_pancake ,0, -1))
    # i= 0
    # while i < max_pancake-1:
    #     if list_pancakes[i] == max_pancake - i:
    #         i += 1
    #         continue
    #     else:
    #         maximum = sorted_list[i]
    #         index_maximum = list_pancakes.index(maximum)
    #         print(f'maximum of {list_pancakes} is:{maximum}, at index {index_maximum}')
    #         if index_maximum < max_pancake -1:
    #             heuristic_val += sum(list_pancakes[index_maximum:])
    #         heuristic_val += (max_pancake -i)*(max_pancake -i+1) // 2
    #         print(f'hur val is {heuristic_val}')
    #
    #         flip = list_pancakes[:index_maximum] + list_pancakes[index_maximum:][::-1]
    #         flop = flip[:i]+flip[i:][::-1]
    #         print(f'after flip {flip} flop is:{flop}')
    #
    #         list_pancakes = flop
    #         i += 1
    # _pancake_state.heuristics_dict[list_for_dict] = heuristic_val
    # print(_pancake_state.heuristics_dict)
    # return heuristic_val

    # heuristic_val = 0
    # list_pancakes = _pancake_state.state_list
    # max_pancake = _pancake_state.N
    #
    # for i in range(max_pancake):
    #     if int(list_pancakes[i]) == max_pancake - i:
    #         i += 1
    #         continue
    # #     else:
    # #         heuristic_val += (max_pancake - i) * (max_pancake - i + 1) // 2
    # #
    # #
    # # return heuristic_val
    #
    # val = _pancake_state.heuristics_dict.get(_pancake_state.get_state_str())
    # if val:
    #     return val
    # pancake_list = _pancake_state.state_list
    # sum_ = 0
    # goal_state_reversed = ','.join(map(str, range(1, _pancake_state.N + 1)))
    # reversed_heuristic_val = sum(range(1, _pancake_state.N + 1))
    #
    # if goal_state_reversed == _pancake_state.state_str:
    #     return reversed_heuristic_val
    #
    # i = 2
    # # flag = True
    # while i < len(pancake_list):
    #     diff = int(pancake_list[-(i + 1)]) - int(pancake_list[-i])
    #
    #     if diff > 1 or diff < -1:
    #         sum_ += sum(map(int, pancake_list[_pancake_state.N - i:]))
    #         _pancake_state.heuristics_dict[str(pancake_list[:_pancake_state.N - i] + pancake_list[_pancake_state.N - i:][::-1])] = sum_
    #         i += 1
    #     elif diff == -1:
    #         # i += 1
    #         # if i >= len(pancake_list):
    #         #     sum_ += sum([int(x) for x in pancake_list[_pancake_state.N - i:]])
    #         #     break
    #         while int(pancake_list[-(i + 1)]) - int(pancake_list[-i]) == -1:
    #             i += 1
    #             if i >= len(pancake_list):
    #                 # flag = False
    #                 break
    #         sum_ += sum(map(int, pancake_list[_pancake_state.N - i:]))  # Add sum from before
    #         _pancake_state.heuristics_dict[str(pancake_list[:_pancake_state.N - i] + pancake_list[_pancake_state.N - i:][::-1])] = sum_
    #         i += 1
    #     else:
    #         i += 1
    #     # if pancake_list[0] != str(_pancake_state.N) and not flag and i > len(pancake_list):
    #     #     sum_ += reversed_heuristic_val
    #     # if pancake_list[0] != str(_pancake_state.N) and i == len(pancake_list): ####not going into this...
    #     #     sum_ += reversed_heuristic_val  # Add from the maximum
    #     #     _pancake_state.heuristics_dict["XXXXX"] = sum_
    # return sum_

    # val = _pancake_state.heuristics_dict.get(_pancake_state.get_state_str())
    # if val:
    #     return val
    # heuristic_val = 0
    # list_pancakes = _pancake_state.state_list
    # max_pancake = _pancake_state.N
    # n= max_pancake
    # max_index = 0
    #
    # while n > 1:
    #     for i in range(1, max_pancake):
    #         if list_pancakes[i] > list_pancakes[max_index]:
    #             max_index = i
    #     if max_index != n - 1:
    #         start = 0
    #         while start < max_index:
    #             list_pancakes[start], list_pancakes[i] = list_pancakes[i], list_pancakes[start]
    #             start += 1
    #             i -= 1
    #     n -= 1
    #
    # state = list(map(int, _pancake_state.state_list))
    # n = _pancake_state.N
    #
    # # Ideal sorted state in descending order
    # ideal_state = list(range(n, 0, -1))
    #
    # # Sum the weights of Misplaced Pancakes
    # misplaced_weight = sum(state[i] for i in range(n) if state[i] != ideal_state[i])
    #
    # # Sequence Order Analysis (counting breaks in the sequence)
    # # The cost of fixing a break in the sequence is the sum of the weights from the break to the top
    # sequence_breaks_cost = sum(state[i] for i in range(1, n) if state[i] - state[i - 1] != 1)
    #
    # # heuristic_value = misplaced_weight + sequence_breaks_cost
    #
    # return heuristic_value

    #
    #
    #
    #
    #
    # heuristic_val = 0
    # list_pancakes = list(map(int, _pancake_state.state_list))
    # max_pancake = _pancake_state.N
    #
    # for i in range(max_pancake):
    #     if list_pancakes[i] == max_pancake - i:
    #         i += 1
    #         continue
    #     else:
    #         #for all the flip:
    #         heuristic_val += (max_pancake - i) * (max_pancake - i + 1) // 2
    #         for j in range(i, max_pancake):
    #             new_pancake_list = list_pancakes[:i]+list_pancakes[i:][::-1]
    #             if list_pancakes[j] == max_pancake - i:
    #                 j+= 1
    #                 continue
    #             else:
    #                 heuristic_val += (max_pancake - i) * (max_pancake - i + 1) // 2
    #                 j+=1
    #         i+=1
    #         continue
    #
    # return heuristic_val
    #
    #
    # # Combine the heuristics
    #
    #
