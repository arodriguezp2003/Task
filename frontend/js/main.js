$(document).ready(function(){
	//$("#login").hide();
	console.log("Init TaskManager by RS");
	
	window.util.be ="http://192.168.1.70:3000/";

	window.collections.alerts = new RS.Collections.AlertsCollection();
	window.collections.alerts.on("add",function(model){
		var view = new RS.Views.AlertView(model);
		view.render();
		$('#Atbody').append(view.el);
	});






	$('#Uenviar').click(function(e){
		e.preventDefault();
		
		var login = $("#login");
		var error = $("#Uinv");
		var user =$("#user").val();
		var password=$("#pass").val();

		var url = window.util.be + "auth/" + user + "/" + password + "/";
		var l = Ladda.create(this);
		l.start();

		if (user==="" || password==="") 
		{
			$("#Udatos").show("slow");
			l.stop();
			setInterval(function(event){
				$("#Udatos").hide("slow");
			},2000);
			return;
		}
		$.get( url, function( data ) {
			if(data=="SI")
			{
				window.util.__prop = {'a': user , 'b' : password};
				

				$.ajax
				({
					type: "GET",
					url: window.util.be + "api/alerts/?format=json",
					dataType: 'json',
					async: false,
					data: '{}',
					beforeSend: function (xhr){ 
						xhr.setRequestHeader('Authorization', window.util.BasicAuth(user, password)); 
					},
					success: function (data){
						$.get( "html/alerta.html", function(datas) {
							login.hide("slow");
							$("#container_tab").hide();
							$("#container_tab").html(datas);		
							$("#container_tab").show("slow");
							data.forEach(function(d){

								window.collections.alerts.add(d);
								

							});					
						});
					}
				});
			}
			else 
			{
				login.show("slow");
				window.util.auth  = {};
				error.show("slow");
				$("#pass").val("");
				$("#user").focus();
				setInterval(function(event){
					error.hide("slow");

				},2000);
			}
			l.stop();
		});

		return false;
	});

window.util.BasicAuth = function (user, password) {
	var tok = user + ':' + password;
	var hash = btoa(tok);
	return "Basic " + hash;
}

});