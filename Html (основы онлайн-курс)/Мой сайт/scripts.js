function calc() {
    var a = prompt("Первое число:");
    var b = prompt("Второе число:");
    
    if(a == "" || b == "") {
        return;
    }

    a = parseInt(a);
    b = parseInt(b);
    
    var sum = a + b;
    alert("Сумма чисел: " + sum);

    var pro = a * b;
    alert("Произведение чисел: " + pro);

    if(a > b) {
        var vich1 = a - b;
        alert("Разность чисел " + a + " и " + b + ": " + vich1);

        var del1 = a / b;
        alert("Частное чисел " + a + " и " + b + ": " + del1);
    }
    else if(a < b) {
        var vich2 = b - a;
        alert("Разность чисел " + b + " и " + a + ": " + vich2);

        var del2 = b / a;
        alert("Частное чисел " + b + " и " + a + ": " + del2);
    }
}



function convert(){
    var rub = prompt("Введите количество рублей:");
    if(rub == ""){
        return;
    }
    rub = parseInt(rub);
    var dollar = rub/64;
    var euro = rub/72;
    alert("Ваши рубли в долларах: " + dollar);
    alert("Ваши рубли в евро: " + euro);
}



function factor(){
    var b = 1;
    var c = 0;
    function factorial(a) {
        if(a === 0){
            alert("Принимаются числа от 1!");
        }
        else if(a == ""){
            return;
        }
        else {
            while (c < a) { 
                b = (c + 1) * b;
                c++;
            }
            if(b == Infinity){
                alert("Ваше число слишком большое!");
            }
            else {
                alert("Факториал числа " + a + " равен " + b + ".");
            }
        }
    } 
    factorial(prompt("Введите число:"));
}



function geopro(){
    var num = prompt("Введите число:");
    if(num == ""){
        return;
    }
    num = parseFloat(num);
    var sum = 0;
    var p = 1;
    while(p <= num) {
        sum = sum + p;
        p++;
    }
    alert("Число в геометрической прогрессии = " + sum);
}



function riddles() {
		var a = prompt("Больше часа, меньше минуты?");
        a = a.toLowerCase();
			if (a == "секунда") {
				alert("Молодец! Правильно!");
				var c = (1);
			}
			else{
				alert("Неправильно! Правильный ответ: секунда.");
				var c = (0);
			}
    
    
	alert("Следующая загадка...");
    
    
		var b = prompt("Какой слон без носа?");
        b = b.toLowerCase();
			if (b == "шахматный" || b == "шахматный слон") {
				alert("Молодец! Правильно!");
				var c = (c+1);
			}
			else{
				alert("Неправильно! Правильный ответ: шахматный.");
				var c = (c+0);
			}
    
    
    alert("Последняя загадка...");
    
    
        var d = prompt("На каком языке говорят молча?");
        d = d.toLowerCase();
			if (d == "язык жестов" || d == "немой" || d == "языке жестов" || d == "немом" || d == "на языке жестов" || d == "на немом") {
				alert("Молодец! Правильно!");
				var c = (c+1);
			}
			else{
				alert("Неправильно! Правильный ответ: язык жестов.");
				var c = (c+0);
			}
    
    
    if (c == 1) {
        var e = (" загадку!");
    }
    if (c > 1){
        var e = (" загадки!");
    }
    if (c > 0){
        alert("Ты ответил правильно на " + c + e);
    }
    else{
        alert("Увы! Ты проиграл и не ответил ни на одну загадку...");
    }
    

	alert("Спасибо за игру! Удачи!");
}



function ugadai(){
    var answer = parseInt(Math.random() * 100);
    var i = parseInt(0);
    
    do {
    var uanswer = prompt("Введи число:");
    if(uanswer == ''){
        break;
    }
    uanswer = parseInt(uanswer);

    if(uanswer < answer){
        alert('Твой ответ меньше моего числа.');
        i++;
    }
    else if(uanswer > answer){
        alert('Твой ответ больше моего числа.');
        i++;
    } 
    else if(uanswer == answer){
        alert('Правильный ответ! Молодец!');
        var a = "";  
        if (i == 1){
            a = " попытку.";
        }
        else if(i == 2 || i == 3 || i == 4){
            a = " попытки.";
        }
        else {
            a = " попыток.";
        }
        alert('Ты потратил ' + i + a);
        break;
    }
    else {
        alert('Необходимо ввести число!');
    }        
    }while(true)
}



function vklad(){
    var money = prompt("Сумма вклада, руб.:");
    if(money == ""){
        return;
    }
    money = money.replace(",", ".")
    money = parseFloat(money);

    
    var persent = prompt("Процентная ставка, %:");
    if(persent == ""){
        return;
    }
    persent = persent.replace(",", ".")
    persent = parseFloat(persent);
    
    var years = prompt("Срок вклада, лет:");
    if(years == ""){
        return;
    }
    years = years.replace(",", ".")
    years = parseFloat(years);

    for (var i = 0.5; i <= years; i = i + 0.5) {
        money = money + (0.5 * money) * persent / 100;
        alert("Прошло лет: " + i + ", сумма на счету: " + Math.floor(money));
    }
}