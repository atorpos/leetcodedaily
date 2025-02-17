# This is a sample Python script.
from Solution1 import Solution1


# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    sol = Solution1()
    print_hi('PyCharm')
    candies1 = [1,3,4,5,2]
    extraCandies = 2
    print(sol.kidsWithCandies(candies1, extraCandies))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
