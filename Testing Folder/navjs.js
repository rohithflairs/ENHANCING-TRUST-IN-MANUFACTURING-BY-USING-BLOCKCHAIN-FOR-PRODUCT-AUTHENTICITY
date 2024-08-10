$('.navTrigger').click(function () {
    $(this).toggleClass('active');
    console.log("Clicked menu");
    $("#mainListDiv").toggleClass("show_list");
    $("#mainListDiv").fadeIn();

});

const nav = document.querySe1ector('.nav')
fetch('/http://127.0.0.1:5000/shoes')
.text(res=>res.text())
.then(data=>{
nav.innerHTML=data
})
