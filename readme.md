# Inventory Management System

## Description

The Inventory Management System (IMS) is a command-line application developed in Python 2.7.5 that allows users to manage products in a store. The system enables sellers to add, update, and remove products, as well as track purchases made by customers. The application uses SQLite as the database to store product and purchase data in a structured format.

## Features

- **Product Management**: 
  - Add new products to the inventory.
  - Update existing product details (price and quantity).
  - Remove products from the inventory.

- **Purchase Management**: 
  - Customers can purchase products, which updates the inventory accordingly.
  - Track purchase history, including customer name, product ID, quantity purchased, and purchase date.

- **Data Storage**: 
  - All data is stored in an SQLite database (`inventory.db`), which is created automatically if it does not exist.

## Requirements

- Python 2.7.5 or older
- SQLite (comes pre-installed with Python)

## Installation

1. **Clone the Repository**:
   Open your terminal and run the following command to clone the repository:
   ```bash
   git clone https://github.com/yourusername/inventory_management_system.git
   cd inventory_management_system```

2. **Setup the database**:
   Run the following commands to create the database and tables:
   ```bash
   python setup_db.py
   ```
## Usage

1. **Run the Application**:
   After setting up the database, you can run the main application using:
   ```bash
   python app.py
   ```
2. **Interacting with the Application**:
   Once the application is running, you will see a menu with the following options:

	```bash
	1. Add Product
	2. Update Product
	3. Remove Product
	4. Purchase Product
	5. View Products
	6. View Purchase History
	7. Exit
	```
		
		* Add Product: Enter the product name, price, and quantity to add a new product to the inventory.
		* Update Product: Enter the product ID to update its price or quantity.
		* Remove Product: Enter the product ID to remove a product from the inventory.
		* Purchase Product: Enter the product ID, quantity, and customer name to make a purchase.
		* View Products: Display all available products in the inventory.
		* View Purchase History: Display the history of all purchases made.


3. **Exiting the Application**:
   To exit the application, select the option to exit from the menu

## Database
   The application uses an SQLite database named inventory.db. The following tables are created:

	* products: Stores product details (ID, name, price, quantity).
	* purchases: Stores purchase records (ID, product ID, quantity, customer name, purchase date).

## Contributing
	If you would like to contribute to this project, please fork the repository and submit a pull request with your changes.



### Instructions for Using the README.md

1. **Replace `yourusername`**: Make sure to replace `yourusername` in the clone URL with your actual GitHub username.

2. **Add License Information**: If you have a specific license for your project, make sure to include it in the `LICENSE` file and reference it in the README.

3. **Markdown Formatting**: The README is written in Markdown format, which is widely used for documentation on GitHub. You can preview how it looks on GitHub by pushing your changes and viewing the repository.

### Final Steps

1. **Create the README.md File**:
   In your project directory, create a file named `README.md` and copy the above content into it.

2. **Add and Commit the README**:
   After creating the README file, add it to your Git repository and commit the changes:
   ```bash
   git add README.md
   git commit -m "Add README.md for Inventory Management System"
   git push origin master```
				
			

				### Last But not the Least, Thank you for going through my repository
