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