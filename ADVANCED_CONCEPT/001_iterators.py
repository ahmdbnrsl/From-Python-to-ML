class MyIterator:
    def __init__(self, start, end):
        self.current = start
        self.end = end

    def __iter__(self):
        return self

    def __next__(self):
        if self.current > self.end:
            raise StopIteration
        value = self.current
        self.current += 1
        return value

# Menggunakan iterator
my_iter = MyIterator(1, 5)
for num in my_iter:
    print(num)
# Output: 1 2 3 4 5

# iterator untuk angka genap dari 1 - 20
class Genap:
    def __init__(self, start, end):
        self.current = start
        self.end = end

    def __iter__(self):
        return self

    def __next__(self):
        if self.current > self.end:
            raise StopIteration
        if self.current % 2 != 0:
            self.current += 1
        value = self.current
        self.current += 2
        return value

genap = Genap(6, 20)
print(genap)
for num in genap:
    print(num)