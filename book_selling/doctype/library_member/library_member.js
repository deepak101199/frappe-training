// Copyright (c) 2021, deepak and contributors
// For license information, please see license.txt

frappe.ui.form.on('Library member', {
	first_name: function(frm){
		let fname=frm.doc.first_name;
		let lname=frm.doc.last_name;
		frm.set_value("full_name",fname + " " +lname)
	},
	last_name: function(frm){
		let fname=frm.doc.first_name;
		let lname=frm.doc.last_name;
		frm.set_value("full_name",fname + " " +lname)
	}
	// refresh: function(frm) {

	// }
});
