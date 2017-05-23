$(document).ready(function(){
    $("#toolbar").click(function(){
        var menu = $("#toolbar_menu")
        if (menu.css('visibility') == 'hidden') 
            menu.css('visibility', 'visible');
        else
            menu.css('visibility', 'hidden')
    });    

    $("#search_line").keyup(function(){
        console.log(this.value);
    });
});
