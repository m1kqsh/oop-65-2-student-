import sqlite3

conn = sqlite3.connect("store.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS products (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    price REAL,
    quantity INTEGER
);
""")

conn.commit()

def create_product(name, price, quantity):
    cursor.execute(
        "INSERT INTO products (name, price, quantity) VALUES (?, ?, ?)",
        (name, price, quantity)
    )
    conn.commit()

def read_products():
    cursor.execute("SELECT * FROM products")
    for row in cursor.fetchall():
        print(row)

def update_product(id, price):
    cursor.execute(
        "UPDATE products SET price = ? WHERE id = ?",
        (price, id)
    )
    conn.commit()


def delete_product(id):
    cursor.execute(
        "DELETE FROM products WHERE id = ?",
        (id,)
    )
    conn.commit()


create_product("Phone", 500, 10)
create_product("Laptop", 1200, 5)

read_products()

update_product(1, 550)

delete_product(2)

print("\nПосле изменений:")
read_products()

conn.close()