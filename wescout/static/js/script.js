document.addEventListener("DOMContentLoaded", function() {
    //Initialize sidenav
    let sidenav = document.querySelectorAll(".sidenav");
    M.Sidenav.init(sidenav);

    // collapsible initializataion
    let collapsibles = document.querySelectorAll(".collapsible");
    M.Collapsible.init(collapsibles);

    // select initialization
    let selects = document.querySelectorAll("select");
    M.FormSelect.init(selects);

    // modal inititalization
    let modal = document.querySelectorAll('.modal');
    M.Modal.init(modal);
});



