import frappe

def execute(filters=None):
    columns = [
        {"label": "Airline", "fieldname": "airline", "fieldtype": "Link", "options": "Airplane"},
        {"label": "Revenue", "fieldname": "revenue", "fieldtype": "Currency"}
    ]
    
    data = get_revenue_by_airline()
    
    total_revenue = sum(row['revenue'] for row in data)
    
    data.append({"airline": "Total", "revenue": total_revenue})
    
    chart = { 
        "data": {
            "labels": [row['airline'] for row in data],
            "datasets": [{"values": [row['revenue'] for row in data]}],
        },
        "type": "donut",
    }
    
    return columns, data, "Here is the report", chart

def get_revenue_by_airline():
    query = """
        SELECT 
            flight AS airline, 
            IFNULL(SUM(total_amount), 0) AS revenue
        FROM 
            `tabAirplane Ticket`
        GROUP BY 
            flight
    """
    return frappe.db.sql(query, as_dict=True)
    
