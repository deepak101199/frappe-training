import frappe

def get_context(context):
    
    form= frappe.get_doc("Article Library","deepak")

    context={
        "form":form
    }


    return context
     