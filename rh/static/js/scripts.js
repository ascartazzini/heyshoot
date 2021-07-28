$(document).ready(function(){
    // Requires jQuery

$(document).on('click','.js-menu_toggle.closed',function(e){
	e.preventDefault(); $('.list_load, .list_item').stop();
	$(this).removeClass('closed').addClass('opened');

	$('.side_menu').css({ 'left':'0px' });

	var count = $('.list_item').length;
	$('.list_load').slideDown( (count*.6)*100 );
	$('.list_item').each(function(i){
		var thisLI = $(this);
		timeOut = 100*i;
		setTimeout(function(){
			thisLI.css({
				'opacity':'1',
				'margin-left':'0'
			});
		},100*i);
	});
});

$(document).on('click','.js-menu_toggle.opened',function(e){
	e.preventDefault(); $('.list_load, .list_item').stop();
	$(this).removeClass('opened').addClass('closed');

	$('.side_menu').css({ 'left':'-250px' });

	var count = $('.list_item').length;
	$('.list_item').css({
		'opacity':'0',
		'margin-left':'-20px'
	});
	$('.list_load').slideUp(300);
});    
});


//AQUI O FILTRO DA TABELA DE CONTAS
$(document).ready(function() {
	$(".search").keyup(function () {
	  var searchTerm = $(".search").val();
	  var listItem = $('.results tbody').children('tr');
	  var searchSplit = searchTerm.replace(/ /g, "'):containsi('")
	  
	$.extend($.expr[':'], {'containsi': function(elem, i, match, array){
		  return (elem.textContent || elem.innerText || '').toLowerCase().indexOf((match[3] || "").toLowerCase()) >= 0;
	  }
	});
	  
	$(".results tbody tr").not(":containsi('" + searchSplit + "')").each(function(e){
	  $(this).attr('visible','false');
	});
  
	$(".results tbody tr:containsi('" + searchSplit + "')").each(function(e){
	  $(this).attr('visible','true');
	});
  
	var jobCount = $('.results tbody tr[visible="true"]').length;
	  $('.counter').text(jobCount + ' item');
  
	if(jobCount == '0') {$('.no-result').show();}
	  else {$('.no-result').hide();}
			});
  });


//AQUI O FILTRO DA TABELA DE PROJETOS
$(document).ready(function() {
	$(".search").keyup(function () {
	  var searchTerm = $(".search").val();
	  var listItem = $('.resultados tbody').children('tr');
	  var searchSplit = searchTerm.replace(/ /g, "'):containsi('")
	  
	$.extend($.expr[':'], {'containsi': function(elem, i, match, array){
		  return (elem.textContent || elem.innerText || '').toLowerCase().indexOf((match[3] || "").toLowerCase()) >= 0;
	  }
	});
	  
	$(".resultados tbody tr").not(":containsi('" + searchSplit + "')").each(function(e){
	  $(this).attr('visible','false');
	});
  
	$(".resultados tbody tr:containsi('" + searchSplit + "')").each(function(e){
	  $(this).attr('visible','true');
	});
  
	var jobCount = $('.resultados tbody tr[visible="true"]').length;
	  $('.contador').text(jobCount + ' item');
  
	if(jobCount == '0') {$('.no-resultados').show();}
	  else {$('.no-resultados').hide();}
			});
  });