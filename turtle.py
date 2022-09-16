'''
Project Name:
Author:
Due Date: YYYY-MM-DD
Course: CS1400-zzz

Put your description here, lessons learned here, and any other information
someone using your program would need to know to make it run.
'''
# (3) add functions here that your main program calls
# to do stuff.

def main():
    '''
    Program starts here.
    '''
    try:
        # (1) replace pass with your code
        height = int(input("Enter height:"))
        width = int(input("Enter width:"))

        pass
    except ValueError:
        print('Width and height must be positive integers.')
        return

    if width < 1 or height < 1:
        print('Width and height must be positive integers.')
        return

    import turtle
    
    # (2) replace pass with your code
    pass

if __name__ == "__main__":
    main()
