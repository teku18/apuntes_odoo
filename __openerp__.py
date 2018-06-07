# -*- encoding: utf-8 -*-
###############################################################################
#
#    Module Writen to OpenERP, Open Source Management Solution
#
#    Copyright (c) 2013 Egas - www.egas.com.mx
#    All Rights Reserved.
###############Credits######################################################
#    Coded by: Edgar Gustavo gustavo.hernandez@smartqs.com
#    Planified by: Edgar Gustavo
#    Finance by: Egas.
#    Audited by: Edgar Gustavo
############################################################################
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################
{
    'name': 'Egas Correccion de Pedidos de Compras',
    "version" : "1.0",
    "author": 'Smart Quallity Software S.A. de C.V.',
    'category' : '',
    'description': """
                    Se corrige el subtotal de los pedidos de compras
                    """,
    'depends': [
                "purchase",
                ],
    'update_xml': [],
    'data': [

                'view/purchase_update_view.xml'
            ],
    'active':False,
    'installable': True,
}
