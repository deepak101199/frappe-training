import frappe

#get
@frappe.whitelist(allow_guest=True)
def get_first():
    member=frappe.db.sql(f"""select * from `tabLibrary member`;""",as_dict=True)
    return member


#post
@frappe.whitelist(allow_guest=True)
def get_first_name(full_name=None):

    member=frappe.db.sql(f"""select first_name,last_name from `tabLibrary member` where full_name='{full_name}';""",as_dict=True)
    return member

#update
@frappe.whitelist(allow_guest=True)
def update_member(full_name):
    member=frappe.db.sql(f"""update `tabLibrary member` set first_name='peepak' where full_name='{full_name}';""")
    
#delete
@frappe.whitelist(allow_guest=True)
def delete_member(full_name):
    member=frappe.db.sql(f"""delete from `tabLibrary member` where full_name='{full_name}';""")
    
# @frappe.whitelist(allow_guest=True)
# def post_test:
#     if frappe.request.data:
#         return True
#     else:
#         return False