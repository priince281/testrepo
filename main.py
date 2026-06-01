idno = input('Please Enter your ID number: ')

while True:
    if idno[0] == '1':
        import facultyaccess
        print('----Choose your option----\n' \
        '1. Add subject\n' \
        '2. Change mark for existing subject')

        choice = int(input('Your choice: '))
        if choice == 1:
            facultyaccess.add_subject()
        
        elif choice == 2:
            facultyaccess.modify_marks()

        else:
            print('Invalid choice, try again!')

    elif idno[0] == '2':
        import studentaccess
        studentaccess.fetch_marks()

    else:
        print('ID number is invaild, try again!')