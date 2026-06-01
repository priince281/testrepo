import json

def fetch_marks():
        try:
            with open('student_info.json', 'r') as file:
                data = json.load(file)
            
            sub_name = input('Subject name: ')
            for key in data:
                if key['sub_name'].lower() == sub_name.lower():
                    print(f'The assigned mark is : {key['sub_mark']}')
                    break                
            else:
                print('The subject name was not found!')
        
        except json.JSONDecodeError:
            print('No info found in the file!')