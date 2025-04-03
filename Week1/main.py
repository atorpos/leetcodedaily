# This is a sample Python script.
from AMZA_OA.code02 import Code02
from Solution1 import Solution1
from Week1.mergearray import mergearray
from Week1.twosum import twosum
from Week3.containsDuplicateii import containsDuplicateii
from Week3.diameterBinaryTree import diameterBinaryTree
from Week3.longestcommonprefix import longestCommonPrefix
from Week3.minimumAbsoluteDifference import minimumAbsoluteDifference
from Week3.palindromenumber import palindromenumber
from Week3.reorganizesting import reorganizestring
from Week3.climbstairs import climbStairs
from lexicographic.lexicographic01 import lexicographic01
from lexicographic.lexicographic02_subarray import lexicographic02_subarray
from solution2 import solution2
from oatrial01 import oatrial
from surroundingzero import surrandingzero
from Week3.validAnagram import validAnagram
from Week3.arrayRankTransform import arrayRankTransform


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
    twosum = twosum()
    mergearray = mergearray()
    codetwo = Code02()
    lex_01 = lexicographic01()
    lex_02 = lexicographic02_subarray()
    palindrom = palindromenumber()
    longestCommonPrefix = longestCommonPrefix()
    climbStairs = climbStairs()
    validAnagram = validAnagram()
    diameterBinaryTree = diameterBinaryTree()
    containsDuplicateii = containsDuplicateii()
    minimumAbsoluteDifference = minimumAbsoluteDifference()
    arrayRankTransform = arrayRankTransform()

    reorganstring = reorganizestring()

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

    nums = [2,7,11,5]
    target = 9
    print(twosum.twoSum(nums, target))

    num1 = [1,2,3,0,0,0]
    num2 = [2,5,6]
    m = 3
    n = 3

    mergearray.merge(num1, m, num2, n)
    print(codetwo.getMinimumString("04829"))

    print(lex_01.lexicalOrder(11))

    print(lex_02.numOfSubarrays([2,4,6]))

    palindrom.isPalindrome(121)

    print(longestCommonPrefix.longestCommonPrefix(["",""]))
    print(f"the climbStairs is {climbStairs.climbstairs(44)}")
    print(f"the validAnagram is {validAnagram.isAnagram('anagram', 'nagaram')}")

    # print(f"the diameterBinaryTree is {diameterBinaryTree.diameterOfBinaryTree([1,2,3,4,5])}")
    print(f"contains duplicate ii is {containsDuplicateii.containsNearbyDuplicate([1,2,3,1], 3)}")
    print(f"Minim is {minimumAbsoluteDifference.minimumabsolutedifference([4,2,3,1])}")

    print(f"the reorganizestring is {reorganstring.reorganizeString('aab')}")
    print(f"the array Ranks Trans is {arrayRankTransform.arrayranktransform([37,12,28,9,100,56,80,5,12])}")


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
