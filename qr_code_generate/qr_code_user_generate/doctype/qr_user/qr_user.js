// Copyright (c) 2024, Thanakorn Sonong and contributors
// For license information, please see license.txt

frappe.ui.form.on("QR User", {
	refresh(frm) {

	},
    generate_qr(frm){
        frappe.call({
            method: "generate_qr_code",
            doc: frm.doc,
            callback: function (r) {
                frm.refresh_fields();
                frm.save();
                frappe.msgprint({
                title: __('Notification'),
                message: __("QR Code is Generate"),
                indicator: 'green',
                alert: true
            });
            }
          });
        
    }
});
