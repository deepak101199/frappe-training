# Copyright (c) 2021, deepak and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document
from datetime import date,timedelta
class Librarymembership(Document):
	def before_save(self):
		today_date=date.today()
		self.from_date=today_date
		number_of_date_to_add=(self.no_month)*30
		End_date=today_date+timedelta(days=number_of_date_to_add)
		self.to_date=End_date
	
