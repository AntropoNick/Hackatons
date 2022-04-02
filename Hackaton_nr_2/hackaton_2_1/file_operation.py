def import_data():
    dict_student={}
    with open('students.csv', 'r') as fopen:
        content = (fopen.readlines())
        # Remove first description line
        content.pop(0)
        # Read line in file
        for line in content:
            # Remove endline sign
            line = line.strip('\n')
            # Split file value
            values=line.split(';',',')
            # Make dictionary from file value
            key_name=(f"{values[0]}_{values[1]}_{values[2]}")
            dict_student[key_name]=values
        return dict_student

if __name__=='__main__':
    print(import_data())