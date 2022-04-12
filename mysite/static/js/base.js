const col_change = document.getElementById('col_change');
const windowSm = 600;

let windowWidth = $(window).width();
if (windowWidth <= windowSm) {
  col_change.classList.add('col-12');
}else {
  col_change.classList.add('col-10');
}


window.addEventListener('DOMContentLoaded', function(){
  window.addEventListener('resize', function(){
    let windowWidth = $(window).width();
    if (windowWidth <= windowSm) {
      col_change.classList.remove('col-10');
      col_change.classList.add('col-12');
    }else {
      col_change.classList.remove('col-12');
      col_change.classList.add('col-10');
    }
  });
});