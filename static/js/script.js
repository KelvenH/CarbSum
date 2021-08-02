$(document).ready(function () {
  $('.sidenav').sidenav({edge: "right"});
  $(".dropdown-trigger").dropdown();
  $('.collapsible').collapsible();

  //toggle show/hide password (Acknowledgement Stack Overflow: https://stackoverflow.com/questions/51552661/how-to-show-and-hide-password-when-click-on-eye-icon-using-jquery)
  $(document).on('click', '.toggle-password', function () {
    $(this).toggleClass("fa-eye fa-eye-slash");
    var input = $("#password");
    input.attr('type') === 'password' ? input.attr('type', 'text') : input.attr('type', 'password')
  });
});










 