
$(document).ready(function(){
    console.log("Hello World")
    $('#submit').click(function(){
        console.log($("#queryForm").serialize());
    });
});



/*
$.ajax('/api/parameters', {
    type: 'POST',  // http method
    data: { myData: 'This is my data.' },  // data to submit
    success: function (data, status, xhr) {
        $('p').append('status: ' + status + ', data: ' + data);
    },
    error: function (jqXhr, textStatus, errorMessage) {
            $('p').append('Error' + errorMessage);
    }
});
*/