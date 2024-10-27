sonlar=[2, 6, 4, 3, 8, 5]
def func1(list1):
    def func2():
        print(f"minimal son {min(list1)}")
        print(f"maximal son {max(list1)}")
    func2()
    def func3():
        kvadrat =[]
        for i in list1:
            kvadrat.append(i**2)
        print(kvadrat)
    func3()
    def func4():
        for i in list1:
            javob = i/2
            print(javob)
    func4()
    def func5():
        javob1=1
        for i in list1:
            javob1*=i
            print(javob1)
    func5()
    def func6():
        yigindi =0
        for i in list1:
            yigindi+=i
        print(yigindi)
    func6()
func1(sonlar)

