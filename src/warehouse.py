import mysql.connector

db = mysql.connector.connect(username="root", host="localhost", password="1234567890", database="warehouse")
cursor = db.cursor()

def list_warehouses():
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

list_warehouses()