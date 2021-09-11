// Copyright (c) 2021, deepak and contributors
// For license information, please see license.txt

frappe.ui.form.on('Library membership', {
	after_save: function(frm){
		frappe.msgprint("your membership is updated")
	}
	// refresh: function(frm) {

	// }
});
