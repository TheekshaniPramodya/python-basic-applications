class Product:
    def __init__(self, product_id, name, quantity, price):
        self.product_id = product_id
        self.name = name
        self.quantity = quantity
        self.price = price

    def update_quantity(self, new_quantity):
        self.quantity = new_quantity

    def get_total_value(self):
        return self.quantity * self.price

    def display_product_details(self):
        print(f"ID: {self.product_id}, Name: {self.name}, Quantity: {self.quantity}, Price: {self.price:.2f}")


class InventorySystem:
    def __init__(self):
        self.products = {}

    def add_product(self, product):
        if product.product_id in self.products:
            print("Product with this ID already exists.")
        else:
            self.products[product.product_id] = product
            print("Product added successfully.")

    def update_product_quantity(self, product_id, new_quantity):
        product = self.products.get(product_id)
        if product:
            product.update_quantity(new_quantity)
            print("Product quantity updated successfully.")
        else:
            print("Product not found.")

    def remove_product(self, product_id):
        if product_id in self.products:
            del self.products[product_id]
            print("Product removed successfully.")
        else:
            print("Product not found.")

    def view_inventory(self):
        if not self.products:
            print("No products in inventory.")
        else:
            print("Inventory:")
            for product in self.products.values():
                product.display_product_details()

    def generate_sales_report(self, filename):
        try:
            with open(filename, 'w') as file:
                file.write("Product Name, Quantity Sold, Total Value\n")
                for product in self.products.values():
                    total_value = product.get_total_value()
                    file.write(f"{product.name}, {product.quantity}, {total_value:.2f}\n")
            print("Sales report generated successfully.")
        except Exception as e:
            print(f"Error generating sales report: {e}")

    def load_inventory_from_file(self, filename):
        try:
            with open(filename, 'r') as file:
                self.products.clear()
                for line in file:
                    product_id, name, quantity, price = line.strip().split(',')
                    self.products[int(product_id)] = Product(int(product_id), name, int(quantity), float(price))
            print("Inventory loaded successfully.")
        except Exception as e:
            print(f"Error loading inventory: {e}")


def menu():
    inventory = InventorySystem()

    while True:
        print("\nGrocery Inventory System")
        print("1. Add Product")
        print("2. Update Product Quantity")
        print("3. Remove Product")
        print("4. View Inventory")
        print("5. Generate Sales Report")
        print("6. Load Inventory from File")
        print("7. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            product_id = int(input("Enter product ID: "))
            name = input("Enter product name: ")
            quantity = int(input("Enter quantity: "))
            price = float(input("Enter price per unit: "))
            product = Product(product_id, name, quantity, price)
            inventory.add_product(product)

        elif choice == '2':
            product_id = int(input("Enter product ID: "))
            new_quantity = int(input("Enter new quantity: "))
            inventory.update_product_quantity(product_id, new_quantity)

        elif choice == '3':
            product_id = int(input("Enter product ID to remove: "))
            inventory.remove_product(product_id)

        elif choice == '4':
            inventory.view_inventory()

        elif choice == '5':
            filename = input("Enter filename for sales report: ")
            inventory.generate_sales_report(filename)

        elif choice == '6':
            filename = input("Enter filename to load inventory: ")
            inventory.load_inventory_from_file(filename)

        elif choice == '7':
            print("Exiting Grocery Inventory System.")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    menu()
