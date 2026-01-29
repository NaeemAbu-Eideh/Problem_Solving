/**
 * @param {number} num
 * @return {string}
 */

function convertToRoman(num){
    var str = "" + num;
    switch(str){
        case "1": {return "I";}break;
        case "5": {return "V";}break;
        case "10": {return "X";}break;
        case "50": {return "L";}break;
        case "100": {return "C";}break;
        case "500": {return "D";}break;
        case "1000": {return "M";}break;
        case "4": {return "IV";}break;
        case "9": {return "IX";}break;
        case "40": {return "XL";}break;
        case "90": {return "XC";}break;
        case "400": {return "CD";}break;
        case "900": {return "CM";}break;
    }
}

var intToRoman = function(num) {
    var sum = "";
    var str_num = "" + num;
    var indecies = str_num.length - 2;
    for(let i = 0 ; i < str_num.length; i++){
        let index = indecies;
        indecies--;
        let str = "";
        str += str_num[i];
        while(index >= 0){
            str+= '0';
            index--;
        }
        var value = Number(str);
        while(value > 0){
            if(value >= 1000){
                sum += convertToRoman(1000);
                value -= 1000;
            }
            else if(value >= 900){
                sum += convertToRoman(900);
                value -= 900;
            }
            else if(value >= 500){
                sum += convertToRoman(500);
                value -= 500;
            }
            else if(value >= 400){
                sum += convertToRoman(400);
                value -= 400;
            }
            else if(value >= 100){
                sum += convertToRoman(100);
                value -= 100;
            }
            else if(value >= 90){
                sum += convertToRoman(90);
                value -= 90;
            }
            else if(value >= 50){
                sum += convertToRoman(50);
                value -= 50;
            }
            else if(value >= 40){
                sum += convertToRoman(40);
                value -= 40;
            }
            else if(value >= 10){
                sum += convertToRoman(10);
                value -= 10;
            }else if(value >= 9){
                sum += convertToRoman(9);
                value -= 9;
            }
            else if(value >= 5){
                sum += convertToRoman(5);
                value -= 5;
            }else if(value >= 4){
                sum += convertToRoman(4);
                value -= 4;
            }
            else{
               sum += convertToRoman(1);
               value -= 1; 
            }
        }
    }
    return sum;
};