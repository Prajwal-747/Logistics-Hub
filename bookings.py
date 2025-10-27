import mysql.connector
from datetime import date

db = mysql.connector.connect(username="root", host="localhost", password="1234567890", database="warehouse")
cursor = db.cursor()

def get_booking_by_id(booking_id):
    query = """
    SELECT b.BookingID, b.ParcelID, b.VehicleID, b.Date, b.Amount,
           p.Status as ParcelStatus,
           v.Type as VehicleType, v.VStatus as VehicleStatus
    FROM Bookings b
    JOIN Parcels p ON b.ParcelID = p.ParcelID
    JOIN Vehicles v ON b.VehicleID = v.VehicleID
    WHERE b.BookingID = %s
    """
    cursor.execute(query, (booking_id,))
    booking = cursor.fetchone()
    if booking:
        return {
            "BookingID": booking[0],
            "ParcelID": booking[1],
            "VehicleID": booking[2],
            "Date": booking[3],
            "Amount": booking[4],
            "ParcelStatus": booking[5],
            "VehicleType": booking[6],
            "VehicleStatus": booking[7]
        }
    else:
        return None

def create_booking():
    parcel_id = int(input("Enter Parcel ID: "))
    # Check parcel exists
    cursor.execute("SELECT ParcelID FROM Parcels WHERE ParcelID = %s", (parcel_id,))
    if not cursor.fetchone():
        print("Parcel ID does not exist. Cannot assign vehicle.\n")
        return

    vehicle_id = int(input("Enter Vehicle ID: "))
    amount = float(input("Enter booking amount: "))

    cursor.execute("INSERT INTO Bookings (ParcelID, VehicleID, Date, Amount) VALUES (%s, %s, %s, %s)",
                   (parcel_id, vehicle_id, date.today(), amount))
    db.commit()

    cursor.execute("UPDATE Parcels SET Status='In Transit' WHERE ParcelID=%s", (parcel_id,))
    db.commit()
    print("Vehicle assigned and parcel status updated to 'In Transit'\n")

def cancel_booking():
    booking_id = int(input("Enter Booking ID to cancel: "))
    cursor.execute("SELECT ParcelID FROM Bookings WHERE BookingID = %s", (booking_id,))
    result = cursor.fetchone()
    if not result:
        print("Booking ID not found.\n")
        return

    parcel_id = result[0]
    cursor.execute("DELETE FROM Bookings WHERE BookingID = %s", (booking_id,))
    db.commit()

    cursor.execute("UPDATE Parcels SET Status='Pending' WHERE ParcelID = %s", (parcel_id,))
    db.commit()
    print(f"Booking {booking_id} cancelled and parcel status reverted to 'Pending'.\n")

# Example usage:
# assign_vehicle()
# cancel_booking()

cursor.close()
db.close()
