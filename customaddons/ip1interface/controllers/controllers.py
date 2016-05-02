# -*- coding: utf-8 -*-
from openerp import http

# class Ip1interface(http.Controller):
#     @http.route('/ip1interface/ip1interface/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/ip1interface/ip1interface/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('ip1interface.listing', {
#             'root': '/ip1interface/ip1interface',
#             'objects': http.request.env['ip1interface.ip1interface'].search([]),
#         })

#     @http.route('/ip1interface/ip1interface/objects/<model("ip1interface.ip1interface"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('ip1interface.object', {
#             'object': obj
#         })