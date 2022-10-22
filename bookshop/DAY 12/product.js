function like(){
    var lik = document.querySelector('.like');
    lik.classList.toggle('blue');
    lik.classList.toggle('revers');
}
function give_heart(){
    var heart = document.querySelector('.heart');
    heart.classList.toggle('red');
    if(heart.classList.contains('red')){
        alert("Kitabı bəyəndiniz!")
    }
    else{
        alert("Bəyənməkdən imtina etdiniz!");
    }
    
}
var new_book = document.createElement('li');
new_book.classList.add('newBook');
new_book.classList.add('dropdown-item');
var warning = document.querySelector('.xeberdar');
function addToCard(){
    var click = document.querySelector('.gray');
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
        new_book.classList.remove('newBook');
        console.log('Elave edildi');
        click.style.backgroundColor = 'gray';
        click.innerText = "Səbətdən çıxart";
        // var new_item = document.querySelector('.newBook');
        new_book.innerHTML = '<i class="x fas fa-times"></i> Inkognito <span>12AZN</span>';
        menu.prepend(new_book);
        var opac = document.getElementsByClassName('opac');
        opac.classList.toggle('opacity');
        document.querySelector('.total').innerHTML = "Cəmi" + "<span>49AZN</span>";
        warning.classList.remove('alert-warning');
        warning.classList.add('alert-danger');
        warning.innerText = "Bu kitabdan sadəcə 1 ədəd qalıb";
    }
    else{
        new_book.classList.add('newBook');
        click.style.backgroundColor = '#109E97';
        click.innerText = "Səbətə əlavə et";
        document.querySelector(".modal-body").innerText = "Məhsul səbətdən çıxarıldı";
        var elements = menu.getElementsByTagName('li');
        menu.removeChild(elements[0]);
        document.querySelector('.total').innerHTML = "Cəmi" + "<span>37AZN</span>";
        warning.classList.remove('alert-danger');
        warning.classList.add('alert-warning');
        warning.innerText = "Bu kitabdan sadəcə 2 ədəd qalıb";
}


    // if(new_book.classList.contains('newBook') != true){
    //     click.style.backgroundColor = '#109E97';
    //     click.innerText = "Səbətə əlavə et";
    //     new_book.classList.add('newBook');
    //     document.querySelector(".modal-body").innerText = 'Məhsul səbətdən çıxarıldı';
    //     new_book.innerHTML = '';
    // }
    
}
