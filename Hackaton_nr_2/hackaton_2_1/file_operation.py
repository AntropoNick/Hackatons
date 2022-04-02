def check_values(values):
    check_size(values)
    return values

def check_size(values):
    # check size first letter
    values[1]=values[1].capitalize()
    values[2]=values[2].capitalize()
    return values

#def check_class(value)


def import_data(filename):
    dict_student={}
    try:
        with open(filename, 'r') as fopen:
            content = (fopen.readlines())
            # Remove first description line
            content.pop(0)
            # Read line in file
            for line in content:
                # Remove endline sign
                line = line.strip('\n')
                # Split file value
                values=line.split(';')
                values=check_values(values)
                # Make dictionary from file value
                key_name=(f"{values[0]}_{values[1]}_{values[2]}")
                values[3]=int(values[3])
                values[4]=int(values[4])
                dict_student[key_name]=values
            return dict_student
    except (FileNotFoundError) as err:
        print("Taki plik nie istnieje. Spróbuj wprowadzić ponownie nazwe pliku")



if __name__=='__main__':
    filename='students.csv'
    print(import_data(filename))
