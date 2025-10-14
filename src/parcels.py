import mysql.connector

db = mysql.connector.connect(username="root", host="localhost", password="1234567890", database="warehouse")
cursor = db.cursor()

def list_parcels():
    query = """
    SELECT ParcelID, BookingID, Weight, PStatus, WarehouseID
    FROM Parcels
    ORDER BY ParcelID
    """
    cursor.execute(query)
    parcels = cursor.fetchall()
    print("ParcelID | BookingID | Weight | Status | WarehouseID")
    print("----------------------------------------------------")
    for p in parcels:
        print(f"{p[0]} | {p[1]} | {p[2]} | {p[3]} | {p[4]}")

def get_parcel_by_id(parcel_id):
    query = """
    SELECT ParcelID, BookingID, Weight, Status, WarehouseID
    FROM Parcels
    WHERE ParcelID = %s
    """
    cursor.execute(query, (parcel_id,))
    parcel = cursor.fetchone()
    if parcel:
        return {
            "ParcelID": parcel[0],
            "BookingID": parcel[1],
            "Weight": parcel[2],
            "Status": parcel[3],
            "WarehouseID": parcel[4]
        }
    else:
        return None


def add_parcel():
    sender = input("Enter sender ID: ")
    receiver = input("Enter receiver: ")
    weight = float(input("Enter parcel weight (kg): "))
    warehouse_id = int(input("Enter warehouse ID: "))
    status = "Stored"

    cursor.execute("INSERT INTO Parcels (SenderID, ReceiverID, Weight, WarehouseID, Status) VALUES (%s, %s, %s, %s, %s)", (sender, receiver, weight, warehouse_id, status))
    db.commit()
    print("Parcel added successfully!")

def update_parcel_status():
    parcel_id = int(input("Enter Parcel ID: "))
    new_status = input("Enter new status (Stored/In Transit/Delivered): ")

    cursor.execute("UPDATE Parcels SET Status=%s WHERE ParcelID=%s", (new_status, parcel_id))
    db.commit()
    print("Parcel status updated!")

def remove_parcel(parcel_id):
    # Check if parcel is part of any booking
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
