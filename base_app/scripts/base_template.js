

$(function(){
	$('#login_button').off('click.login').on('click.login', function(){
		$('body').loadmodal({
			id: 'login_modal',
			title: 'Login',
			url: '/member/login/',
		});
	});
});



