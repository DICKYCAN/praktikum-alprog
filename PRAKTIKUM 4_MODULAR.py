import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import FuncFormatter

EMPLOYEE_DATA_LIST = []  
DIVISION_LIST = ['it', 'hr', 'finance', 'marketing']
POSITION_LIST = ['staff', 'senior', 'manager']
STATUS_LIST = ['single', 'married']

users = {
    'admin': 'admin123',  
    'user': 'user123'    
}

def login():
    """
    Function to handle user login
    """
    max_attempts = 3
    attempts = 0

    while attempts < max_attempts:
        username = input("Enter username: ").strip()
        password = input("Enter password: ").strip()

        if username in users and users[username] == password:
            print("Login successful!")
            return True
        else:
            attempts += 1
            print(f"Invalid username or password. {max_attempts - attempts} attempts remaining.")
    return False

def validate_input(prompt, input_type, valid_values=None, min_value=None, max_value=None):
    """
    Function to validate input with error handling
    """
    while True:
        try:
            if input_type == 'str':
                value = input(prompt).strip().lower()
                if not value:
                    raise ValueError("Input cannot be empty!")
                if valid_values and value not in valid_values:
                    raise ValueError(f"Input must be one of: {', '.join(valid_values)}")
                return value
            
            elif input_type == 'int':
                value = int(input(prompt))
                if min_value is not None and value < min_value:
                    raise ValueError(f"Input cannot be less than {min_value}")
                if max_value is not None and value > max_value:
                    raise ValueError(f"Input cannot be more than {max_value}")
                return value
            
        except ValueError as e:
            if str(e).startswith("Input"):
                print(f"Error: {str(e)}")
            else:
                print("Error: Input must be a valid number!")

def input_employee_data():
    """
    Function to input employee data with error handling
    """
    global DIVISION_LIST, POSITION_LIST, STATUS_LIST

    employee_data = {}
    
    employee_data["name"] = validate_input("Enter employee name: ", 'str')
    employee_data["position"] = validate_input(
        "Enter position (staff/senior/manager): ",
        'str',
        valid_values=POSITION_LIST
    )
    employee_data["division"] = validate_input(
        "Enter division (it/hr/finance/marketing): ",
        'str',
        valid_values=DIVISION_LIST
    )
    employee_data["years_of_service"] = validate_input(
        "Enter years of service (years): ",
        'int',
        min_value=0,
        max_value=50
    )
    employee_data["working_days"] = validate_input(
        "Enter number of working days (0-30): ",
        'int',
        min_value=0,
        max_value=30
    )
    employee_data["status"] = validate_input(
        "Enter status (single/married): ",
        'str',
        valid_values=STATUS_LIST
    )
    
    return employee_data

def calculate_base_salary(position):
    if position == 'staff':
        return 4000000
    elif position == 'senior':
        return 6000000
    else:  # manager
        return 10000000

def calculate_service_bonus(position, years_of_service, base_salary):
    if years_of_service >= 5:
        if position == 'manager':
            return base_salary * 0.2
        elif position == 'senior':
            return base_salary * 0.15
        else:
            return base_salary * 0.1
    else:
        return base_salary * 0.05

def calculate_division_allowance(division, base_salary):
    if division == 'it':
        return base_salary * 0.15
    elif division == 'finance':
        return base_salary * 0.1
    else:
        return base_salary * 0.08

def calculate_deduction(working_days, years_of_service, base_salary):
    if working_days < 20:
        if years_of_service < 2:
            return base_salary * 0.1
        else:
            return base_salary * 0.05
    return 0

def calculate_salary(data):
    """
    Main function to calculate employee salary
    """
    base_salary = calculate_base_salary(data['position'])
    service_bonus = calculate_service_bonus(data['position'], data['years_of_service'], base_salary)
    division_allowance = calculate_division_allowance(data['division'], base_salary)
    deduction = calculate_deduction(data['working_days'], data['years_of_service'], base_salary)

    total_salary = base_salary + service_bonus + division_allowance - deduction
    
    return {
        'base_salary': base_salary,
        'service_bonus': service_bonus,
        'division_allowance': division_allowance,
        'deduction': deduction,
        'total_salary': total_salary
    }

def create_dataframe():
    """
    Create DataFrame from global employee data list
    """
    global EMPLOYEE_DATA_LIST
    return pd.DataFrame(EMPLOYEE_DATA_LIST)

