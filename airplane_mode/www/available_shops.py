import frappe

def get_context(context):
    # Fetch shops with status 'Available'
    context.available_shops = frappe.get_all(
        "Shop",
        filters={"status": "Available"},
        fields=["tenant", "shop_name", "area", "rent_amount"]
    )
    
    # Debug: print to console or use frappe.msgprint to display on screen
    print("Fetched shops:", context.available_shops)
    frappe.msgprint(f"Fetched shops: {context.available_shops}")
    
    return context
