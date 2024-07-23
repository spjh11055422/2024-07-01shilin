import index
def main():
    p1 = index.getPerson(name="楊凱")
    print(p1.bmi_print())
    print("=============")
    p2 = index.Person.getPerson(name='楊凱')
    print(p2.bmi_print())
    print('==================================================================================================================================================================================================')
    p3 =index.Person.getPerson1(name='楊凱')
    print(p3.bmi_print())

if __name__ == '__main__':
    main()
   