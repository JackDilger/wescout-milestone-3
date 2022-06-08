document.addEventListener("DOMContentLoaded", function() {
    //Initialize sidenav
    let sidenav = document.querySelectorAll(".sidenav");
    M.Sidenav.init(sidenav);
}); 

document.addEventListener('DOMContentLoaded', function() {
    var elems = document.querySelectorAll('.collapsible');
    var instances = M.Collapsible.init(elems, options);
  });