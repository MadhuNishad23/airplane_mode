import frappe
from frappe.utils import nowdate, formatdate

def update_shop_counts(doc, method):
    airport_name = doc.airport

    total_shops = frappe.db.count('Shop', filters={'airport': airport_name})
    occupied_shops = frappe.db.count('Shop', filters={'airport': airport_name, 'status': 'Occupied'})
    
    available_shops = total_shops - occupied_shops

    frappe.db.set_value('Airports', airport_name, 'total_shops', total_shops)
    frappe.db.set_value('Airports', airport_name, 'occupied_shops', occupied_shops)
    frappe.db.set_value('Airports', airport_name, 'available_shops', available_shops)


