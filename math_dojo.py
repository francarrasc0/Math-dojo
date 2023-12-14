class MathDojo:
    def __init__(self):
        self.result = 0

    def add(self, num, *nums):
        self.result += num
        for n in nums:
            self.result += n
        return self

    def subtract(self, num, *nums):
        self.result -= num
        for n in nums:
            self.result -= n
        return self

md = MathDojo()

sum_1 = md.add(5, 10, 15, 20).result
print(sum_1)

md = MathDojo()

sum_2 = md.add(5,4).result
print(sum_2)

md = MathDojo()

sum_3 = md.add(10, 23, 3).result
print(sum_3)

md = MathDojo()

sub_1 = md.add(10).subtract(5, 3).result
print(sub_1)

md = MathDojo()

sub_2 = md.add(20).subtract(4,5,1).result
print(sub_2)

md = MathDojo()

sub_3 = md.add(13).subtract(2,5).result
print(sub_3)