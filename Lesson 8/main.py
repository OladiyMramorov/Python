import view
import data_base

while True:
    operation = view.action()
    if operation == 1:
        data_base.add_person()
    if operation == 2:
        data_base.find_person()
    if operation == 3:
        data_base.change_person()
    if operation == 4:
        data_base.delete_data()
    if operation == 5:
        break