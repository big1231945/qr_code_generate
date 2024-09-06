# Copyright (c) 2024, Thanakorn Sonong and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

from qr_code_generate.qr_code import get_qr_code

class QRUser(Document):
	def validate(self):
		self.qr_code = get_qr_code(f'https://ecomm.erpeazy.com/user_data?name={self.name}')

	# @frappe.whitelist()
	# def generate_qr_code(self):
	# 	self.qr_code = get_qr_code(f'https://ecomm.erpeazy.com/user_data?name={self.name}')
	@frappe.whitelist()
	def generate_qr_code(self):
		for i in self.user_table:
			i.qr_code = get_qr_code(f'https://ecomm.erpeazy.com/user_data?name={i.name_surename}&id={self.name}')


@frappe.whitelist(allow_guest=True)
def get_doctype_data(name,id):
	try:
		# ดึงข้อมูลจาก Doctype
		doc = frappe.get_doc("QR User", id)
		for i in doc.user_table:
			if i.name_surename == name:
				data = {
					"company_name": i.company_name,
					"name_surename": i.name_surename,
					"email_address": i.email_address,
					"telephone_no": i.telephone_no
				}
		return data
	except frappe.DoesNotExistError:
		frappe.throw(frappe._("Document not found"), frappe.DoesNotExistError)
