import frappe
from frappe.model.document import Document

class Shop(Document):
    def before_insert(self):
        # Fetch settings from "Airport Shop Settings" Single DocType
        settings = frappe.get_single("Airport Shop Settings")
        
        # Check if default_rent_amount exists in settings
        if settings.default_rent_amount:
            # Set the default rent amount if rent_amount is not provided
            if not self.rent_amount:
                self.rent_amount = settings.default_rent_amount
                print(f"Default rent amount set to: {self.rent_amount}")
        else:
            print("Default rent amount not set in Airport Shop Settings")
