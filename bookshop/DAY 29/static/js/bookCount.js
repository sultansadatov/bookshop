// $(".decrease").on("click", function(){
//     var currentVal = $("#book_count");
//     takenVal = currentVal.val();
//     console.log(takenVal);
//     if (!isNaN(takenVal)) {
//         currentVal.val(takenVal - 1);
//     }
//     if(takenVal < 1){
//         alert("Yalnış dəyər daxil etdiniz !")
//         currentVal.val(takenVal) = 0;
//         console.log(takenVal);
//     }

//     $(".books_imgs").children().last().remove();
// });
// var arr = [];
// $(".increase").on("click", function(){
//     var currentVal = $("#book_count");
//     takenVal = parseInt( currentVal.val());
//     // console.log(takenVal);
//     if (!isNaN(takenVal)) {
//         currentVal.val(takenVal + 1);
//     }
//     if(takenVal > 8){
//         alert("Yalnış dəyər daxil etdiniz !")
//         currentVal.val(takenVal) = 9;
//         // console.log(takenVal);
//     }
    
//     var is = true;
//     while(is){
//         var rand = Math.floor(Math.random() * books.length);
//         console.log(rand);
//         if(!arr.includes(rand)){
//             console.log(arr.includes(rand));
//             console.log(arr);
//             is = false;
//             arr.push(rand);
//             console.log("Work");
//             $(".books_imgs").append(
            // `<div class="grid-item ${books[rand].class} image col-4 pb-5">
            //     <div class="card" >
            //         <img src="${books[rand].img}" class="card-img-top" alt="...">
            //         <div class="card-body">
            //             <h5 class="card-title">${books[rand].name}</h5>
            //             <p class="card-text">${books[rand].writer}</p>
            //             <a class="btn btn-primary" href="product.html" role="button">Ətraflı</a>
            //     </div>
            // </div>`
//             )
//         }
//         if(arr.length % 3 === 0){
//             arr = [];
//         }
//     }
// });

// let books = [
//     {
//         writer: "David Eagleman",
//         img: "images/Inkognito.png",
//         price: "12.00",
//         name: "Inkognito",
//         class: "psixologiya"
//     },
//     {
//         writer: "Viktor Hugo",
//         img: "images/Sefiller.jpg",
//         price: "21.00",
//         name: "Səfillər",
//         class: "roman"
//     },
//     {
//         writer: "George Orwell",
//         img: "images/1984.jpg",
//         price: "16.00",
//         name: "1984",
//         class: "bilim-kurgu"
//     }
// ]

t1 = "Başla";
t2 = "Bitir";

$(".btn-start").on("click", function(){
    $(this).toggleClass("btn-danger");
    if($(this).hasClass("btn-danger")){
        this.innerText = "Bitir";
        $(".page-count-block").css("display", "block");
    }
    else{
        this.innerText = "Başla";
        $(".page-count-block").css("display", "none");
        $(".alert-success").css("display", "none");
        $(".alert-danger").css("display", "none");
    }

});

$(".counter-btn").on("click", function(){
    var page = $("#page").val();
    var day = $("#day").val();
    var result = Math.ceil(page/day);
    if(day <= 0 || page < 0 || isNaN(page) || isNaN(day) || isNaN(result)){
        $(".alert-danger").css("display", "block");
        $(".alert-danger").html(`<b>Hesablamada xəta baş verdi!</b>`)
    }else{
        $(".alert-success").css("display", "block");
        // text("Hər gün ən az " + result + " səhifə oxumalısınız")
        $(".alert-success").html(`Hər gün ən az <b>${result}</b> səhifə oxumalısınız!`)
    }
});

// $(".grid-item").isotope({
//     itemSelector: '.grid-item',
//     layoutMode: 'fitRows'
// });
// $(".filter button").on("click", function(){
//     var value = $(this).attr("data-name");
//     console.log(value);
//     $(".grid").isotope({
//     filter: value
// });            
// });