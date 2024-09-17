# IT5016_Assessment-3
# Requisition System

## Overview

The **Requisition System** is a Python class-based application designed to manage and process requisitions. This system allows for the creation of requisition records, updating staff information, adding items, approving or rejecting requisitions based on their total cost, and generating statistics on requisition statuses.

## Features

- **Unique Requisition IDs**: Automatically generates unique IDs for each requisition.
- **Staff Management**: Update staff information associated with requisitions.
- **Requisition Details**: Add items to requisitions and calculate total costs.
- **Approval System**: Automatically approve requisitions with a total cost below $500 and set to `Pending` otherwise.
- **Response Handling**: Respond to requisitions with 'Approved' or 'Not Approved'.
- **Statistics Generation**: Get statistics on the number of requisitions in various statuses (Approved, Not Approved, Pending).

## Installation

To use the Requisition System, you need Python installed on your system. This project doesn't have external dependencies, so no additional installations are required beyond Python itself.

1. **Clone the Repository**

   ```bash
   git clone https://github.com/yourusername/requisition-system.git
   cd requisition-system
