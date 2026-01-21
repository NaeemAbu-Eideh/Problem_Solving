/**
 * @param {string} s
 * @return {number}
 */
   function keyNumber(char){
      switch(char){
        case 'a': {return 1;} break;
        case 'b': {return 2;} break;
        case 'c': {return 3;} break;
        case 'd': {return 4;} break;
        case 'e': {return 5;} break;
        case 'f': {return 6;} break;
        case 'g': {return 7;} break;
        case 'h': {return 8;} break;
        case 'i': {return 9;} break;
        case 'j': {return 10;} break;
        case 'k': {return 11;} break;
        case 'l': {return 12;} break;
        case 'm': {return 13;} break;
        case 'n': {return 14;} break;
        case 'o': {return 15;} break;
        case 'p': {return 16;} break;
        case 'q': {return 17;} break;
        case 'r': {return 18;} break;
        case 's': {return 19;} break;
        case 't': {return 20;} break;
        case 'u': {return 21;} break;
        case 'v': {return 22;} break;
        case 'w': {return 23;} break;
        case 'x': {return 24;} break;
        case 'y': {return 25;} break;
        case 'z': {return 26;} break;
        case 'A': {return 1;} break;
        case 'B': {return 2;} break;
        case 'C': {return 3;} break;
        case 'D': {return 4;} break;
        case 'E': {return 5;} break;
        case 'F': {return 6;} break;
        case 'G': {return 7;} break;
        case 'H': {return 8;} break;
        case 'I': {return 9;} break;
        case 'J': {return 10;} break;
        case 'K': {return 11;} break;
        case 'L': {return 12;} break;
        case 'M': {return 13;} break;
        case 'N': {return 14;} break;
        case 'O': {return 15;} break;
        case 'P': {return 16;} break;
        case 'Q': {return 17;} break;
        case 'R': {return 18;} break;
        case 'S': {return 19;} break;
        case 'T': {return 20;} break;
        case 'U': {return 21;} break;
        case 'V': {return 22;} break;
        case 'W': {return 23;} break;
        case 'X': {return 24;} break;
        case 'Y': {return 25;} break;
        case 'Z': {return 26;} break;
      }
   }
var countKeyChanges = function(s) {
    key = keyNumber(s[0]);
    count = 0;
    for(let i = 1 ; i < s.length; i++){
        if(keyNumber(s[i]) !== key){
            count++;
            key = keyNumber(s[i]);
        }
    }
    return count; 
};