class A:
    def add(self, datatype, *args):
        if datatype == 'int':
            answer = 0

        if datatype == 'string':
            answer = ""

        for x in args:
            answer = answer + x
        print(answer)


a = A()
a.add('int', 2, 3)
a.add('int', 2, 3, 4)

a.add('string', 'hi', 'bye')
a.add('string', 'hi', 'bye', 'welcome')
