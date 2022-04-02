def check_values(values):
    (nr_class,name,surname,work_to_do,grade)=tuple(values)
    name=correct_size_letter(name)
    surname=correct_size_letter(surname)
    if not check_class(nr_class):
        print (f"Incorrect class notation for a studen {name} {surname}")
    work_to_do = make_value(work_to_do,name, surname,'work to do')
    grade = make_value(grade, name, surname, 'grade')
    return [nr_class,name,surname,work_to_do,grade]

def correct_size_letter(input):
    # check size first letter
    return(input.lower()).capitalize()

def check_class(input):
    try:
        return input[1].isalpha() and input[0].isnumeric()
    except Exception:
        print ("Empty or incomplete field class")
        exit(1)

def make_value (input, name, surname, task):
    try:
        return(int(input))
    except Exception:
        print (f'Incorrect value {task} for student {name} {surname}')
        exit(1)


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
                dict_student[key_name]=values[1:]
            return dict_student
    except (FileNotFoundError) as err:
        print("This file does not exist. Try re-entering the file name")



if __name__=='__main__':
    filename='students.csv'
    print(import_data(filename))
