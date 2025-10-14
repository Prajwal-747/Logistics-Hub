import mysql.connector
from datetime import date

db = mysql.connector.connect(username="root", host="localhost", password="1234567890", database="warehouse")
cursor = db.cursor()

def assign_vehicle():
    parcel_id = int(input("Enter Parcel ID: "))
    vehicle_id = int(input("Enter Vehicle ID: "))
    amount = float(input("Enter booking amount: "))

    cursor.execute("INSERT INTO Bookings (ParcelID, VehicleID, Date, Amount) VALUES (%s, %s, %s, %s)",
                (parcel_id, vehicle_id, date.today(), amount))
    db.commit()

    cursor.execute("UPDATE Parcels SET Status='In Transit' WHERE ParcelID=%s", (parcel_id,))
    db.commit()
    print("Vehicle assigned and parcel status updated to 'In Transit'\n")

def add_vehicle():
    vehicle_id = int(input("Enter new Vehicle ID: "))
    vehicle_type = input("Enter Vehicle Type: ")
    status = input("Enter Vehicle Status: ")

    cursor.execute("INSERT INTO Vehicles (VehicleID, Type, Status) VALUES (%s, %s, %s)",
                (vehicle_id, vehicle_type, status))
    db.commit()
    print("Vehicle added successfully.\n")

def remove_vehicle():
    vehicle_id = int(input("Enter Vehicle ID to remove: "))
    cursor.execute("SELECT BookingID FROM Bookings WHERE VehicleID = %s", (vehicle_id,))
    bookings = cursor.fetchall()
    if bookings:
        print("This vehicle is assigned to one or more bookings and cannot be removed.")
        return

    cursor.execute("DELETE FROM Vehicles WHERE VehicleID = %s", (vehicle_id,))
    db.commit()
    if cursor.rowcount > 0:
        print("Vehicle removed successfully.\n")
    else:
        print("No vehicle found with the given ID.\n")

def change_vehicle_status():
    vehicle_id = int(input("Enter Vehicle ID: "))
    new_status = input("Enter new Status: ")

    cursor.execute("UPDATE Vehicles SET Status = %s WHERE VehicleID = %s", (new_status, vehicle_id))
    db.commit()
    if cursor.rowcount > 0:
        print(f"Vehicle {vehicle_id} status updated to {new_status}.\n")
    else:
        print("No vehicle found with the given ID.\n")