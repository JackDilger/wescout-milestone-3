document.addEventListener("DOMContentLoaded", function() {
    //Initialize sidenav- required javascript from materialize
    let sidenav = document.querySelectorAll(".sidenav");
    M.Sidenav.init(sidenav);

    // collapsible initializataion-required javascript from materialize
    let collapsibles = document.querySelectorAll(".collapsible");
    M.Collapsible.init(collapsibles);

    // select initialization-required javascript from materialize
    let selects = document.querySelectorAll("select");
    M.FormSelect.init(selects);

    // modal inititalization-required javascript from materialize
    let modal = document.querySelectorAll('.modal');
    M.Modal.init(modal);
});