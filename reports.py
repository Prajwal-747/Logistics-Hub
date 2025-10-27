import mysql.connector

db = mysql.connector.connect(username="root", host="localhost", password="1234567890", database="warehouse")
cursor = db.cursor()

def report_parcel_status_summary():
    """Count of parcels by status (e.g., Pending, In Transit, Delivered)"""
    query = """
    SELECT Status, COUNT(*) AS Count
    FROM Parcels
    GROUP BY Status
    """
    cursor.execute(query)
    results = cursor.fetchall()
    print("Parcel Status Summary:")
    for status, count in results:
        print(f"{status}: {count}")
    print()

def report_warehouse_usage():
    """Show used capacity as number of parcels per warehouse vs capacity"""
    query = """
    SELECT w.WarehouseID, w.Location, w.WCapacity, COUNT(p.ParcelID) AS UsedCapacity
    FROM Warehouses w
    LEFT JOIN Parcels p ON w.WarehouseID = p.WarehouseID
    GROUP BY w.WarehouseID, w.Location, w.WCapacity
    """
    cursor.execute(query)
    results = cursor.fetchall()
    print("Warehouse Usage Report:")
    print("WarehouseID | Location | Capacity | Used")
    for wid, loc, capacity, used in results:
        print(f"{wid} | {loc} | {capacity} | {used}")
    print()

def report_vehicle_utilization():
    """Show vehicles and how full they are based on bookings"""
    query = """
    SELECT v.VehicleID, v.Type, v.Status, COUNT(b.BookingID) AS BookingCount
    FROM Vehicles v
    LEFT JOIN Bookings b ON v.VehicleID = b.VehicleID
    GROUP BY v.VehicleID, v.Type, v.Status
    """
    cursor.execute(query)
    results = cursor.fetchall()
    print("Vehicle Utilization Report:")
    print("VehicleID | Type | Status | Current Bookings")
    for vid, vtype, status, bookings in results:
        print(f"{vid} | {vtype} | {status} | {bookings}")
    print()

def report_active_bookings():
    """List all active bookings with parcel and vehicle details"""
    query = """
    SELECT b.BookingID, b.ParcelID, b.VehicleID, b.Date, b.Amount,
           p.Status as ParcelStatus,
           v.Type as VehicleType, v.Status as VehicleStatus
    FROM Bookings b
    JOIN Parcels p ON b.ParcelID = p.ParcelID
    JOIN Vehicles v ON b.VehicleID = v.VehicleID
    ORDER BY b.Date DESC
    """
    cursor.execute(query)
    results = cursor.fetchall()
    print("Active Bookings:")
    header = ("BookingID", "ParcelID", "VehicleID", "Date", "Amount", "ParcelStatus", "VehicleType", "VehicleStatus")
    print(" | ".join(header))
    for row in results:
        print(" | ".join(str(col) for col in row))
    print()

