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

import openerp.pooler as pooler

import time
import openerp
import openerp.modules.registry
from openerp.tools.translate import _
from openerp.tools import config
from openerp import SUPERUSER_ID
import web.http as openerpweb


#----------------------------------------------------------
# OpenERP Web helpers
#----------------------------------------------------------


class WklDataSet(openerpweb.Controller):
    _cp_path = "/web/workflow_info"

    @openerpweb.jsonrequest
    def info(self, req, model, id, signal,status,note):
        """
        self._db = False
        self._uid = False
        self._login = False
        self._password = False
        """
        result = False 
        object = pooler.get_pool(req.session._db).get(model)
        cr = pooler.get_db(req.session._db).cursor()
        uid = req.session._uid 
        if not object:
            raise except_osv('Object Error', 'Object %s doesn\'t exist' % str(model))
        try:
            cr.execute('select id from wkf_instance where res_id=%s and res_type=%s and state=%s', (id, model, 'active'))
            instance_id = cr.dictfetchone()['id']
            
            cr.execute("""
                select * from wkf_workitem where inst_id=%s""", (instance_id,))
            workitem = cr.dictfetchall()[0]
            
            result =  object._workflow_signal(cr, uid, [id], signal)[id]
            
            wkf_logs_obj = pooler.get_pool(req.session._db).get("workflow.logs")
            context={}
            vals={'res_type':model,
                    'res_id':id,
                    'time':time.strftime('%Y-%m-%d %H:%M:%S'),
                    'uid':uid,
                    'act_id':workitem['act_id'],
                    'status':status,
                    'info':note,
                  }
            wkf_logs_obj.create(cr,SUPERUSER_ID,vals,context=context)
            cr.commit()
        except Exception:
            cr.rollback()
            raise
        finally:
            cr.close()
        return result

# vim:expandtab:tabstop=4:softtabstop=4:shiftwidth=4:
