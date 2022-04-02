import datetime
import file_operation as file
import check_file

def make_massages(persons):
    now = datetime.datetime.now()
    for key, value in persons.items():
        (name,surname,work_to_do,grade)=tuple(value)
        text = f'{now.date()}, Gdynia\n\n\
        Welcome {name} {surname},\n\n\
This is a kindly reminder that you have {work_to_do}\n\
tasks left to submit before you can graduate.\n\n\
Your current grade is {grade} and can increase to {grade+1}\n\
if you submit all assignments in 1 month.\n\n\
        Socrates\n\
        Your teacher'
        save_to_file(key, text)


def save_to_file(file_name, content):
    check_file.do_this_with_file(f'{file_name}.txt','write',content)


def main():

    students = file.import_data('students.csv')
    make_massages(students)


if __name__ == '__main__':
    main()
