# IT5016_Assessment-3
# Requisition System

## Overview

The **Requisition System** is a requisition management and processing application built using classes in Python. The requisition records can be created, personnel information can be updated, items can be added, requisitions can be approved or rejected based on their overall cost, and statistics on requisition statuses can be generated using this system.
## Features

- **Unique Requisition IDs**: creates distinct IDs automatically for every request.
- **Staff Management**:Update the staff data linked to the requests.
- **Requisition Details**:Compute the overall cost by adding goods to requisitions.
- **Approval System**: Requisitions that amount less than $500 will be automatically approved; those that don't should be marked as 'Pending'.
- **Response Handling**: Respond to requisitions with 'Approved' or 'Not Approved'.
- **Statistics Generation**: Get statistics on the number of requisitions in various statuses (Approved, Not Approved, Pending).

## Exemple Output

Requisition Statistics: {'Total Requisitions': 5, 'Approved': 2, 'Not Approved': 0, 'Pending': 3}
{'Date': datetime.datetime(2024, 9, 18, 10, 34, 37, 535916), 'Staff ID': '123', 'Staff Name': 'ismit', 'Requisition ID': 10071, 'Items': [('Item1', 200), ('Item2', 150)], 'Total Cost': 350, 'Status': 'Approved'}  
{'Date': datetime.datetime(2024, 9, 18, 10, 34, 37, 535916), 'Staff ID': '1234', 'Staff Name': 'gurnoor', 'Requisition ID': 10072, 'Items': [('Item3', 300), ('Item4', 200)], 'Total Cost': 500, 'Status': 'Pending'}
{'Date': datetime.datetime(2024, 9, 18, 10, 34, 37, 535916), 'Staff ID': '12345', 'Staff Name': 'saraj', 'Requisition ID': 10073, 'Items': [('Item5', 600), ('Item6', 50)], 'Total Cost': 650, 'Status': 'Pending'}  
{'Date': datetime.datetime(2024, 9, 18, 10, 34, 37, 535916), 'Staff ID': '001', 'Staff Name': 'emon', 'Requisition ID': 10074, 'Items': [('Item7', 100), ('Item8', 350)], 'Total Cost': 450, 'Status': 'Approved'}   
{'Date': datetime.datetime(2024, 9, 18, 10, 34, 37, 535916), 'Staff ID': '002', 'Staff Name': 'shobin', 'Requisition ID': 10075, 'Items': [('Item9', 500), ('Item10', 100)], 'Total Cost': 600, 'Status': 'Pending'} 


