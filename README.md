# Assignment 3 
# Requisition System

## Overview

The Requisition System is a Python class designed to manage and process requisitions in an organization. It allows for creating requisitions, updating staff information, calculating total costs, approving or rejecting requisitions based on cost, and generating statistics about requisitions.

## Features

- **Unique Requisition IDs**: Automatically generates a unique ID for each requisition.
- **Dynamic Status Updates**: Approves or rejects requisitions based on total cost.
- **Statistics Generation**: Provides statistics on requisition statuses.
- **Flexible Item Management**: Supports adding multiple items and calculating their total cost.
- **Date Handling**: Records and displays the date of requisitions.

## Class Properties

- `date`: The date and time when the requisition is created.
- `staff_id`: The ID of the staff member making the requisition.
- `staff_name`: The name of the staff member making the requisition.
- `requisition_id`: A unique ID automatically assigned to each requisition.
- `items`: A list of tuples where each tuple contains an item name and its cost.
- `status`: The current status of the requisition (Pending, Approved, Not Approved).
- `total_cost`: The total cost of all items in the requisition.

## Methods

- **`__init__(self, date, staff_id, staff_name)`**: Initializes a new requisition with the given date, staff ID, and staff name.
- **`staff_info(self, staff_id, staff_name)`**: Updates the staff ID and name.
- **`requisition_details(self, items)`**: Sets the items and calculates the total cost.
- **`requisition_approval(self)`**: Approves or sets the requisition status based on the total cost.
- **`respond_requisition(self, response)`**: Responds to the requisition, changing the status if it is still 'Pending'.
- **`display_requisition(self)`**: Returns a dictionary with the requisition's details.
- **`requisition_statistic(requisitions)`**: Generates statistics on the list of requisitions.

## Example Usage

```python
from datetime import datetime
from requisition_system import RequisitionSystem  # Adjust the import based on your file structure

# Create instances of requisitions
requisitions = []

# Example 1: Requisition with total less than $500
req1 = RequisitionSystem(datetime.now(), '123', 'ismit')
req1.requisition_details([('Item1', 200), ('Item2', 150)])
req1.requisition_approval()
requisitions.append(req1)

# Example 2: Requisition with total exactly $500
req2 = RequisitionSystem(datetime.now(), '1234', 'gurnoor')
req2.requisition_details([('Item3', 300), ('Item4', 200)])
req2.requisition_approval()
requisitions.append(req2)

# Example 3: Requisition with total greater than $500
req3 = RequisitionSystem(datetime.now(), '12345', 'saraj')
req3.requisition_details([('Item5', 600), ('Item6', 50)])
req3.requisition_approval()
requisitions.append(req3)

# Example 4: Requisition with total less than $500
req4 = RequisitionSystem(datetime.now(), '001', 'emon')
req4.requisition_details([('Item7', 100), ('Item8', 350)])
req4.requisition_approval()
requisitions.append(req4)

# Example 5: Requisition with total greater than $500
req5 = RequisitionSystem(datetime.now(), '002', 'shobin')
req5.requisition_details([('Item9', 500), ('Item10', 100)])
req5.requisition_approval()
requisitions.append(req5)

# Display requisition statistics
stats = RequisitionSystem.requisition_statistic(requisitions)
print("Requisition Statistics:", stats)

# Display each requisition's details
for req in requisitions:
    print(req.display_requisition())
 
