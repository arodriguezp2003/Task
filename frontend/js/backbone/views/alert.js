RS.Views.AlertView = Backbone.View.extend({
	events:{
		"click #mod" : "clickmod",
		"click #el" : "clickel"
	},
	className:"",
	tagName: "tr",

	initialize : function(model){
		var self = this;
		this.model = model;
		this.template = swig.compile($("#alerta_tpl").html());
	},
	render: function(data) {
		var self = this;
		var locals ={
			alert : this.model.toJSON()
		};
		this.$el.html( this.template(locals) );

		return this;
	},
	remove: function() {
		$(this.el).find('.event').remove();
	},
	clickmod: function(){
		alert("modifica");
	},	
	clickel: function(){
		alert("elimina");
	},		
});
