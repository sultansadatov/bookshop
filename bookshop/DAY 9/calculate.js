var page = parseInt(prompt("Kitabın səhifə sayı ? "));
var days = parseInt(prompt("Neçə günə bitirməlisiniz ? "));
var result = Math.ceil(page/days);
if(isNaN(page) || isNaN(days) || days === 0){
    alert("Hesablamada səhv baş verdi")
}
else{
alert("Hər gün ən az " + result + " səhifə oxumalısınız!");
}
console.log("Səhifə sayı: " + page)
console.log("Gün sayı: " + days)
console.log("Nəticə: " + result)