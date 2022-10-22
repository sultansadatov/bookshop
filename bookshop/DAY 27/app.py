from flask import Flask, render_template

app = Flask(__name__)

book = {
    "name": "Incognito (beyinin gizli həyatı)",
    "price": 12.00,
    "old_price": 15.00,
    "description": '''Tanınmış nevroloq D.İqlmenin 20-dən çox dilə tərcümə edilən və indidən klassik əsərə çevrilən bu kitabı beynin sirli dünyasına təcrübələr, elmi biliklər və tarixi faktlar işığında səyahət edir. 
    Kitab tibbi mövzuda olsa da, müəllif yazarlıq məharətini və zəngin biliyini birləşdirərək elmi faktları sadə və müqayisəli dillə oxucularına təqdim edir. 
    Müəllif əsər boyu sədaqət geni, qumarbazlara çevrilən parkinson xəstələri, gen-mühit əlaqəsi, “yaxşı” və “pis” gen, şüuraltı və qərarvermə mexanizmi, məsuliyyət anlayışı, beynin insan həyatında rolu kimi bir çox mövzulara toxunur. 
    Alim bu mövzuların beyinlə əlaqəsini izah etməklə kifayətlənmir, beyinlə bağlı müxtəlif formullar və modellər irəli sürür. 
    İnsan psixologiyası və davranışlarına neyron və gen prizmasından baxmağı öyrədir. 
    Elmi-populyar dildə yazılmış bu kitab xüsusən müəllimlər, psixoloqlar, valideynlər, həkimlər üçün mühüm bilikləri ehtiva edir.''',
    "count": 2,
    "language": "Azerbaijani",
    "genre": "Psychology",
    "author": "David Eagleman",
    "publishing": "Qanun Nəşriyyatı"
}

@app.route("/")
def home_page():
    return render_template("index.html", page="home")

@app.route("/product/")
def product():
    return render_template("product.html", book_var=book, page="product")