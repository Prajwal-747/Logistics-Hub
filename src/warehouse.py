import mysql.connector

db = mysql.connector.connect(username="root", host="localhost", password="1234567890", database="warehouse")
cursor = db.cursor()

def list_wh():
    query = """SELECT 
    w.WarehouseID,
    w.Location,
    m.MName
    FROM Warehouses AS w
    JOIN Managers AS m
    ON w.ManagerID = m.ManagerID;"""
    cursor.execute(query)
    data = cursor.fetchall()
    print("(WarehouseID, Location, Manager Name)")
    for i in data:
        print(i)

def add_wh():
    location = input("Enter location: ")
    capacity = int(input("Enter capacity: "))
    manager_id = int(input("Enter manager ID: "))

    cursor.execute("INSERT INTO Warehouses (Location, Capacity, ManagerID) VALUES (%s, %s, %s)", (location, capacity, manager_id))
    db.commit()
    print("Warehouse added successfully!\n")

def remove_wh():
    warehouse_to_remove = int(input("Enter WarehouseID to remove: "))
    cursor.execute("SELECT WarehouseID, Location FROM Warehouses WHERE WarehouseID != %s", (warehouse_to_remove,))
    warehouses = cursor.fetchall()
    if not warehouses:
        print("No other warehouses available for transfer. Cannot remove this warehouse.")
        return

    print("Select warehouse ID to transfer parcels to:")
    for w in warehouses:
        print(f"{w[0]} - {w[1]}")
    transfer_to = int(input("Enter destination WarehouseID: "))

    cursor.execute("UPDATE Parcels SET WarehouseID = %s WHERE WarehouseID = %s", (transfer_to, warehouse_to_remove))

    cursor.execute("DELETE FROM Warehouses WHERE WarehouseID = %s", (warehouse_to_remove,))
    db.commit()
    print(f"Warehouse {warehouse_to_remove} removed and parcels transferred to {transfer_to}.\n")