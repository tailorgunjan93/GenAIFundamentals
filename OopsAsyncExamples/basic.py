import time
def function1():
    time.sleep(2)
    print("Function 1 complete")
    return "Result from function 1"
def function2():
    time.sleep(3)
    print("Function 2 complete")
    return "Result from function 2"
def function3():
    time.sleep(1)
    print("Function 3 complete")
    return "Result from function 3"

def main():
    function1()
    function2() 
    function3()

if __name__ == "__main__":
    main()