import json

data = []

def modify_marks():
        try:
            with open('student_info.json', 'r') as file:
                data = json.load(file)

            sub_name = input('Subject name: ')
            for key in data:
                if key['sub_name'].lower() == sub_name.lower():
                    sub_mark = input('Enter the new mark: ')
                    key['sub_mark'] = sub_mark
                    break
                    
            else:
                print('Subject not found, try again!')
            
            with open('student_info.json', 'w') as file:
                json.dump(data, file, indent=4)
        
        except json.JSONDecodeError:
            print("No info found in the file, or the file doesn't exist!")

def add_subject():
    try:
        with open('student_info.json', 'r') as file:
            data = json.load(file)

        sub_name = input('Enter the subject name: ')
        sub_mark = input('Enter the subject mark: ')

        data.append(
            {
                'sub_name' : sub_name,
                'sub_mark' : sub_mark
            }
        )

        with open('student_info.json', 'w') as file:
            json.dump(data, file, indent=4)
    
    except (json.JSONDecodeError, FileNotFoundError):
        print('The file was not found or empty. After this it should be created, try again!')
        with open('student_info.json', 'w') as file:
            json.dump([], file)