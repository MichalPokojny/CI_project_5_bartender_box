// Display banner messages with a fade effect and rotate through a list of messages
$(document).ready(function() {
    // Array of banner messages to display
    var messages = ['Free delivery on orders over €60 !', 'Special offer: Free gift with every purchase!']; 
    var index = 0;

    // Display the first banner message immediately
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

    // Sorting script for products.html for sorting products in asc or desc order
    
    $('#sort-selector').change(function() {
        var selector = $(this);
        var currentUrl = new URL(window.location);
    
        var selectedVal = selector.val();
        var [sort, direction] = selectedVal.split("_");
    
        currentUrl.searchParams.set("sort", sort);
        currentUrl.searchParams.set("direction", direction);
    
        if(selectedVal === "reset"){
            currentUrl.searchParams.delete("sort");
            currentUrl.searchParams.delete("direction");
        }
    
        window.location.replace(currentUrl);
    });

});
