# Copyright (c) 2024, Madhu Nishad and contributors
# For license information, please see license.txt

# Copyright (c) 2024, BWH and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
import random

class AirplaneTicket(Document):
    
    def validate(self):
        total = self.flight_price
        if self.add_ons:
            unique_add_ons = set()
            valid_add_ons = []

            for add_on in self.add_ons:
                if add_on.add_on_type in unique_add_ons:
                    frappe.msgprint(f"Duplicate add-on: {add_on.add_on_type}")
                else:
                    unique_add_ons.add(add_on.add_on_type)
                    valid_add_ons.append(add_on)
                    total += add_on.amount
            
            self.add_ons = valid_add_ons
        self.total_amount = total

        self.validate_ticket_capacity()

    def before_insert(self):
        random_integer = random.randint(1, 3)
        random_alphabate = random.choice(['A','B','C','D','E'])
        self.seat = f"{ random_integer}{ random_alphabate}"
        
        random_int = random.randint(1, 3)
        random_alpha = random.choice(['G'])
        self.gate_number = f"{ random_int}{ random_alpha}"
            
    
    def before_submit(document):
        if document.status != "Boarded":
            frappe.throw("This Airplane Ticket cannot be submitted because its status is not 'Boarded'.")
          
    def validate_ticket_capacity(self):
        flight_doc = frappe.get_doc("Airplane Flight", self.flight)

        airplane_doc = frappe.get_doc("Airplane", flight_doc.airplane)
        capacity = airplane_doc.capacity

        issued_tickets = frappe.db.count("Airplane Ticket", filters={"flight": self.flight})

        if issued_tickets >= capacity:
            frappe.throw(f"Cannot create a new ticket. The number of issued tickets ({issued_tickets}) exceeds the airplane's capacity ({capacity}).")
