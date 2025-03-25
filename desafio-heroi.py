let nome = "Pedro" // prompt("Por favor, digite seu nome:");
let nivel = 1200 // prompt("Por favor, digite um nível entre (0 - 20000):");

switch (nivel) 
{

case nivel < 1000:
console.log("O Herói de nome " + nome + " está no nível Ferro");
break;

case nivel < 2000:
console.log("O Herói de nome " + nome + " está no nível bronze");
break;

case nivel < 5000:
console.log("O Herói de nome " + nome + " está no nível Prata");
break;

case nivel < 7000:
console.log("O Herói de nome " + nome + " está no nível Ouro");
break;

case nivel < 8000:
console.log("O Herói de nome " + nome + " está no nível Platina");
break;

case nivel < 9000:
console.log("O Herói de nome " + nome + " está no nível Ascendente");
break;

case nivel < 10000:
console.log("O Herói de nome " + nome + " está no nível Imortal");
break;

default:
console.log("O Herói de nome " + nome + " está no nível Radiante");
break;

}