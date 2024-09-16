from datetime import datetime

# Creating class named RequisitionSystem
class RequisitionSystem:
    requisition_counter = 10070  # Class-level counter for unique IDs
    
    def __init__(self, date, staff_id, staff_name):
        # Initializing the requisition details
        self.date = date
        self.staff_id = staff_id
        self.staff_name = staff_name
        RequisitionSystem.requisition_counter += 1
        self.requisition_id = RequisitionSystem.requisition_counter  # Generating unique ID
        self.items = []
        self.status = 'Pending'

    # Method to update staff information
    def staff_info(self, staff_id, staff_name):
        self.staff_id = staff_id
        self.staff_name = staff_name
        
    # Method to update requisition details
    def requisition_details(self, items):
        self.items = items
        total = sum(cost for _, cost in items)
        return total

    # Method to approve or reject requisition
    def requisition_approval(self):
        total = self.requisition_details(self.items)
        if total >= 500:
            self.status = 'Pending'  # Initial status
        else:
            self.status = 'Approved'  # Auto-approved if total < 500

    # Method to respond to requisition
    def respond_requisition(self, response):
        if self.status == 'Pending':
            if response == 'Approved':
                self.status = 'Approved'
            elif response == 'Not Approved':
                self.status = 'Not Approved'
            else:
                print("Invalid response. Status remains Pending.")
        else:
            print("Requisition already processed.")

    # Method to display requisition information
    def display_requisition(self):
        return {
            'Date': self.date,
            'Staff ID': self.staff_id,
            'Staff Name': self.staff_name,
            'Requisition ID': self.requisition_id,
            'Items': self.items,
            'Total Cost': self.requisition_details(self.items),
            'Status': self.status
        }

    # Method to display requisition statistics
    @staticmethod
    def requisition_statistic(requisitions):
        total_requisitions = len(requisitions)
        approved = sum(1 for req in requisitions if req.status == 'Approved')
        not_approved = sum(1 for req in requisitions if req.status == 'Not Approved')
        pending = total_requisitions - approved - not_approved
        
        return {
            'Total Requisitions': total_requisitions,
            'Approved': approved,
            'Not Approved': not_approved,
            'Pending': pending
        }

# Test script
if __name__ == "__main__":
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