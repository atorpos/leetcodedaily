class fizzbuzz:

    def fizzbuzz(self, n):
        for i in range(1,n+1):
            if(i%3==0) and (i%5==0):
                print("FizzBuzz")
            if(i/3).is_integer():
                print("Fizz")
            elif(i/5).is_integer():
                print("Buzz")
            else:
                print(n)