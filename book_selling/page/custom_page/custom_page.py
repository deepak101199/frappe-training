import frappe


@frappe.whitelist()
def get_article_count():
    return frappe.db.sql("""select count(*) from `tabArticle Library`;""")