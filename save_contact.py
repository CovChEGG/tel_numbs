import user_interface_functions as ui_f

def write_to_file():
    id = ui_f.id()
    name = ui_f.username()
    surname = ui_f.surname()
    phone_number = ui_f.phone()
    comment = ui_f.comments()
    with open('PhoneBook.csv', 'a') as data:
        data.write(f'\n')
        data.write(f'{id};{name};{surname};{phone_number};{comment}')
