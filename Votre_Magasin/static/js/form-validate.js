function valid_datas( f ){
	
	if( f.name.value == '' ){
		jQuery('#form_status').html('<span class="wrong">Enter Your Name!</span>');
		notice( f.name );
	}else if( f.email.value == '' ){
		jQuery('#form_status').html('<span class="wrong">Enter Your Email in correct format!</span>');
		notice( f.email );
        }else if( f.vehicleno.value == '' ){
		jQuery('#form_status').html('<span class="wrong">Enter Your Vehicle No !</span>');
		notice( f.vehicleno );
	}else if( f.phone.value == '' ){
		jQuery('#form_status').html('<span class="wrong">Enter Your Phone no in correct format!</span>');
		notice( f.phone );
	}else if( f.address.value == '' ){
		jQuery('#form_status').html('<span class="wrong">Enter Your Address!</span>');
		notice( f.address );
        }else if( f.latitude.value == '' ){
		jQuery('#form_status').html('<span class="wrong">Enter Your Latitude!</span>');
		notice( f.latitude );
        }else if( f.longitude.value == '' ){
		jQuery('#form_status').html('<span class="wrong"> Enter Your Longitude !</span>');
		notice( f.longitude );
        }else if( f.username.value == '' ){
		jQuery('#form_status').html('<span class="wrong">Enter Your Username !</span>');
		notice( f.username );
        }else if( f.password.value == '' ){
		jQuery('#form_status').html('<span class="wrong"> Enter Your Password !</span>');
		notice( f.password );
         }else if( f.confirm_password.value ==''){
		jQuery('#form_status').html('<span class="wrong">Enter Confirm Password !</span>');
		notice( f.confirm_password );
         }else if( f.confirm_password.value != f.password.value ){
		jQuery('#form_status').html('<span class="wrong">Passwords doesnt Match!</span>');
		notice( f.confirm_password );
	}else if( f.subcategory.value == '' ){
		jQuery('#form_status').html('<span class="wrong">Enter Subcategory!</span>');
		notice( f.subcategory );
	}else if( f.category.value == '' ){
		jQuery('#form_status').html('<span class="wrong">Enter Category !</span>');
		notice( f.category );
	}else{
		 jQuery.ajax({
			url: 'mail.php',
			method: 'POST',
			data: jQuery('form#Reg_cust').serialize(),
			complete: function(data) {
				jQuery('#form_status').html(data.responseText);
				jQuery('#Reg_cust').find('input,textarea').attr({value:''});
				jQuery('#Reg_cust').css({opacity:1});
				jQuery('#Reg_cust').remove();
			}
		});
		jQuery('#form_status').html('<span class="loading">Sending your message...</span>');
		jQuery('#Reg_cust').animate({opacity:0.3});
		jQuery('#Reg_cust').find('input,textarea,button').css('border','none').attr({'disabled':''});
	}
	
	return false;
}

function notice( f ){
	jQuery('#Reg_cust').find('input,textarea').css('border','none');
	f.style.border = '1px solid red';
	f.focus();
}