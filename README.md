# Smart-Inventory-Mutation-Tracker
## Overview
This project analyzes how data behaves when copied in Python using a warehouse inventory system. Each product contains nested details such as price, stock, and supplier information.

## Features
Creation of inventory using nested dictionaries
Use of shallow copy and deep copy
Price reduction applied to all items
Stock and supplier rating modified based on roll number logic
Comparison of original and copied data
Detection of changes using functions and conditions

## Data Structure
Each item contains item name and nested details including price, stock, and supplier information. All items are stored in a list.

## Functions Used
build_inventory(): Creates the inventory data
update_data(data, roll_no): Applies discount and modifications
check_difference(data1, data2): Compares original and modified data

## Personalization Logic
Index = roll number modulo length of inventory
This ensures only one specific item is modified based on roll number

## Processing Logic
Price is reduced by 10 percent for all items
Stock and supplier rating are modified only for the selected index

## How to Run
Run the Python file
Enter the roll number when prompted

## Output
Original inventory data
Shallow copy result
Deep copy result
Differences shown as tuple of changed and unchanged items
Explanation of behavior

## Learning Outcome
This project helped in understanding nested data structures, functions, and the difference between shallow copy and deep copy in Python.
