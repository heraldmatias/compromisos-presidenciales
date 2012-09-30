function andina_news(){        
        var noticias = $("#noticias");
	$.getJSON('/andina/noticias/json/', function(data){
                $.each(data, function(key,value){                
			noticias.append(key +" = " + value["titular"]);
		});
		
	});
}
/*
$.each(data, function(key,value){                
			noticias.append(key);
		});*/
$(document).ready(function() {
andina_news();
});
