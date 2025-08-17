# Inventory Management System

A comprehensive desktop application built with PyQt5 for managing inventory items with an intuitive GUI interface.

## Features

### Core Functionality
- **Add Items**: Create new inventory entries with name, quantity, price, and expiry date
- **Remove Items**: Delete selected items with confirmation dialog
- **Edit & Update**: Modify existing inventory data through the table interface
- **Clear Fields**: Reset input fields with a single click

### Data Management
- **CSV Import/Export**: Load and save inventory data from/to CSV files
- **Save Inventory**: Export complete inventory to custom file locations
- **Export Selected**: Save only selected items to a separate file
- **Auto-load**: Automatically loads inventory from `inventory.csv` on startup

### Organization & Sorting
- **Sort by Name**: Alphabetical sorting of items
- **Sort by Quantity**: Numerical sorting by stock levels
- **Sort by Price**: Organize items by price value
- **Select All/Deselect All**: Bulk selection controls

### Analysis Tools
- **Calculate Total Value**: Compute the total monetary value of selected items
- **Item Selection**: Multi-select items for batch operations

## Requirements

- Python 3.x
- PyQt5
- CSV module (built-in)

## Installation

1. Clone the repository:
```bash
git clone <your-repository-url>
cd inventory-management-system
```

2. Install required dependencies:
```bash
pip install PyQt5
```

3. Create an initial `inventory.csv` file in `C:\Users\HP\` directory with headers:
```csv
Name,Quantity,Price,Expiry Date
```

## Usage

1. Run the application:
```bash
python ims.py
```

2. **Adding Items**: 
   - Fill in the Name, Quantity, Price, and Expiry Date fields
   - Click "Add Item" to add to inventory

3. **Managing Items**:
   - Select items from the table to perform bulk operations
   - Use sort buttons to organize your inventory
   - Remove unwanted items using "Remove Selected Items"

4. **Data Operations**:
   - Save your work using "Save Inventory"
   - Import existing CSV files with "Import Inventory" 
   - Export selected items for sharing or backup

5. **Analysis**:
   - Select items and use "Calculate Total Value" to get monetary worth

## File Structure

```
inventory-management-system/
│
├── ims.py              # Main application file
├── inventory.csv       # Default inventory data file
└── README.md          # This file
```

## Configuration

The application currently loads the default inventory file from:
```
C:\Users\HP\inventory.csv
```

To change the default path, modify line 77 in `ims.py`:
```python
with open("your/custom/path/inventory.csv") as file:
```

## Screenshots

The application features a clean two-panel layout:
- **Left Panel**: Input fields and action buttons
- **Right Panel**: Inventory table with sortable columns

## Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## Future Enhancements

- Database integration (SQLite/MySQL)
- Advanced search and filtering
- Barcode scanning support
- Low stock alerts
- Reporting and analytics dashboard
- Multi-user support with authentication

## License

This project is open source and available under the [MIT License](LICENSE).

## Author

**Adi Rajendra Maitre**  
*B.Tech IT Student*  

Connect with me:
- Portfolio: [adimaitre.pages.dev](https://adimaitre.pages.dev)
- LinkedIn: [linkedin.com/in/adimaitre](https://linkedin.com/in/adimaitre)

---

*"Code with purpose, build with spirit."*