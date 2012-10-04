function andina_news(){        
        var noticias = $("#noticias");
	$.getJSON('http://50.116.43.119:8070/andina/noticias/json/?callback=?', function(data){
                $.each(data, function(key,value){                
			noticias.append(key +" = " + value["titular"]);
		});
		
	});
}
function andina_news2(){
$.ajax({
  dataType: 'json',
  data: 'id=10',
  jsonp: 'jsonp_callback',
  url: 'http://50.116.43.119:8070/andina/noticias/json/',
  success: function () {
    alert("exito");
  },
}).done(function() { alert("success"); })
    .fail(function(jqXHR, textStatus) { alert("error"+textStatus); })
    .always(function() { alert("complete"); });

}

/*
$.each(data, function(key,value){                
			noticias.append(key);
		});*/
$(document).ready(function() {
andina_news2();
});
