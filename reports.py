import mysql.connector
from tabulate import tabulate

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
    print("\nParcel Status Summary:\n")
    if results:
        print(tabulate(results, headers=["Status", "Count"], tablefmt="pretty"))
    else:
        print("No parcel data available.")
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
    print("\nWarehouse Usage Report:\n")
    if results:
        print(tabulate(results, headers=["WarehouseID", "Location", "Capacity", "Used"], tablefmt="pretty"))
    else:
        print("No warehouse data available.")
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
    print("\nVehicle Utilization Report:\n")
    if results:
        print(tabulate(results, headers=["VehicleID", "Type", "Status", "Current Bookings"], tablefmt="pretty"))
    else:
        print("No vehicle data available.")
    print()

def report_active_bookings():
    """List all active bookings with parcel and vehicle details"""
    query = """
SELECT b.BookingID, b.ParcelID, b.VehicleID, b.Date, b.Amount, p.PStatus as ParcelStatus, v.Type as VehicleType, v.VStatus as VehicleStatus
FROM Bookings b
JOIN Parcels p ON b.ParcelID = p.ParcelID
JOIN Vehicles v ON b.VehicleID = v.VehicleID
ORDER BY b.Date DESC
"""
    cursor.execute(query)
    results = cursor.fetchall()
    print("Active Bookings:")

    headers = [
        "BookingID", 
        "ParcelID", 
        "VehicleID", 
        "Date", 
        "Amount", 
        "ParcelStatus", 
        "VehicleType", 
        "VehicleStatus"
    ]

    print("\nActive Bookings:\n")
    print(tabulate(results, headers=headers, tablefmt="pretty"))
    print()

