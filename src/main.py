import parcels
import vehicles
import warehouse
import managers
import reports
import bookings

while True:
    print("""
========= Warehouse & Truck Management System =========
1. Warehouse
2. Vehicles
3. Parcels
4. Bookings
5. Admin
6. Exit
=======================================================
""")

    choice = input("Enter your choice: ")

    if choice == '1':  # Warehouse menu
        while True:
            print("""
    ========= Warehouse =========
    1. List Warehouses
    2. Add Warehouse
    3. Remove Warehouse
    4. Go back
    =====================================================
    """)
            c = input("Enter your choice: ")
            if c == '1':
                warehouse.list_wh()
            elif c == '2':
                warehouse.add_wh()
            elif c == '3':
                warehouse.remove_wh()
            elif c == '4':
                break
            else:
                print("Invalid choice!")

    elif choice == '2':  # Vehicles menu
        while True:
            print("""
    ========= Vehicles =========
    1. List Vehicles
    2. Add Vehicle
    3. Remove Vehicle
    4. Change Vehicle Status
    5. Get Vehicle by ID
    6. Go back
    ============================
    """)
            c = input("Enter your choice: ")
            if c == '1':
                vehicles.list_vehicles()
            elif c == '2':
                vehicles.add_vehicle()
            elif c == '3':
                vehicles.remove_vehicle()
            elif c == '4':
                vehicles.change_vehicle_status()
            elif c == '5':
                vehicles.get_vehicle_by_id()
            elif c == '6':
                break
            else:
                print("Invalid choice!")

    elif choice == '3':  # Parcels menu
        while True:
            print("""
    ========= Parcels =========
    1. List Parcels
    2. Add Parcel
    3. Remove Parcel
    4. Update Parcel Status
    5. Get Parcel By ID
    6. Go back
    ===========================
    """)
            c = input("Enter your choice: ")
            if c == '1':
                parcels.list_parcels()
            elif c == '2':
                parcels.add_parcel()
            elif c == '3':
                parcels.update_parcel_status()
            elif c == '4':
                parcels.remove_parcel()
            elif c == '6':
                parcels.get_parcel_by_id()
            elif c == '6':
                break
            else:
                print("Invalid choice!")

    elif choice == '4':  # Bookings menu
        while True:
            print("""
    ========= Bookings =========
    1. Create Booking
    2. Cancel Booking
    3. Get Booking by ID
    4. Go back
    =============================
    """)
            c = input("Enter your choice: ")
            if c == '1':
                bookings.create_booking()
            elif c == '2':
                bookings.cancel_booking()
            elif c == '3':
                bookings.get_booking_by_id()
            elif c == '4':
                break
            else:
                print("Invalid choice!")

    elif choice == '5':  # Admin/Reports menu
        while True:
            print("""
    ========= Admin Reports =========
    1. Parcel Status Summary
    2. Warehouse Usage
    3. Vehicle Utilization
    4. Active Bookings
    5. Managers
    6. Go back
    =================================
    """)
            c = input("Enter your choice: ")
            if c == '1':
                reports.report_parcel_status_summary()
            elif c == '2':
                reports.report_warehouse_usage()
            elif c == '3':
                reports.report_vehicle_utilization()
            elif c == '4':
                reports.report_active_bookings()
            elif c == '5':
                while True:
                    print("""
            ========= Managers =========
            1. List Managers
            2. Hire Managers
            3. Fire Managers
            4. Go back
            =================================
            """)
                    c = input("Enter your choice: ")
                    if c =='1':
                        managers.list_managers()
                    elif c == '2':
                        managers.add_manager()
                    elif c == '3':
                        managers.remove_manager()
                    elif c == '4':
                        break
                    else:
                        print("Invalid choice!")

            elif c == '6':
                break
            else:
                print("Invalid choice!")

    elif choice == '6':
        print("Exiting program.")
        break

    else:
        print("Invalid choice!")
