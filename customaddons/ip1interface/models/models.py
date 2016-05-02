from openerp.osv import osv
import requests
from openerp.exceptions import except_orm
from openerp.osv import osv, fields

class ip1parts(osv.osv):
    _name = 'product.template'
    _inherit = 'product.template'
    _columns = {'product_number': fields.char('Product Number')}

class ip1interface(osv.osv):
    _name = 'mrp.production'
    _inherit = 'mrp.production'

    def action_in_production(self, cr, uid, ids, context=None):
        production = self.browse(cr, uid, ids, context=context)
        for prod in production:
            bom_obj = self.pool.get('mrp.bom').browse(cr, uid, prod.bom_id.id, context=context)
            part_numbers = []
            for line in bom_obj.bom_line_ids:
                part_numbers.append(line.product_id.product_tmpl_id.product_number)
            data = {"order_id": prod.name, "quantity": prod.product_qty, "part_numbers": part_numbers}

        #Connect to IP1 and invoke the create new order method
        ip1IPAddress = 'http://192.168.178.72'
        r = requests.post(ip1IPAddress + '/ExecutionEngineWeb/api/orders/createnewodoo', json=data)

        #If the order was successfully created on IP1 then set the order to production, ortherwise throw error
        if(r.json() == True):
            super(ip1interface, self).action_in_production(cr, uid, ids, context)
        else:
             raise except_orm('IP1 Connection','An error occurred when creating the order on IP1!')
        return self