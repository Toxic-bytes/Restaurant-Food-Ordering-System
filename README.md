
# Restaurant Food Ordering System

## Project Overview
The Restaurant Food Ordering System is a console-based application developed using Core Python. It allows users to view the food menu, place orders, calculate bills, apply discounts, and store order details in CSV files.

## Features
- Display the food menu with food IDs and prices.
- Place orders by entering Food ID and quantity.
- Validate user input.
- Calculate subtotal and final bill amount.
- Apply a 10% discount when the subtotal is above Rs.500.
- Generate unique order IDs.
- Save order details in a CSV file.
- View all previously saved orders.
- Exit the application.

## Technology Stack
- Programming Language: Python 
- File Handling: CSV
- Date Handling: datetime module
- Concepts: Classes, Objects, Methods, Loops, Conditional Statements, and Exception Handling.

## Project Files
- `restaurant.py` - Main Python application.
- `menu.csv` - Stores food IDs, food names, and prices.
- `orders.csv` - Stores order details, dates, quantities, and bill amounts.

## Setup and Run Instructions

1. Install Python  on your computer.
2. Download or clone this repository.
3. Open the project folder in VS Code or a terminal.
4. Make sure all three project files are in the same folder.
5. Run the following command:

```bash
python restaurant.py
```

## Environment Variables
This project does not require any environment variables or additional configuration.

## API and Database Notes
- This project does not use external APIs.
- It does not use MySQL or any other database.
- CSV files are used to store menu and order information.

## Team Member Contributions

**Project Developer:** Gummadi Dhananjaya Krishna

- Designed and developed the application using Core Python.
- Implemented menu display and order placement.
- Developed bill calculation and discount functionality.
- Implemented unique order ID generation.
- Used CSV file handling to save and retrieve order records.
- Tested the main application features.

## Future Improvements
- Allow multiple food items in one order.
- Add options to update or cancel orders.
- Introduce a graphical user interface.
- Integrate a database such as MySQL.

## Project Status
Completed as a beginner-level Core Python project.
