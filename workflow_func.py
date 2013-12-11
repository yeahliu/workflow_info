# -*- coding: utf-8 -*-
##############################################################################
#
#    yeahliu
#    Copyright (C) yeahliu (<talent_qiao@163.com>).
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

from openerp.osv import fields, osv
from openerp.tools.translate import _
from openerp import netsvc
from openerp.osv.orm import BaseModel

def _get_workflow_logs(self, cr, uid, ids, field_name, args, context=None):
        model = self._name
        if not model:
            return {}
        model_obj = self.pool.get(model)
        wkl_logs_obj = self.pool.get("workflow.logs")
        res = {}
        for ms in model_obj.browse(cr,uid,ids,context=context) :
            res[ms.id]= wkl_logs_obj.search(cr,uid,[('res_id','=',ms.id),('res_type','=',model)])
        return res ;


# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:

