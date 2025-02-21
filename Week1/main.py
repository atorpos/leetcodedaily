# This is a sample Python script.
from Solution1 import Solution1
from solution2 import solution2
from oatrial01 import oatrial
from surroundingzero import surrandingzero


# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    sol = Solution1()
    sol2 = solution2()
    oatrial01 = oatrial()
    surrandingzero01 = surrandingzero()
    print_hi('PyCharm')
    candies1 = [1,3,4,5,2]
    extraCandies = 2
    print(sol.kidsWithCandies(candies1, extraCandies))

    intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]
    print(sol2.merge(intervals))
    print(sol2.merge_intervals(intervals))

    print(oatrial.get_key_identifier("baab"))
    print(oatrial.get_key_identifier("pop"))
    print(oatrial.get_key_identifier("abcccbadse"))

    print(oatrial.calculate_min_total_wattage([4, 9, 2, 10, 3, 5, 3], 3))

    print(oatrial.get_maximum_greyness(["101","000","122","434"]))
    center = [3, 1, 6, 8, 9]
    destination = [2, 3, 1, 7, 9]
    print(oatrial.calculate_minimum_distance(center, destination))

    matrix = [["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]]

    print(surrandingzero01.surround_with_zero(matrix))

    case_one="001101"

    print(surrandingzero01.numberOfWays(case_one))

    max_sum_subarray = [1,2,3,4,5]

    k = 5120

    print(surrandingzero01.maxmumSubarraySum(max_sum_subarray, k))

    print(surrandingzero01.kthKactor(7, 2))

    letterwords = "seacfcde"
    print(surrandingzero01.partitionString(letterwords))

    paragraph = "Bob hit the ball, the hit Ball flew far away it was hit"

    print(surrandingzero01.mostCommonWord(paragraph, ["hit"]))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
