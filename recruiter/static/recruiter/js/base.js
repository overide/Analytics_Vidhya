/* contains little helper jQuery scripts for miscellaneous purpose and AJAX*/

// method to validate registration form
function validate_reg_form(form)
{
	valid = true;
	var errors=[];
	var pass1 = document.getElementById("id_password1_reg").value;
	var pass2 = document.getElementById("id_password2_reg").value;
	if(pass1 !== pass2)
	{
		errors.push("password do not match!");
		valid = false;
	}

	if(pass1.length < 8)
	{
		errors.push("password is too short!");
		valid = false;
	}

	if(!valid)
	{
		for(var i=0;i<errors.length;i++)
		{
			error_node = document.createElement('p');
			error_textnode = document.createTextNode(errors[i]);
			error_node.appendChild(error_textnode);
			document.getElementById('reg-form-errors').appendChild(error_node);
		}

		return false;
	}
	else
		document.getElementById('reg-form-errors').innerHTML("");

	return true;
}

//validate if password is not too short
$(document).ready(function(){
	$('#id_password1_reg').change(function(){
		var pass_len = $('#id_password1_reg').val().length;
		if(pass_len<8) 
			$('#id_password1_reg').siblings('.form-field-errors').text("password is too short!");
		else
			$('#id_password1_reg').siblings('.form-field-errors').text("");

	});
});

/*Script to show help text of fields */
$(document).ready(function() {
    $('.has-popover').popover({'trigger':'hover'});
});

/*Script to keep footer always at bottom*/
$(document).ready(function() {
 var docHeight = $(window).height();
 var footerHeight = $('#footer').height();
 var footerTop = $('#footer').position().top + footerHeight;

 if (footerTop < docHeight) {
  $('#footer').css('margin-top', 10+ (docHeight - footerTop) + 'px');
 }
});




//AJAX methods 

//Validating Registration Box username
$(document).ready(function(){
	$("#id_username_reg").change(function () {
	  var form = $(this).closest("form");	
	  var error_p = $(this).siblings('.form-field-errors');
	  $.ajax({
	    url: $(this).attr("data-validate-username-url"),
	    data: form.serialize(),
	    dataType: 'json',
	    success: function (data) {
	      if (data.is_taken) {
	      	error_p.text(data.error_message);}
	      else
	      	error_p.text("");
	    }
	  });

	});
});

// Validating Registration box email field
$(document).ready(function(){
	$("#id_email_reg").change(function () {
	  var form = $(this).closest("form");
	  var error_p = $(this).siblings('.form-field-errors');
	  $.ajax({
	    url: $(this).attr("data-validate-email-url"),
	    data: form.serialize(),
	    dataType: 'json',
	    success: function (data) {
	      if (data.email_exist) {
	        error_p.text(data.error_message);}
	      else
	      	error_p.text("");
	    }
	  });

	});
});

