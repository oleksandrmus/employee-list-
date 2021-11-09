employee_shift =["MIke","Andrew","Emma","Kelly","john ", "Brad "]
def replace_employee(employee_shift,old_employee,new_employee):
    index_old_employee = employee_shift.index(old_employee)
    employee_shift.remove(old_employee)
    employee_shift.insert(index_old_employee,new_employee)
    print(employee_shift)
replace_employee(employee_shift,old_employee="Kelly", new_employee="Matilda")





