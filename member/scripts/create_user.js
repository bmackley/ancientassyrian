
$(function(){
	$('#id_dateOfBirth').off('click').on('click', function(){
		console.log('ready');
		$('#id_dateOfBirth').datepicker({
		    format: 'mm/dd/yyyy',
		    changeMonth: true,
   			changeYear: true,
   			yearRange: "1940:2012",
   			defaultDate: "-18y",
		});	
	});
});