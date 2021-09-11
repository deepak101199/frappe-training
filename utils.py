import frappe

# #validate
# def test_hook(doc,event):
#     msg=doc.article_cost
#     frappe.msgprint(msg)

# #after_insert
# def save_note(doc,event):
#     doc_title=doc.article
#     new_note=frappe.get_doc({
#         "doctype":"Note",
#         "title":doc_title,
#         "content":"new article created"
#     })
#     new_note.insert()
#     # frappe.db.commit()

def save_note(doc,event):
    doc_title=doc.article
    cost=doc.total_cost
    new_note=frappe.get_doc({
        "doctype":"hook",
        "name1":doc_title,
        "cost":cost
    })
    new_note.insert()


# #before_insert
# def bfsubmit(doc,event):
#         if((doc.article,doc.author,doc.article_cost,doc.deliver_cost)==None):
#             frappe.throw("fill all feilds")

# #on_update
# def onupdate(doc,event):
#     article=doc.total_cost
#     if(article>500):
#         frappe.throw("price is should be lessthan 500")

# #on_trash
# def ontrash(doc,event):
#     name=doc.article
#     frappe.msgprint("you are deleting the document")

# #after_delete
# def afterdelete(doc,event):
#     frappe.msgprint("you have sucsess fully deleted the document")

# #after_rename
# def afterrename(doc,event):
#     frappe.msgprint("you have renamed sucssesfully")


#writing custom api in the erpnext ecosystem

@frappe.whitelist(allow_guest=True)
def get_author_articles(author=None,total_cost=None):
    articles = frappe.db.sql(f""" SELECT * FROM `tabArticle Library` WHERE total_cost ='{total_cost}';""", as_dict=True)
    return articles