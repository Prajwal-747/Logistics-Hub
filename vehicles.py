import mysql.connector
from datetime import date

db = mysql.connector.connect(username="root", host="localhost", password="1234567890", database="warehouse")
cursor = db.cursor()

def list_vehicles(cursor):
    query = """
    SELECT VehicleID, Type, VStatus
    FROM Vehicles
    ORDER BY VehicleID
    """
    cursor.execute(query)
    vehicles = cursor.fetchall()
    print("VehicleID | Type | Status")
    print("------------------------")
    for v in vehicles:
        print(f"{v[0]} | {v[1]} | {v[2]}")

def get_vehicle_by_id(vehicle_id,):
    query = """
    SELECT VehicleID, Type, VStatus, VCapacity
    FROM Vehicles
    WHERE VehicleID = %s
    """
    cursor.execute(query, (vehicle_id,))
    vehicle = cursor.fetchone()
    if not vehicle:
        return

    # Count active bookings for this vehicle
    cursor.execute("SELECT COUNT(*) FROM Bookings WHERE VehicleID = %s", (vehicle_id,))
    booking_count = cursor.fetchone()[0]

    # Calculate % full = (booking_count / capacity) * 100
    percent_full = (booking_count / vehicle[3]) * 100

    print("VehicleID", vehicle[0])
    print("Type", vehicle[1])
    print("Status", vehicle[2])
    print("PercentFull", round(percent_full, 2))



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