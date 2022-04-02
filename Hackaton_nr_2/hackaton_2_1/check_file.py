import os

def do_this_with_file (filename,operation,content):
    if operation=='read':
        if os.path.isfile(filename):
            with open(filename, 'r') as fopen:
                if os.path.getsize(filename)==0:
                    print ('Plik jest pusty')
                else:
                    print("Wczytano plik")
                    return fopen.read()
        else:
            print ("Plik nie istnieje")
    elif operation =='write':
        if os.path.isfile(filename):
            with open(filename, 'w') as fopen:
                answer=str(input("Plik itnieje. Czy go nadpisac? T/N: "))
                if answer=='T':
                    #with open(filename, 'w') as fopen:
                    fopen.write(content)
                elif answer=='N':
                    print('Pliku nie zapisano')
        else:
            with open(filename, 'w') as fopen:
                print ("Zapisano do pliku")
                fopen.write(content)
