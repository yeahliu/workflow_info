# -*- coding: utf-8 -*-
##############################################################################
#
#    yeahliu
#    Copyright 2013 yeahliu <talent_qiao@163.com>
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
    'name': 'workflow_info',
    'version': '0.1',
    'category': 'Tools',
    'description': """
如有问题，请发邮件给我<talent_qiao@163.com>

""",
    'author': 'yeahliu',
    'website': '',
    'depends': ['web'],
    'js': [
        'static/src/js/*.js'
    ],
    'css': [
    ],
    'qweb' : [
        'static/src/xml/*.xml',
    ],
    'data' : [
        'security/ir.model.access.csv',      
              ],
    'installable': True,
    'images': [],
}

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
