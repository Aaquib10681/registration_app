$(document).ready(function () {
  var today_date_obj = moment();

  $("#date_of_birth").change(function () {
    var input_date_string = $(this).val();
    var input_date_obj = moment(input_date_string);
    var duration = moment.duration(today_date_obj.diff(input_date_obj));
    var years = duration.years();
    var months = duration.months();
    var days = duration.days();
    var final_diff = `${years}Y-${months}M-${days}D`;

    // now i need ot add this final diff in age input field automatically
    $("#age_field").val(final_diff);
  });
});
