// Copyright (c) 2021, deepak and contributors
// For license information, please see license.txt

frappe.ui.form.on('Article Library', {
	refresh: function(frm) {
		frm.add_custom_button("get author article",() => {
		let author=frm.doc.author;
		let total_cost=frm.doc.total_cost
		
		frappe.call({
			method: "book_selling.utils.get_author_articles",
			args: {
				author: author ,
				total_cost:total_cost
			},
			callback: function(articles){
				console.log(articles)
			},
		});
	},"Action"
	);
	},
	article_cost: function(frm){
		let arcost=parseInt(frm.doc.article_cost);
		let dcost=parseInt(frm.doc.deliver_cost);
		let tcost=arcost+dcost
		frm.set_value("total_cost",tcost)
	},
	deliver_cost: function(frm){
		let arcost=parseInt(frm.doc.article_cost);
		let dcost=parseInt(frm.doc.deliver_cost);
		let tcost=arcost+dcost
		frm.set_value("total_cost",tcost)
	}
	
});
