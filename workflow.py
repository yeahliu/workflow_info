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



class wkf_logs(osv.osv):
    _name = "workflow.logs"
    _table = "wkf_logs"
    _order = "id desc"
    _columns = {
        'res_type': fields.char('资源类型', size=256, required=True),
        'res_id': fields.integer('资源ID',  required=True),
        'uid': fields.many2one('res.users', '用户',required=True),
        'act_id': fields.many2one('workflow.activity', '工作流阶段'),
        'time': fields.datetime('处理时间'),
        'info': fields.text('记录'),
        'status':fields.selection([('ok','通过'),('no','拒绝'),('submit','提交')],'状态'),        
    }

wkf_logs()

        
# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:

