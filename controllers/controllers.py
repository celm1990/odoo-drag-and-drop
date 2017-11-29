# -*- coding: utf-8 -*-
from odoo import http

# class Odoo-drag-and-drop(http.Controller):
#     @http.route('/odoo-drag-and-drop/odoo-drag-and-drop/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/odoo-drag-and-drop/odoo-drag-and-drop/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('odoo-drag-and-drop.listing', {
#             'root': '/odoo-drag-and-drop/odoo-drag-and-drop',
#             'objects': http.request.env['odoo-drag-and-drop.odoo-drag-and-drop'].search([]),
#         })

#     @http.route('/odoo-drag-and-drop/odoo-drag-and-drop/objects/<model("odoo-drag-and-drop.odoo-drag-and-drop"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('odoo-drag-and-drop.object', {
#             'object': obj
#         })