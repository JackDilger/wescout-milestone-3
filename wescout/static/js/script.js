document.addEventListener("DOMContentLoaded", function() {
    //Initialize sidenav
    let sidenav = document.querySelectorAll(".sidenav");
    M.Sidenav.init(sidenav);

    // collapsible initializataion
    let collapsibles = document.querySelectorAll(".collapsible");
    M.Collapsible.init(collapsibles);

}); 

