print("Fizzbuzz game")
print()

def fizzbuzz(a,b):
    for i in range(a,b):
        if i % 3 == 0 and i % 5 == 0:
            print(str(i) + " can be divided simultaneously per 3 and 5!")
            print("FIZZBUZZ!")
        elif i%3==0:
            print(str(i) + " can be divided per 3!")
            print("FIZZ!")
        elif i%5==0:
            print(str(i) + " can be divided per 5!")
            print("BUZZ!")
        else:
            print("Child yells " + str(i) + "!")

fizzbuzz(5,25)

