"""Determine if a number has a exact square root"""
def square_root(int_to_eval):
    
    response = 0
    
    while response**2 < int_to_eval:
        response +=1
        
    if response**2 == int_to_eval:
        return print(int_to_eval, "has exact square root, which is: ", response)
    else:
        return print(int_to_eval, "Does NOT have an exact square root")


def run():
    question = True

    while question:
        object_to_evaluate = int(input("Write an integer: "))
        
        square_root(object_to_evaluate)
        
        answer = input(str("\nTry another number? (yes/no)"))
        
        if answer == 'yes' or answer == 'y':
            question = True
        elif answer == 'no' or answer == 'n':
            question = False
        else:
            print("This is not a valid option!!!!")
            question = False
    
    
if __name__ == '__main__':
    run()
    
#Here we use enumeration