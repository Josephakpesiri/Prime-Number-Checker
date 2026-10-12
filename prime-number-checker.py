print("========= PRIME NUMBER CHECKER =========")
print()
#collect and store number
number = int(input("Enter a number: "))
print()

#check for prime numbers
#since 1 is not a prime number, let's exclude it from the list
for checker in range(2, number): 
        #checker = number - 1
        #while checker < number:
        if number % checker == 0:
            print(f"{number} is not a prime number.")
            break
        checker += 1
else:
            print(f"{number} is a prime number.")