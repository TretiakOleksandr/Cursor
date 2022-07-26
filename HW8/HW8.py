# 1. Implement class iterator for Fibonacci numbers. Iterator get numbers of first Fibonacci numbers
print("-1-----------------------------------------------")
class FibonacciNumbers:
    def __init__(self, num):
        self.num = num
        self.fib_list = [0, 1]
        self.i = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.i > self.num:
            raise StopIteration
        result = self.fib_list[self.i]
        self.i += 1
        self.fib_list.append(self.fib_list[-1] + self.fib_list[-2])
        return  result

for i in FibonacciNumbers(10):
    print(i)

# 2. Implement generator for Fibonacci numbers
print("-2-----------------------------------------------")
def fibonacci_gen(num):
    fib_list = [0, 1]
    i = 0
    while i <= num:
        result = fib_list[i]
        i += 1
        fib_list.append(fib_list[-1] + fib_list[-2])
        yield result

for j in fibonacci_gen(10):
    print(j)

# 3. Write generator expression that returns square numbers of integers from 0 to 10
print("-3-----------------------------------------------")
sqNumGen = (i**2 for i in range(11))

for k in sqNumGen:
    print(k)

# 4. Implement coroutine for accumulation arithmetic mean
print("-4-----------------------------------------------")
def accumulation_mean():
    sum = 0
    ind = 0
    while True:
        in_ = yield
        sum += in_
        ind += 1
        print(int(sum/ind))

acc_mean = accumulation_mean()
next(acc_mean)
acc_mean.send(2)
acc_mean.send(8)
acc_mean.send(2)
acc_mean.send(4)
