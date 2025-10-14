import parcels
import vehicles
import warehouse
import managers
import reports

while True:
    print("""
========= Warehouse & Truck Management System =========
1. Add Warehouse
2. Add Parcel
3. Update Parcel Status
4. Assign Vehicle for Delivery
5. View Reports
6. Exit
=======================================================
""")
    choice = input("Enter your choice: ")

    if choice == '1':
        warehouse.add_warehouse()
    elif choice == '2':
        parcels.add_parcel()
    elif choice == '3':
        parcels.update_parcel_status()
    elif choice == '4':
        vehicles.assign_vehicle()
    elif choice == '5':
        reports.view_report()
    elif choice == '6':
        break
    else:
        print("Invalid choice!")