import sys
import csv
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QPushButton,
    QTableWidget, QTableWidgetItem, QFileDialog, QMessageBox, QInputDialog, QHeaderView
)
from PyQt5.QtCore import Qt


class InventoryManagementSystem(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Inventory Management System")
        self.setGeometry(100, 100, 800, 600)

        self.init_ui()

    def init_ui(self):
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        self.layout = QHBoxLayout(self.central_widget)

        self.left_panel = QWidget()
        self.right_panel = QWidget()

        self.layout.addWidget(self.left_panel)
        self.layout.addWidget(self.right_panel)

        self.init_left_panel()
        self.init_right_panel()

    def init_left_panel(self):
        layout = QVBoxLayout(self.left_panel)

        self.name_label = QLabel("Name:")
        self.name_entry = QLineEdit()

        self.quantity_label = QLabel("Quantity:")
        self.quantity_entry = QLineEdit()

        self.price_label = QLabel("Price:")
        self.price_entry = QLineEdit()

        self.expiry_date_label = QLabel("Expiry Date:")
        self.expiry_date_entry = QLineEdit()

        add_button = QPushButton("Add Item")
        add_button.clicked.connect(self.add_item)

        remove_button = QPushButton("Remove Selected Items")
        remove_button.clicked.connect(self.remove_selected_items)

        clear_button = QPushButton("Clear Entry Fields")
        clear_button.clicked.connect(self.clear_entry_fields)

        save_button = QPushButton("Save Inventory")
        save_button.clicked.connect(self.save_inventory)

        selectall_button = QPushButton("Select all the items")
        selectall_button.clicked.connect(self.select_all_items)

        deselectall_button = QPushButton("DeSelect all the items")
        deselectall_button.clicked.connect(self.deselect_all_items)

        sort_by_name_button = QPushButton("Sort By Name")
        sort_by_name_button.clicked.connect(self.sort_items_by_name)

        sort_by_quantity_button = QPushButton("Sort By Quantity")
        sort_by_quantity_button.clicked.connect(self.sort_items_by_quantity)

        sort_by_price_button = QPushButton("Sort By Price")
        sort_by_price_button.clicked.connect(self.sort_items_by_price)

        about_button = QPushButton("About the Application")
        about_button.clicked.connect(self.show_about)

        calculate_item_value_button = QPushButton("Calculate the Total Value of All the items")
        calculate_item_value_button.clicked.connect(self.calculate_item_value)

        import_button = QPushButton("Export Selected Items")
        import_button.clicked.connect(self.import_inventory)

        export_button = QPushButton("Export Selected Items")
        export_button.clicked.connect(self.export_inventory)

        layout.addWidget(self.name_label)
        layout.addWidget(self.name_entry)
        layout.addWidget(self.quantity_label)
        layout.addWidget(self.quantity_entry)
        layout.addWidget(self.price_label)
        layout.addWidget(self.price_entry)
        layout.addWidget(self.expiry_date_label)
        layout.addWidget(self.expiry_date_entry)
        layout.addWidget(add_button)
        layout.addWidget(remove_button)
        layout.addWidget(clear_button)
        layout.addWidget(save_button)
        layout.addWidget(calculate_item_value_button)
        layout.addWidget(selectall_button)
        layout.addWidget(deselectall_button)
        layout.addWidget(sort_by_name_button)
        layout.addWidget(sort_by_quantity_button)
        layout.addWidget(sort_by_price_button)
        layout.addWidget(about_button)
        layout.addWidget(import_button)
        layout.addWidget(export_button)

    def init_right_panel(self):
        layout = QVBoxLayout(self.right_panel)

        self.table_widget = QTableWidget()
        self.table_widget.setColumnCount(4)
        self.table_widget.setHorizontalHeaderLabels(["Name", "Quantity", "Price", "Expiry Date"])
        self.table_widget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

        layout.addWidget(self.table_widget)

        self.load_inventory()

    def load_inventory(self):
        with open("C:\\Users\\HP\\inventory.csv") as file:
            reader = csv.reader(file)
            header = next(reader)
            self.table_widget.setRowCount(0)
            for row_data in reader:
                row_count = self.table_widget.rowCount()
                self.table_widget.insertRow(row_count)
                for col, value in enumerate(row_data):
                    self.table_widget.setItem(row_count, col, QTableWidgetItem(value))

    def add_item(self):
        name = self.name_entry.text()
        quantity = self.quantity_entry.text()
        price = self.price_entry.text()
        expiry_date = self.expiry_date_entry.text()

        if not name or not quantity or not price or not expiry_date:
            QMessageBox.warning(self, "Error", "Please fill in all the fields.")
            return

        row_count = self.table_widget.rowCount()
        self.table_widget.insertRow(row_count)
        self.table_widget.setItem(row_count, 0, QTableWidgetItem(name))
        self.table_widget.setItem(row_count, 1, QTableWidgetItem(quantity))
        self.table_widget.setItem(row_count, 2, QTableWidgetItem(price))
        self.table_widget.setItem(row_count, 3, QTableWidgetItem(expiry_date))

        self.clear_entry_fields()

    def remove_selected_items(self):
        selected_rows = self.table_widget.selectionModel().selectedRows()
        if not selected_rows:
            QMessageBox.warning(self, "Error", "No items selected.")
            return

        reply = QMessageBox.question(
            self, "Confirm Deletion", "Are you sure you want to remove the selected items?",
            QMessageBox.Yes | QMessageBox.No
        )
        if reply == QMessageBox.Yes:
            for row in reversed(selected_rows):
                self.table_widget.removeRow(row.row())

    def clear_entry_fields(self):
        self.name_entry.clear()
        self.quantity_entry.clear()
        self.price_entry.clear()
        self.expiry_date_entry.clear()

    def select_all_items(self):
        self.table_widget.selectAll()

    def deselect_all_items(self):
        self.table_widget.clearSelection()

    def sort_items_by_name(self):
        self.table_widget.sortItems(0)

    def sort_items_by_quantity(self):
        self.table_widget.sortItems(1)

    def sort_items_by_price(self):
        self.table_widget.sortItems(2)

    def sort_items_by_exp(self):
        self.table_widget.sortItems(3)

    def show_about(self):
        QMessageBox.about(self, "About", "Inventory Management System\nVersion 1.0")

    def save_inventory(self):
        file_name, _ = QFileDialog.getSaveFileName(
            self, "Save Inventory", "", "CSV Files (*.csv)"
        )

        if file_name:
            with open(file_name, "w", newline="") as file:
                writer = csv.writer(file)
                writer.writerow(["Name", "Quantity", "Price", "Expiry Date"])
                for row in range(self.table_widget.rowCount()):
                    row_data = [
                        self.table_widget.item(row, 0).text(),
                        self.table_widget.item(row, 1).text(),
                        self.table_widget.item(row, 2).text(),
                        self.table_widget.item(row, 3).text(),
                    ]
                    writer.writerow(row_data)

            QMessageBox.information(self, "Success", "Inventory saved successfully.")

    def import_inventory(self):
        file_name, _ = QFileDialog.getOpenFileName(
            self, "Import Inventory", "", "CSV Files (*.csv)"
        )

        if file_name:
            with open(file_name, "r") as file:
                reader = csv.reader(file)
                header = next(reader)
                self.table_widget.clearContents()
                self.table_widget.setRowCount(0)
                for row_data in reader:
                    row_count = self.table_widget.rowCount()
                    self.table_widget.insertRow(row_count)
                    for col, value in enumerate(row_data):
                        self.table_widget.setItem(row_count, col, QTableWidgetItem(value))
            QMessageBox.information(self, "Success", "Inventory imported successfully.")

    def export_inventory(self):
        file_name, _ = QFileDialog.getSaveFileName(
            self, "Export Inventory", "", "CSV Files (*.csv)"
        )

        if file_name:
            selected_rows = self.table_widget.selectionModel().selectedRows()
            if not selected_rows:
                QMessageBox.warning(self, "Error", "No items selected.")
                return

            with open(file_name, "w", newline="") as file:
                writer = csv.writer(file)
                writer.writerow(["Name", "Quantity", "Price", "Expiry Date"])
                for row in selected_rows:
                    row_data = [
                        self.table_widget.item(row.row(), 0).text(),
                        self.table_widget.item(row.row(), 1).text(),
                        self.table_widget.item(row.row(), 2).text(),
                        self.table_widget.item(row.row(), 3).text(),
                    ]
                    writer.writerow(row_data)

            QMessageBox.information(self, "Success", "Inventory exported successfully.")

    def closeEvent(self, event):
        reply = QMessageBox.question(
            self, "Confirm Exit", "Are you sure you want to exit the Inventory Management System?",
            QMessageBox.Yes | QMessageBox.No
        )
        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()

    def calculate_item_value(self):
        selected_rows = self.table_widget.selectionModel().selectedRows()
        if not selected_rows:
            QMessageBox.warning(self, "Error", "No items selected.")
            return

        total_value = 0.0
        for row in selected_rows:
            item_quantity = float(self.table_widget.item(row.row(), 1).text())
            item_price = float(self.table_widget.item(row.row(), 2).text())
            item_value = item_quantity * item_price
            total_value += item_value

        QMessageBox.information(self, "Item Value", f"The total value of the selected items is: {total_value}")

    

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ims = InventoryManagementSystem()
    ims.show()
    sys.exit(app.exec_())