from cal_fun import do_addition
from cal_fun import do_substraction

def main():
    print("welcome to the calculator app")
    print("""\ select the function from the give options:
          1. Add
          2. Subtract
          
          
          """)
    user_input=input("select the input")
    
    a=int(input("values of a"))
    b=int(input("values of b"))

    
    if user_input=='1':
        result=do_addition(a,b)
    elif  user_input=='2':
        result=do_substraction(a,b)
    print('result',result)
    
if __name__=='__main__':
    main()