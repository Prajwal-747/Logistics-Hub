import mysql.connector

db = mysql.connector.connect(username="root", host="localhost", password="1234567890", database="warehouse")
cursor = db.cursor()

def add_parcel():
    sender = input("Enter sender ID: ")
    receiver = input("Enter receiver: ")
    weight = float(input("Enter parcel weight (kg): "))
    warehouse_id = int(input("Enter warehouse ID: "))
    status = input("Enter status (Stored/In Transit/Delivered): ")

    cursor.execute("INSERT INTO Parcels (SenderID, ReceiverID, Weight, WarehouseID, Status) VALUES (%s, %s, %s, %s, %s)", (sender, receiver, weight, warehouse_id, status))
    db.commit()
    print("Parcel added successfully!")

def update_parcel_status():
    parcel_id = int(input("Enter Parcel ID: "))
    new_status = input("Enter new status (Stored/In Transit/Delivered): ")

    cursor.execute("UPDATE Parcels SET Status=%s WHERE ParcelID=%s", (new_status, parcel_id))
    db.commit()
    print("Parcel status updated!")