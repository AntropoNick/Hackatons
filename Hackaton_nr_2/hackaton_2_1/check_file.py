import os

def do_this_with_file (filename,operation,content):
    if operation=='read':
        if os.path.isfile(filename):
            with open(filename, 'r') as fopen:
                if os.path.getsize(filename)==0:
                    print (f'This file {filename} is empty')
                else:
                    print(f"Read file {filename}")
                    return fopen.read()
        else:
            print (f"This file {filename} doesn't exist ")
    elif operation =='write':
        if os.path.isfile(filename):
            with open(filename, 'w') as fopen:
                while True:
                    answer=str(input(f"File  {filename} already exist . Overwride this file? Y/N: "))
                    if answer=='Y':
                        #with open(filename, 'w') as fopen:
                        fopen.write(content)
                        break
                    elif answer=='N':
                        print(f"File {filename} wasn't save ")
                        break
                    else:
                        print ("Incorrect answer. Try again")
        else:
            with open(filename, 'w') as fopen:
                print (f"Save to file {filename}")
                fopen.write(content)
