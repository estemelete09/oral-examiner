//jQuery used to stop the page from loading when running python functions
jQuery(document).on('click', '#playquestion', function(e){
    e.preventDefault();
    console.log("page will not refresh!") // sanity check
    create_audio();
});

jQuery(document).on('click', '#answerbutton', function(e){
    e.preventDefault();
    console.log("page will not refresh!")  // sanity check
    create_text();
});

jQuery(document).on('click', '#checkbutton', function(e){
    e.preventDefault();
    console.log("page will not refresh!")  // sanity check
    check_answer();
});

function create_text() {    
    console.log("create text is working!"); // sanity check
    console.log(jQuery('#answerfield').text());

    jQuery.ajax({
        url: 'speech_to_text', 
        dataType: 'json',
        data: {
            testing: jQuery("#answerfield").text()
        },
        success: function(json) {          
            console.log(json);
            jQuery("#answerfield").text(json.audiodata);
        }
    });
};

function create_audio() {    
    console.log("create audio is working!"); // sanity check
    var questionfield = jQuery("#questionfield").val();
    jQuery.ajax({
        url: 'text_to_speech',
        dataType: 'json',
        data: {
            'getdata': questionfield
        },
        success: function(json) {           
            console.log(json);
            jQuery("#questionfield").val(json.getdata);

        }
    });
};

function check_answer() {    
    console.log("checking answer is working!"); // sanity check
    var questionfield = jQuery("#questionfield").val();
    var answerfield = jQuery("#answerfield").text();
    jQuery.ajax({
        url: 'check_answer',
        dataType: 'json',
        data: {
            'questiondata': questionfield,
            'answerdata': answerfield

        },
        success: function(json) {           
            console.log(json);
            jQuery("#result").text(json.result_text);

        }
    });
};
