import mysql.connector

db = mysql.connector.connect(username="root", host="localhost", password="1234567890", database="warehouse")
cursor = db.cursor()

def generate_report():
    try:
        query = """
        SELECT 
            w.WarehouseID,
            w.Location,
            w.WCapacity,
            IFNULL(COUNT(p.ParcelID), 0) AS UsedCapacity,
            m.MName
        FROM Warehouses w
        LEFT JOIN Parcels p ON w.WarehouseID = p.WarehouseID
        LEFT JOIN Managers m ON w.ManagerID = m.ManagerID
        GROUP BY w.WarehouseID, w.Location, w.WCapacity, m.MName
        """

        cursor.execute(query)
        rows = cursor.fetchall()

        print(f"{'ID':<5} {'Location':<15} {'Capacity':<10} {'Used':<10} {'%Full':<8} {'Manager':<15}")
        print("-" * 65)

        for row in rows:
            warehouse_id = row[0]
            location = row[1]
            capacity = row[2]
            used = row[3]
            manager = row[4]
            percent_full = (used / capacity * 100) if capacity else 0
            print(f"{warehouse_id:<5} {location:<15} {capacity:<10} {used:<10} {percent_full:>6.2f}%   {manager:<15}")

    except mysql.connector.Error as e:
        print("MySQL Error:", e)
    except Exception as e:
        print("Error:", e)

generate_report()