def visualize_data(df, division_budget):
    """
    Create visualization comparing total salary used 
    with the budget per division.
    """
    total_salary_per_division = df.groupby('division')['total_salary'].sum()

    division = list(total_salary_per_division.index) 
    total_salary_used = total_salary_per_division.values  
    budget = [division_budget[d] for d in division]  

    x = np.arange(len(division))  
    width = 0.2  

    fig, ax = plt.subplots(figsize=(10, 5))

    ax.bar(x - width / 2, budget, width=width, color='blue', label='Budget')
    ax.bar(x + width / 2, total_salary_used, width=width, color='green', label='Total Salary Used')

    def format_ticks(value, _):
        return f"{int(value):,}" 

    ax.yaxis.set_major_formatter(FuncFormatter(format_ticks))

    ax.set_xlabel('division', fontsize=12)
    ax.set_ylabel('Amount (Rp)', fontsize=12)
    ax.set_title('Comparison of Budget and Total Salary Used per division', fontsize=14)
    ax.set_xticks(x)
    ax.set_xticklabels(division, fontsize=10)
    ax.legend()

    plt.tight_layout()
    plt.show()

def data_to_excel(df):
    average_salary_position = df.groupby('position')['total_salary'].mean().reset_index()
    average_salary_position.rename(columns={"total_salary": "average_salary"}, inplace=True)
    average_salary_position = average_salary_position.sort_values(by="average_salary", ascending=False)

    average_salary_division = df.groupby('division')['total_salary'].mean().reset_index()
    average_salary_division.rename(columns={"total_salary": "average_salary"}, inplace=True)
    average_salary_division = average_salary_division.sort_values(by="average_salary", ascending=False)

    with pd.ExcelWriter('employee_salary_report.xlsx', engine='openpyxl') as writer:
        df.to_excel(writer, sheet_name="Employee Data", index=False)
        average_salary_position.to_excel(writer, sheet_name="Average Salary Position", index=False)
        average_salary_division.to_excel(writer, sheet_name="Average Salary Division", index=False)

    "Data successfully saved to 'employee_salary_report.xlsx'."

def input_data_from_excel():
    """
    Input data from Excel file
    """
    file_path = input("Enter Excel file path: ").strip()
    try:
        df_excel = pd.read_excel(file_path)
        for index, row in df_excel.iterrows():
            employee_data = {
                'name': row['name'],
                'position': row['position'],
                'division': row['division'],
                'years_of_service': row['years_of_service'],
                'working_days': row['working_days'],
                'status': row['status']
            }
            result = calculate_salary(employee_data)
            complete_data = {**employee_data, **result}
            EMPLOYEE_DATA_LIST.append(complete_data)
        print(f"Data from {file_path} successfully imported!")
    except Exception as e:
        print(f"Error: {e}")


def main():
    """
    Main program function
    """
    global EMPLOYEE_DATA_LIST 

    budget = validate_input("Enter this month's budget: ", 'int', min_value=0)
    
    DIVISION_BUDGET = {
        'it': budget * 0.3, 
        'hr': budget * 0.15,
        'finance': budget * 0.10,
        'marketing': budget * 0.45, 
    }

    print("\n=== SELECT INPUT METHOD ===")
    print("1. Manual Input")
    print("2. Input from Excel")
    
    choice = validate_input(
        "Select input method (1/2): ",
        'str',
        valid_values=['1', '2']
    )
    
    if choice == '1':
        loop = True
        while loop == True:
            employee_data = input_employee_data()
            result = calculate_salary(employee_data)
            complete_data = {**employee_data, **result}
            EMPLOYEE_DATA_LIST.append(complete_data)
            print("\nData successfully added!")
            action = validate_input("Apakah ingin menambah data lain? (y/n):",'str',valid_values=['y','n']).lower()
            if action == 'n':
                loop = False
                
    elif choice == '2':
        input_data_from_excel()
        print("\nData successfully imported from Excel. Program completed")

    df = create_dataframe()

    print("\nAverage salary per position:")
    print(df.groupby('position')['total_salary'].mean())
    
    print("\nAverage salary per division:")
    print(df.groupby('division')['total_salary'].mean())
    
    print(f"| {'No':<3} | {'Name':<15} | {'Position':<15} | {'division':<15} | {'Years of Service':<10} | {'Working Days':<10} | {'Status':<10} | {'Total Salary':<10} |")
    print("=" * 120)
    for idx, employee in enumerate(EMPLOYEE_DATA_LIST, start=1):
        print(f"| {idx:<3} | {employee['name']:<15} | {employee['position']:<15} | {employee['division']:<15} | "
            f"{employee['years_of_service']:<10} | {employee['working_days']:<10} | {employee['status']:<10} | {employee['total_salary']:<10,.0f} |")

    # Save data to Excel
    data_to_excel(df)
    print("\nData has been saved to 'employee_salary_report.xlsx'")
    
    # Visualize data
    print("\nCreating data visualization...")
    visualize_data(df, DIVISION_BUDGET)
value = login()
if value == True :
    main()
else :
    print("Maximum login attempts reached. Exiting program.") 