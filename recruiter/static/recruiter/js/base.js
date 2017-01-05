/* contains little helper jQuery scripts for miscellaneous purpose */

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