import mysql.connector

db = mysql.connector.connect(username="root", host="localhost", password="1234567890", database="warehouse")
cursor = db.cursor()

def list_managers():
    try:
        query = """
            SELECT 
                m.ManagerID,
                m.MName,
                m.MNumber,
                COUNT(w.WarehouseID) AS WarehouseCount
            FROM Managers m
            LEFT JOIN Warehouses w ON m.ManagerID = w.ManagerID
            GROUP BY m.ManagerID, m.MName, m.MNumber
        """
        cursor.execute(query)
        rows = cursor.fetchall()

        print("ManagerID  Name            Contact           Warehouses Owned")
        print("------------------------------------------------------------")
        for row in rows:
            print(f"{row[0]}  {row[1]}  {row[2]}  {row[3]}")

    except mysql.connector.Error as e:
        print("MySQL Error:", e)

def add_manager(manager_id, name, contact):
    try:
        query = "INSERT INTO Managers (ManagerID, MName, MNumber) VALUES (%s, %s, %s)"
        cursor.execute(query, (manager_id, name, contact))
        db.commit()
        print(f"Manager {name} added successfully.")
    except mysql.connector.Error as e:
        print("MySQL Error:", e)

def remove_manager(manager_id):
    try:
        cursor.execute("SELECT WarehouseID FROM Warehouses WHERE ManagerID = %s", (manager_id,))
        warehouses = cursor.fetchall()
        
        if warehouses:
            print(f"Manager {manager_id} owns {len(warehouses)} warehouse(s).")
            cursor.execute("SELECT ManagerID, MName FROM Managers WHERE ManagerID != %s", (manager_id,))
            managers = cursor.fetchall()
            if not managers:
                print("No other managers available. Cannot remove this manager.")
                return
            
            print("Select a manager ID to transfer warehouses to:")
            for m in managers:
                print(f"{m[0]} - {m[1]}")

            transfer_to = int(input("Enter new manager ID: "))
            cursor.execute("UPDATE Warehouses SET ManagerID = %s WHERE ManagerID = %s", (transfer_to, manager_id))

        cursor.execute("DELETE FROM Managers WHERE ManagerID = %s", (manager_id,))
        db.commit()
        if cursor.rowcount > 0:
            print(f"Manager with ID {manager_id} removed.")
        else:
            print("No manager found with the given ID.")
    except mysql.connector.Error as e:
        print("MySQL Error:", e)

add_manager()   
remove_manager()
list_managers()