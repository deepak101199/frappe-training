frappe.pages['custom-page'].on_page_load = function (wrapper) {
	new PageContent(wrapper);

};
PageContent = Class.extend({
	init: function (wrapper) {
		this.page = frappe.ui.make_app_page({
			parent: wrapper,
			title: 'Custom page',
			single_column: true
		});
		this.make();
	},
	make: function () {
		let htmlContent = `<div>
		
		<h1 id=article-count>css test</h1>
		<h2>test heading</h2>
		</div>
			<button type="button" class="btn btn-outline-primary">Primary</button>
	
		`;
	let articleCount=function(){
		frappe.call({
			method: 
				"book_selling.book_selling.page.custom_page.custom_page.get_article_count",
			callback: function(articleCount){
				console.log(articleCount)
				$("#article-count").text(articleCount.message);
			},
		});};
		$(frappe.render_template(htmlContent, this)).appendTo(this.page.main);
		articleCount();
	},
});