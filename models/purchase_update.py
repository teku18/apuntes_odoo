
from openerp.osv import osv, fields
import openerp.addons.decimal_precision as dp

class purchase_order_line(osv.osv):

    def _subtotal_sin_impuestos(self, cr, uid, ids, prop, arg, context=None):
        res = {}
        cur_obj=self.pool.get('res.currency')
        tax_obj = self.pool.get('account.tax')
        for line in self.browse(cr, uid, ids, context=context):
            taxes = tax_obj.compute_all(cr, uid, line.taxes_id, line.price_unit, line.product_qty, line.product_id, line.order_id.partner_id)
            cur = line.order_id.pricelist_id.currency_id
            #res[line.id] = cur_obj.round(cr, uid, cur, taxes['total'])
            res[line.id] = cur_obj.round(cr, uid, cur, line.price_unit * line.product_qty)
            print 'nuevo apartado???'
        print res
        return res

    _inherit='purchase.order.line'

    _columns={
        'subtotal_sin_impuestos': fields.function(_subtotal_sin_impuestos, string='Subtotal', digits_compute=dp.get_precision('Account')),
    }

purchase_order_line()

class purchase_order(osv.osv):
#SOLO SE HEREDA EL MODELO SIN AGREGAR NINGUN OTRO CAMPO O FUNCION
    _inherit='purchase.order'

purchase_order()

class account_invoice(osv.osv):
    def _factura_sin_impuestos(self, cr, uid, ids, prop, arg, context=None):
        res={}

        #BROWSE TRAE LOS DATOS DEL MODELO DEL CUAL ESTA HEREDANDO EN ESTE CASO ES 'account.invoice.line'
        line_obj= self.browse(cr, uid, ids, context=context)

        #TRAE LOS OBJETOS EN FORMA DE LISTA, SE TIENEN QUE RECORRER PARA PODER ACCEDER A ELLOS
        for line in line_obj:
        #SE CREA UN DICCIONARIO EN DONDE AL ID DEL DETALLE DE LA FACTURA SE LE ASIGNA EL RESULTADO DE LA OPERACION
         res[line.id] = line.price_unit * line.quantity

        return res #RETORNAMOS UNA LISTA CON EL SUBTOTAL DE LA OPERACION SIN LOS IMPUESTOS
                   #RETORNO LOS VALORES ASI POR QUE ES EL DETALLE DE LA FACTURA Y ASI LO INTERPRETA EL SISTEMA

    _inherit='account.invoice.line'

    _columns = {
        #LA DECLARACION DE UN NUEVO CAMPO, PERO ESTE ES UNA FUNCION A LA VEZ, ES DECIR QUE SE RECALCULA CADA VEZ
        #QUE EL SISTEMA SE RECARGA POR LO TANTO NO SE GUARDA EN LA BD A MENOS QUE USEMOS EL ATRIBUTO (store='True')
        'factura_sin_impuestos': fields.function(_factura_sin_impuestos, string='monto',
                                                  digits_compute=dp.get_precision('Account')),
    }

account_invoice()
