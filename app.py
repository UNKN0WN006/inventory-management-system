import sqlite3
from datetime import datetime

# Connecting to the SQLite database
conn = sqlite3.connect('inventory.db')
cursor = conn.cursor()

# Function to add, update, remove, purchase, view all  new product. Also to view purchase history
def add_product(name, price, quantity):
    cursor.execute('INSERT INTO products (name, price, quantity) VALUES (?, ?, ?)', (name, price, quantity))
    conn.commit()
    print("Product added successfully.")


def update_product(product_id, price=None, quantity=None):
    if price is not None:
        cursor.execute('UPDATE products SET price = ? WHERE id = ?', (price, product_id))
    if quantity is not None:
        cursor.execute('UPDATE products SET quantity = ? WHERE id = ?', (quantity, product_id))
    conn.commit()
    print("Product updated successfully.")

def remove_product(product_id):
    cursor.execute('DELETE FROM products WHERE id = ?', (product_id,))
    conn.commit()
    print("Product removed successfully.")

def purchase_product(product_id, quantity, customer_name):
    cursor.execute('SELECT quantity FROM products WHERE id = ?', (product_id,))
    result = cursor.fetchone()
    if result and result[0] >= quantity:
        cursor.execute('UPDATE products SET quantity = quantity - ? WHERE id = ?', (quantity, product_id))
        cursor.execute('INSERT INTO purchases (product_id, quantity, customer_name, purchase_date) VALUES (?, ?, ?, ?)',
                       (product_id, quantity, customer_name, datetime.now()))
        conn.commit()
        print("Purchase successful.")
    else:
        print("Purchase failed: Not enough stock or product does not exist.")

def view_products():
    cursor.execute('SELECT * FROM products')
    products = cursor.fetchall()
    if products:
        print("\nAvailable Products:")
        for product in products:
            print("ID: {}, Name: {}, Price: {}, Quantity: {}".format(product[0], product[1], product[2], product[3]))
    else:
        print("No products available.")

def view_purchase_history():
    cursor.execute('SELECT * FROM purchases')
    purchases = cursor.fetchall()
    if purchases:
        print("\nPurchase History:")
        for purchase in purchases:
            print("ID: {}, Product ID: {}, Quantity: {}, Customer: {}, Date: {}".format(
                purchase[0], purchase[1], purchase[2], purchase[3], purchase[4]))
    else:
                print("No purchases have been made yet.")

# Main function to run the application
def main():
    while True:
        print("\n--- Inventory Management System ---")
        print("1. Add Product")
        print("2. Update Product")
        print("3. Remove Product")
        print("4. Purchase Product")
        print("5. View Products")
        print("6. View Purchase History")
        print("7. Exit")
        choice = raw_input("Enter your choice: ")

        if choice == '1':
            name = raw_input("Enter product name: ")
            price = float(raw_input("Enter product price: "))
            quantity = int(raw_input("Enter product quantity: "))
            add_product(name, price, quantity)
        elif choice == '2':
            product_id = int(raw_input("Enter product ID to update: "))
            price_input = raw_input("Enter new price (or leave blank): ")
            quantity_input = raw_input("Enter new quantity (or leave blank): ")
            price = float(price_input) if price_input else None
            quantity = int(quantity_input) if quantity_input else None
            update_product(product_id, price, quantity)
        elif choice == '3':
            product_id = int(raw_input("Enter product ID to remove: "))
            remove_product(product_id)
        elif choice == '4':
            product_id = int(raw_input("Enter product ID to purchase: "))
            quantity = int(raw_input("Enter quantity to purchase: "))
            customer_name = raw_input("Enter customer name: ")
            purchase_product(product_id, quantity, customer_name)
        elif choice == '5':
            view_products()
        elif choice == '6':
            view_purchase_history()
        elif choice == '7':
            print("Exiting the system.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()

# Closing the database connection when done
conn.close()
