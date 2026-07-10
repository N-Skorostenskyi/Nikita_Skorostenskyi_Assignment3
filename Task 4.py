employees = [
{"name": "Олена", "department": "Marketing", "salary":
25000},
{"name": "Ігор", "department": "IT", "salary": 55000},
{"name": "Наталія", "department": "Marketing", "salary":
28000},
{"name": "Олег", "department": "HR", "salary": 22000},
{"name": "Андрій", "department": "IT", "salary": 55000},
{"name": "Марія", "department": "IT", "salary": 52000},
]

def get_department_stats(employee_list, target_dept):
    emp_dept=[emp for emp in employee_list if emp["department"] == target_dept]

    avg_salary=round(sum(emp["salary"] for emp in emp_dept)/len(emp_dept),2)

    max_salary=max(emp["salary"] for emp in emp_dept)

    top_employees= [emp["name"] for emp in emp_dept if emp["salary"]==max_salary]

    count=len(emp_dept)
    return {
        "department": target_dept,
        "average_salary": avg_salary,
        "top_earner": top_employees,
        "count": count
    }
print(get_department_stats(employees,"IT"))



