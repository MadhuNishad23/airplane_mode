// Copyright (c) 2024, Madhu Nishad and contributors
// For license information, please see license.txt

// frappe.ui.form.on("Airplane Ticket", {
// 	refresh(frm) {

// 	},
// });
// Copyright (c) 2024, BWH and contributors
// For license information, please see license.txt

frappe.ui.form.on("Airplane Ticket", {
    refresh(frm) {
        frm.add_custom_button(__('Assign Seat'), function() {
            
            let d = new frappe.ui.Dialog({
                title: 'Enter Seat Number',
                fields: [
                    {
                        label: 'Seat Number',
                        fieldname: 'seat_number',
                        fieldtype: 'Data',
                        reqd: 1 
                    }
                ],
                primary_action_label: 'Set Seat',
                primary_action(values) {
                    frm.set_value('seat', values.seat_number);

                    d.hide();
                }
            });

            d.show();
        }).addClass('btn-primary'); 
    }
});
