workflow_info
====
openerp工作流增强，在审批或拒绝过程中，可以输入审批信息，同时记录审批记录
欢迎提出修改意见，http://blog.csdn.net/yeahliu/article/details/17207289
或发送至<talent_qiao@163.com>

功能 ：
1. 对于审批和拒绝，弹出输入信息的窗口，可以对此次审批作说明
2. 审批记录记录在表wkf_logs中，这个表原本在openerp中就已经有，只是没有启用
3. 与原工作流按钮不冲突，可以一起使用

使用说明 ：
1. 安装workflow_info模块
2. 将需要弹出信息窗口用于输入审批信息的按钮的type设置成"workflow_ok"或"workflow_no"
3. 如果需要在页面上输入审批记录，按以下步骤操作：
	a. 在.py文件中引入“from openerp.addons.workflow_info import workflow_func”
    b. 在_columns里加入字段，如
    	'wkf_logs':fields.function(workflow_func._get_workflow_logs, string='审批记录', type='one2many', relation="workflow.logs",readonly=True),
    c. 在view文件里可以这样引用：
    	<field name="wkf_logs">
			<tree string="审批记录" colors="red:(status=='no')">
				<field name="job_id" />
				<field name="employee_id" />
				<field name="time" />
				<field name="status" />
				<field name="info" />
			</tree>
		</field>
    d. 对于按钮，可以这样设置：
    	<button name="to_sale" string="提交" type="workflow_submit" states="draft" class="oe_highlight" />
        	workflow_submit表示这是提交按钮，不需要弹出输入窗口
        <button name="to_delivery" string="销售审批" type="workflow_ok" states="wf_sale" class="oe_highlight"/>
        	workflow_ok 表示这是审批按钮，弹出输入审批信息窗口
        <button name="refuse"  string="拒绝" type="workflow_no"  class="oe_highlight"/>
        	workflow_no 表示这是拒绝按钮，弹出输入拒绝信息窗口