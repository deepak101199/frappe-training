# Copyright (c) 2021, deepak and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class ArticleLibrary(Document):
	
	def validate(self):
		if(self.track_buyer==0):
			if (self.buyer):
				frappe.throw("this article does not allow track buyer")
