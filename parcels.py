import mysql.connector
from tabulate import tabulate

db = mysql.connector.connect(username="root", host="localhost", password="1234567890", database="warehouse")
cursor = db.cursor()

def list_parcels():
    try:
        query = """
        SELECT ParcelID, BookingID, Weight, PStatus, WarehouseID
        FROM Parcels
        ORDER BY ParcelID
        """
        cursor.execute(query)
        parcels = cursor.fetchall()
        print("\nParcels List:\n")
        if parcels:
            headers = ["ParcelID", "BookingID", "Weight", "Status", "WarehouseID"]
            print(tabulate(parcels, headers=headers, tablefmt="pretty"))
        else:
            print("No parcels found.")
        print()
    except mysql.connector.Error as e:
        print(f"MySQL Error: {e}")

def get_parcel_by_id(parcel_id):
    try:
        query = """
        SELECT ParcelID, BookingID, Weight, Status, WarehouseID
        FROM Parcels
        WHERE ParcelID = %s
        """
        cursor.execute(query, (parcel_id,))
        parcel = cursor.fetchone()
        print(
            "ParcelID: ", parcel[0],
            "\nBookingID: ", parcel[1],
            "\nWeight: ", parcel[2],
            "\nStatus :", parcel[3],
            "\nWarehouseID: ", parcel[4]
        )
    except mysql.connector.Error as e:
        print(f"MySQL Error: {e}")

def add_parcel():
    try:
        sender = input("Enter sender ID: ")
        receiver = input("Enter receiver: ")
        weight = float(input("Enter parcel weight (kg): "))
        warehouse_id = int(input("Enter warehouse ID: "))
        status = "Stored"

        cursor.execute("INSERT INTO Parcels (SenderID, ReceiverID, Weight, WarehouseID, Status) VALUES (%s, %s, %s, %s, %s)", (sender, receiver, weight, warehouse_id, status))
        db.commit()
        print("Parcel added successfully!")
    except mysql.connector.Error as e:
        print(f"MySQL Error: {e}")

def update_parcel_status():
    try:
        parcel_id = int(input("Enter Parcel ID: "))
        new_status = input("Enter new status (Stored/In Transit/Delivered): ")

        cursor.execute("UPDATE Parcels SET Status=%s WHERE ParcelID=%s", (new_status, parcel_id))
        db.commit()
        print("Parcel status updated!")
    except mysql.connector.Error as e:
        print(f"MySQL Error: {e}")

def remove_parcel(parcel_id):
    try:
        cursor.execute("SELECT BookingID FROM Bookings WHERE ParcelID = %s", (parcel_id,))
        booking = cursor.fetchone()
        if booking:
            print("Parcel is part of a booking and cannot be removed.")
            return False

        # Delete parcel
        cursor.execute("DELETE FROM Parcels WHERE ParcelID = %s", (parcel_id,))
        db.commit()
        if cursor.rowcount > 0:
            print(f"Parcel {parcel_id} removed successfully.")
            return True
        else:
            print("Parcel not found.")
            return False
    except mysql.connector.Error as e:
        print(f"MySQL Error: {e}")
