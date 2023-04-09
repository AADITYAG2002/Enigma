class MyClass:
    def __init__(self):
       self.value = 60

    def __new__(cls):
        return cls

obj = MyClass()
print(obj)
# Output: 42