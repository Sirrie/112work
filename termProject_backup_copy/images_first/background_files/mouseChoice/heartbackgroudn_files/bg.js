// ¸¡´°Ô¤ÀÀ±³¾°
$(function(){
  $('.box_btn').click(function(){
        $.blockUI({ 
            message: $('#preview'), 
            css: { 
		        top:		'8%',
		        left:		'50%',
		        marginLeft:     '-45%', 
				border:		'6px solid #eee',
                width: '90%',
				height: '84%',
				cursor:		'pointer'

            } 
        }); 
		$('.blockOverlay,#preview').attr('title','µ¥»÷¹Ø±Õ').click($.unblockUI); 
	 });
});	 

function changeBG(pattern){document.getElementById('preview').style.background='url('+pattern+')';}