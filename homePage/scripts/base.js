
$(function(){
	//MY CODE FOR THE ASSIGNMENT//
	/*
	$('.list-inline li img').off().on('hover', function(event){
		console.log(this);
		var elem = $(this);
		console.log(elem);
		var pos = elem.offset()
		console.log(pos)
		var parent = $('.parentClass')
		$(parent).stop() //stops propogation
		$(parent).css({top: pos.top -25, left: pos.left - 25, 'z-index': 99, display:'block', position: 'absolute'}, 1000)		
		$(parent).toggle(2000);
	});
	*/
	
	
	//.$('item).stop().animate()
	//start a container for the area that your working in 
	var container = $('#license')
	var glyphs = container.find('.imageMaps td img')
	
	//this is how you add an element with all of the javascript
	$(document).on('hover' , '.add_glyph', function(){ //binds event to document, and works like an if
		console.log('hello')
		container.append(container_contents)
	})
	//This is a better way to do it.  Called name spaced events
	container.on('click' , '.add_glyph', function(){ //binds event to document, and works like an if
		container.append(container_contents)
	});
	//This is the best way to do it. If Ajax comes down, there will be 2 events coming down. 
	container.off('hover','.add_glyph').on('hover' , '.add_glyph', function(){ //always used namespaced events. 
		console.log('word')
		container.append(container_contents)
	});
	$('.AssyrianChar').hover(function(){
		console.log('Assyrian Hover');
	});
	//.trigger() //this will trigger your event. 
	
	//Check out custom jQuery events
	
	//Plugins a plugin is a self invoking function
	/*
	(function($){
		$.fn.yourname = function(options){
			
		}//this does it in our namespace
		$.yourname = function(options) {
			
		}//this appends to jQuery.  So it can work anywhere jQuery is called
		
		options = {
			//this dictionary becomes the default
		}, options);//if the user sends in multiple objects, they will overrride the default
	})(jQuery); //end plugin. Jquery is in the global namespace
	*/
	
	
	//START OF MY CODE//
	// $('.list-inline li img').off().on('hover', function(event){
	// 	console.log(this);
	// 	var elem = $(this);
	// 	console.log(elem);
	// 	var pos = elem.offset()
	// 	console.log(pos)
	// 	var parent = $('.parentClass')
	// 	$(parent).stop() //stops propogation
	// 	$(parent).css({top: pos.top -25, left: pos.left - 25, 'z-index': 99, display:'block', position: 'absolute'})
	// 	$(parent).toggle(1000);
	// });
	// $('#imageMaps').off('hover', '.imgHover').on('hover', function(){
	// 		$(this).stop().toggleClass('.imageMapsExpanded')
	// });
	
	// $('.draggable-char').off('hover', '.AssyrianElem').on('hover', function(){
// 	   $(this).stop().toggleClass('.imageMapsExpanded')
// 	    $('.Assyrian-char').animate({
// 		   opacity: 0.25,
// 		   left: "+=50",
// 		   height: "toggle"
// 		   }, 1000, function() {
// 		   // Animation complete.
// 	   });
// 	})
// /* ======= Scrollspy ======= */
    
// 	/* ======= ScrollTo ======= */
// 	 // there's the gallery and the trash
// 	 // let the gallery items be draggable
// 	 $( "li", ".draggable-char").draggable({
// 		 snap: ".CharTable"
// 	 });
// 	 // Droppable items
// 	 $("td", '.CharTable').droppable({
// 		 accept: ".draggable-char",
// 		 tolerance: "pointer",
// 		 drop: function( event, ui ) {
// 			$( this ).addClass( "red" )
// 		}
// 	 });
// 	 $('.check_answers').click( function(){
// 	 	//goes through and checks that the user's answers are correct. 

// 	 	$('.CharTable').each(function(){
// 	 		this_char = $(this)
// 	 		console.log(this_char.attr('id') + "A")
// 	 		that_char = $(this_char.attr('id') + "A")
// 	 		console.log('aaa')
// 	 		console.log(that_char.pos())
// 	 		console.log('bbb')
// 	 		if (this_char.hasClass('Assyrian-char')){
// 	 			console.log('yes')
// 	 		}
// 	 		console.log(this_char)
// 	 		$(this).css('background-color', 'blue')
// 	 	})
// 	 	Table = $('#Transliteration_Table')
// 	 	console.log(Table)
// 	 	console.log('a')
// 	 	table2 = $('table')
// 	 	console.log(table2)
// 	 	console.log('working')
// 	 });//end check_answers
// 	 // let the gallery be droppable as well, accepting items from the trash
// 	 // image deletion function
});






