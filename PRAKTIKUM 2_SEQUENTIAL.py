# dummy variable # 
employee_data_list = []

# Division and Position Declaration #
list_division = ['it', 'hr', 'finance', 'marketing']
list_position = ['staff', 'senior', 'manager']

# List of Data #
list_data = {
    'name': ['andi', 'budi', 'citra', 'dewi', 'eka', 'fajar', 'gita', 'hendra', 'indah', 'joko'],
    'position': ['staff', 'senior', 'manager', 'staff', 'senior', 'manager', 'staff', 'senior', 'manager', 'staff'],
    'division': ['it', 'finance', 'marketing', 'hr', 'it', 'finance', 'marketing', 'hr', 'it', 'finance'],
    'years_of_service': [2, 7, 10, 1, 4, 6, 3, 5, 8, 2],
    'working_days': [21, 24, 17, 19, 20, 25, 26, 28, 25, 23],
}

# Login Process #
data_account = {'admin': 'admin123', 'user': 'user123'}
max_attempts = 3 
attempts = 0 
is_logged_in = True 

while attempts < max_attempts and is_logged_in == True: 
    username = input("Enter username: ").strip() 
    password = input("Enter password: ").strip() 
    
    if username not in data_account or data_account[username] != password: 
        attempts += 1 
        remaining_attempts = max_attempts - attempts 
        print(f"Invalid username or password. {remaining_attempts} attempts remaining.")

    else :
        print('Login successful')
        is_logged_in = False
    
    if attempts == max_attempts :
        print('Maximum login attempts reached. Exiting program')
        exit()
        
# Input Method
test = True
while test:
    input_choice = input("Choose input method (manual/list_data): ").strip().lower()
    if input_choice in ['manual', 'list_data']:
        test = False
    else:
        print("Invalid choice! Enter 'manual' or 'list_data'.")

if input_choice == 'manual':
    test = 1
    while test == 1:
        try:
            num_employees = int(input("Enter the number of employee data to input: "))
            if num_employees > 0:
                test = 0
            else:
                print("Error: Input must be greater than 0.")
        except ValueError:
            print("Invalid input. Enter a valid number.")
    
    for i in range(num_employees):
        print(f'employee-{i+1}' )
        test = 1
        while test == 1:
            name = input("Enter employee name: ").strip().lower()
            if name:
                test = 0
            else:
                print("Error: Input cannot be empty!")

        # Input position
        test = 1
        while test == 1:
            position = input("Enter position (staff/senior/manager): ").strip().lower()
            if position in list_position:
                test = 0
            else:
                print("Error: Input must be one of: staff, senior, manager")

        # Input division
        test = 1
        while test == 1:
            division = input("Enter division (it/hr/finance/marketing): ").strip().lower()
            if division in list_division:
                test = 0
            else:
                print("Error: Input must be one of: it, hr, finance, marketing")

        # Input years of service
        test = 1
        while test == 1:
            try:
                years_of_service = int(input("Enter years of service (years): "))
                if 0 <= years_of_service <= 50:
                    test = 0
                else:
                    print("Error: Input cannot be less than 0 or more than 50")
            except ValueError:
                print("Error: Input must be a valid number!")

        # Input working days
        test = 1
        while test == 1:
            try:
                working_days = int(input("Enter number of working days (0-30): "))
                if 0 <= working_days <= 30:
                    test = 0
                else:
                    print("Error: Input cannot be less than 0 or more than 30")
            except ValueError:
                print("Error: Input must be a valid number!")
        
        employee_data_list.append({
            'name': name,
            'position': position,
            'division': division,
            'years_of_service': years_of_service,
            'working_days': working_days
        })
else :
    # list_data method #
    for i in range(len(list_data['name'])):
        employee_data_list.append({
            'name': list_data['name'][i],
            'position': list_data['position'][i],
            'division': list_data['division'][i],
            'years_of_service': list_data['years_of_service'][i],
            'working_days': list_data['working_days'][i]
        })

for employee in employee_data_list:
    
    # base salary #
    if employee['position'] == 'staff':
        base_salary = 4000000
    elif employee['position'] == 'senior':
        base_salary = 6000000
    else:  # manager
        base_salary = 10000000
    
    # service bonus #
    if employee['years_of_service'] >= 5:
        if employee['position'] == 'manager':
            service_bonus = base_salary * 0.2
        elif employee['position'] == 'senior':
            service_bonus = base_salary * 0.15
        else:
            service_bonus = base_salary * 0.1
    else:
        service_bonus = base_salary * 0.05
    
    # division allowance #
    if employee['division'] == 'it':
        division_allowance = base_salary * 0.15
    elif employee['division'] == 'finance':
        division_allowance = base_salary * 0.1
    else:
        division_allowance = base_salary * 0.08
    
    # deduction #    
    deduction = base_salary * (0.1 if employee['working_days'] < 20 and employee['years_of_service'] < 2 else 0.05 if employee['working_days'] < 20 else 0)
    
    # calculating all the component #
    employee['total_salary'] = base_salary + service_bonus + division_allowance - deduction

# Input Company Budget #
test = 1
while test == 1:
    try:
        budget = int(input("Enter this month's budget: "))
        if budget > 0:
            test = 0
        else:
            print("Error: Input must be greater than 0.")
    except ValueError:
        print("Invalid input. Enter a valid number.")

division_budget = {
        'it': budget * 0.3, 
        'hr': budget * 0.15,
        'finance': budget * 0.10,
        'marketing': budget * 0.45, 
    }
# Display all the employee data #

print("="*35, "EMPLOYEE DATA", "="*35)
print("=" * 85)
print(f"| {'No':<3} | {'Name':<15} | {'Position':<10} | {'Division':<10} | {'Years':<5} | {'Days':<5} | {'Total Salary':<15} |")
print("=" * 85)
for idx, employee in enumerate(employee_data_list, start=1):
    print(f"| {idx:<3} | {employee['name']:<15} | {employee['position']:<10} | {employee['division']:<10} | {employee['years_of_service']:<5} | {employee['working_days']:<5} | {employee['total_salary']:<15,.2f} |")
print("=" * 85)