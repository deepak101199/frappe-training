import frappe

def get_context(context):
    
    form= frappe.get_doc("hook","8675344a38")

    context={
        "form":form
    }


    return context
     