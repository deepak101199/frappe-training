// Copyright (c) 2021, deepak and contributors
// For license information, please see license.txt

frappe.ui.form.on('Membership Payment', {
	no_of_month: function(frm){
		let nmonth=frm.doc.no_of_month;
		let tot=nmonth * 200;
		frm.set_value("total_fee",tot)
	},
	after_save: function(frm){
		frappe.msgprint("payment sucsessful")
	}
	// refresh: function(frm) {

	// }
});
