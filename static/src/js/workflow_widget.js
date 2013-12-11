/*---------------------------------------------------------
 * workflow 增强
 * Copyright 2013 yeahliu <talent_qiao@163.com>
 *---------------------------------------------------------*/
openerp.workflow_info = function(instance) {
    var _t = instance.web._t,
        _lt = instance.web._lt;
    var QWeb = instance.web.qweb;

    instance.web.View.include({        
        do_execute_action: function (action_data, dataset, record_id, on_closed) {
	    	//alert("action_data :"+action_data + "  dataset:"+dataset+ "  record_id: "+record_id+"  on_closed: "+on_closed )
	    	var self = this;
	    	if(action_data.type == "workflow_ok" || action_data.type == "workflow_no"){
	    		ok = true;
	    		if( action_data.type == "workflow_no") ok = false ;
	    		
	    		_title = ok? "输入审批意见(可不填)：" :"输入拒绝意见："
	    		var dialog = new instance.web.Dialog(this,{
	    			title: _title,
	    			dialogClass: 'oe_act_window',
	    			width:500
	    		},	QWeb.render("textbox_pft_wkl"));
	    		buttons=[
					                {text: _t("提交"), click: function() { 
						                	return instance.session.rpc('/web/workflow_info/info', {
										            model: dataset.model,
										            id: record_id, // wkf_instance id
										            signal: action_data.name,
										            note:dialog.$el.find(".oe_textbox_pft_wkl").val(),
										            status: ok?'ok':'no'
										        }).then(function(){
										        	dialog.destroy();									        
										        }).then(function () {
										        	self.reload();
									            });
					                	}
					                }
					            ];
					            
	    		dialog._add_buttons(buttons);
	    		dialog.open();
	    	} else if (action_data.type == "workflow_submit"){
	    		return instance.session.rpc('/web/workflow_info/info', {
										            model: dataset.model,
										            id: record_id, // wkf_instance id
										            signal: action_data.name,
										            note:'提交',
										            status: 'submit'
										        }).then(function () {
										        	self.reload();
									            });
	    	} else {
	    		return this._super(action_data, dataset, record_id, on_closed) ;
    	}
    },
    });
    
};

// vim:et fdc=0 fdl=0 foldnestmax=3 fdm=syntax:
