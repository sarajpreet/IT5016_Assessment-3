# Assignment 3 
# Requisition System

## Overview

The Requisition System is a Python class that is created for the purpose of overseeing and handling requisitions within a company. It enables the creation of requisitions, staff information updates, total cost calculations, requisition approval or rejection based on cost, and requisition statistics generation.
## Property

- Unique Requisition IDs: Automatically generating a unique ID for each requisition members.
- Dynamic Status Updates: Approving or rejecting requisitions IDs based on total cost.
- Statistics Generation: Providing statistics on requisition IDs statuses.
- Flexible Item Management: Supporting and adding multiple items and calculating their total cost.
- Date Handling: Recording and displaying the date of requisitions IDs.

## Class Properties

- date: The date and time when the requisition is created.
- staff id: The staff ID of the staff member making the requisition.
- staff name: The staff name of the staff member making the requisition.
- requisition id: A unique ID automatically assigned to each requisition member.
- items: A list of items where each item contains an item name and its cost.
- total:= requisition total is total cost for all item.
- status:  Pending, Approved or Not Approved is current status of the requisition.

## Methods

- __init__(self, date, staff_id, staff_name): Initializing a new requisition with the date,  ID, and name.
- staff_info: Updating the staff ID and name.
- requisition_detai: Approving the items and calculates the total cost.
- requisition_approval: Approving the requisition status based on the total cost.
- respond_requisition: Responding to the requisition, changing the status if it is still 'Pending'.
- display_requisition: Returning a dictionary with the requisition's details.
- requisition_statistic: Generating statistics on the list of requisitions.

## Example Usage

```python
from datetime import datetime
from requisition_system import RequisitionSystem  # Adjust the import based on your file structure

# Create instances of requisitions
requisitions = []

# Example 1: Requisition with total less than $500
req1 = RequisitionSystem(datetime.now(), '1', 'i')
req1.requisition_details([('Item1', 200), ('Item2', 149)])
req1.requisition_approval()
requisitions.append(req1)

# Example 2: Requisition with total exactly $500
req2 = RequisitionSystem(datetime.now(), '12', 'g')
req2.requisition_details([('Item3', 300), ('Item4', 199)])
req2.requisition_approval()
requisitions.append(req2)

# Example 3: Requisition with total greater than $500
req3 = RequisitionSystem(datetime.now(), '123', 's')
req3.requisition_details([('Item5', 600), ('Item6', 49)])
req3.requisition_approval()
requisitions.append(req3)

# Example 4: Requisition with total less than $500
req4 = RequisitionSystem(datetime.now(), '1', 'e')
req4.requisition_details([('Item7', 100), ('Item8', 349)])
req4.requisition_approval()
requisitions.append(req4)

# Example 5: Requisition with total greater than $500
req5 = RequisitionSystem(datetime.now(), '2', 's')
req5.requisition_details([('Item9', 500), ('Item10', 99)])
req5.requisition_approval()
requisitions.append(req5)

# Display requisition statistics
stats = RequisitionSystem.requisition_statistic(requisitions)
print("Requisition Statistics:", stats)

# Display each requisition's details
for req in requisitions:
    print(req.display_requisition())
 
