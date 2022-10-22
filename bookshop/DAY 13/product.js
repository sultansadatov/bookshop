function like(){
    var lik = document.querySelector('.like');
    lik.classList.toggle('blue');
    lik.classList.toggle('revers');
};
function give_heart(){
    var heart = document.querySelector('.heart');
    heart.classList.toggle('red');
    if(heart.classList.contains('red')){
        alert("Kitabı bəyəndiniz!")
    }
    else{
        alert("Bəyənməkdən imtina etdiniz!");
    }
    
};
var incog = 12;
var fstPrice = 16;
var sefiller = 21;
var totalPrice = fstPrice + sefiller;
var new_book = document.createElement('li');
new_book.classList.add('newBook');
new_book.classList.add('dropdown-item');
new_book.innerHTML = '<i class="x fas fa-times"></i> Inkognito <span>12AZN</span>';
var warning = document.querySelector('.xeberdar');
var click = document.querySelector('.gray');
function addToCard(){
    click.classList.toggle('click');
    var menu = document.querySelector('.menu');
    // if(new_book.classList.contains('newBook') == true);{
    //     console.log('Elave edildi');
    //     click.style.backgroundColor = 'gray';
    //     click.innerText = "Səbətdən çıxart";
    //     // var new_item = document.querySelector('.newBook');
    //     new_book.innerHTML = "Inkognito" + "<span>12AZN</span>";
    //     new_book.classList.remove('newBook');
    //     menu.prepend(new_book);
    //     document.querySelector('.total').innerHTML = "Cəmi" + "<span>49AZN</span>";
    // }
    if(new_book.classList.contains('newBook')){
        totalPrice += incog;
        console.log(incog);
        console.log(totalPrice);
        console.log('Elave edildi');
        new_book.classList.remove('newBook');
        // // // new_book.classList.toggle('newBook');
        new_book.classList.add('inCognito');
        // dropdownList.document.querySelectorAll("#menu > li > i");
        click.style.backgroundColor = 'gray';
        click.innerText = "Səbətdən çıxart";
        document.querySelector(".modal-body").innerText = "Məhsul səbətə əlavə edildi";
        // var new_item = document.querySelector('.newBook');
        new_book.classList.toggle('dropdown-item');        
        menu.prepend(new_book);
        var opac = document.querySelector('.opac');
        opac.classList.toggle('opacity');
        document.querySelector('.total').innerHTML = `Cəmi  <span>${totalPrice}AZN</span>`;
        warning.classList.remove('alert-warning');
        warning.classList.add('alert-danger');
        warning.innerText = "Bu kitabdan sadəcə 1 ədəd qalıb";
        

    }
    else{
        totalPrice -= incog;
        console.log(totalPrice);
        new_book.classList.remove('inCognito');
        new_book.classList.add('delete');
        new_book.classList.remove('dropdown-item');
        new_book.classList.add('newBook');
        console.log("Cixarildi");
        // new_book.classList.add('newBook');
        click.style.backgroundColor = '#109E97';
        click.innerText = "Səbətə əlavə et";
        document.querySelector(".modal-body").innerText = "Məhsul səbətdən çıxarıldı";
        var elements = menu.getElementsByTagName('li');
        menu.removeChild(elements[0]);
        document.querySelector('.total').innerHTML = `Cəmi <span>${totalPrice}AZN</span>`;
        warning.classList.remove('alert-danger');
        warning.classList.add('alert-warning');
        warning.innerText = "Bu kitabdan sadəcə 2 ədəd qalıb";
    };
};

// var ul = document.querySelector("#menu");
// var firstbook = document.querySelector(".firsbook");
// var sefilBook = document.querySelector(".sefiller");
// var inCognito = document.querySelector(".inCognito");


let xMarkNew = new_book.children.item(0);
xMarkNew.addEventListener("click", function(){
    this.parentElement.classList.add('delete');
    this.parentElement.classList.remove('dropdown-item');
    this.parentElement.classList.add('newBook');
    click.style.backgroundColor = '#109E97';
        click.innerText = "Səbətə əlavə et";
        totalPrice -= incog;
        document.querySelector('.total').innerHTML = `Cəmi  <span>${totalPrice}AZN</span>`
        warning.classList.remove('alert-danger');
        warning.classList.add('alert-warning');
        warning.innerText = "Bu kitabdan sadəcə 2 ədəd qalıb";
});

let dropdownList = document.querySelectorAll("#menu > li > i");
console.log(dropdownList);
dropdownList.forEach(item => {
    item.addEventListener("click", function(event){
        this.parentElement.classList.add('delete');
        this.parentElement.classList.remove('dropdown-item');
        if (this.parentElement.classList.contains('firstbook')){
            totalPrice -= fstPrice;
            console.log(totalPrice);
            document.querySelector('.total').innerHTML = `Cəmi  <span>${totalPrice}AZN</span>`
        }
        else if(this.parentElement.classList.contains('sefiller')){
            totalPrice -= sefiller;
            console.log(totalPrice);
            document.querySelector('.total').innerHTML = `Cəmi  <span>${totalPrice}AZN</span>`
        }
        else if(this.parentElement.classList.contains('inCognito')){
        totalPrice -= 12;
        console.log(totalPrice);
        document.querySelector('.total').innerHTML = `Cəmi  <span>${totalPrice}AZN</span>`
    }
}
    )
console.log(totalPrice);   
});

// function deleted(){

//     document.querySelector('.dropdown-item').style.display = 'none';
//     document.querySelector('.dropdown-item').classList.remove('dropdown-item');
// }

// var xMark = document.querySelector('.x');
// xMark.addEventListener('click', function(){
//     document.querySelector('.dropdown-item').style.display = 'none';
//     document.querySelector('.dropdown-item').classList.remove('dropdown-item');
// });
