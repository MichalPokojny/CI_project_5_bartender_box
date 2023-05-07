// Display banner messages with a fade effect and rotate through a list of messages
$(document).ready(function() {
    // Array of banner messages to display
    var messages = ['Free delivery on orders over €60 !', 'Special offer: Free gift with every purchase!']; 
    var index = 0;

    $('.banner-text').text(messages[index]);

    // Set a timer to display the banner messages every 5s
    setInterval(function() {
        $('.banner-text').fadeOut(function() {
            $(this).text(messages[index]);
        }).fadeIn();

        index++;

        if (index === messages.length) {
            index = 0;
        }
    }, 5000);
});

