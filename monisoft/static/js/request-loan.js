function sendApprovedRequestLoan() {
  var form = $('#request-loan-form');
  var url = form.attr('action');
  var data = form.serialize();
  $.post(url, data, function(response) {
    switch (response.status) {
      case '200':
        debugger;
        var state = response.data.approved ? 'approved': 'NOT approved';
        toastr.info('Your loan request is: ' + state);
        break;
      case '500':
        toastr.info('Oops something went wrong');
        break;
      case 'form_error': // has custom error
        listErrors = response.form_error;
        for (var key in listErrors) {
          toastr.info(key + ': ' + listErrors[key]);
        }
        break;
    }
  });
}
