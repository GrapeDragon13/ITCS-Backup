var term = 'mississippi';
var definition = 'the name of a state and a river';
var correctlyGuessed = Array.from("-".repeat(term.length));
var guessed = [];
var numWrong = 0;
//var term = JSON.parse(data);

updateScreen(numWrong);

function theGallows(numWrong) {
    var gallowsPic;
    if (numWrong == 0) {
        var gallowsPic = 'one';
    } else if (numWrong == 3) {
        var gallowsPic = 'two';
    } else if (numWrong == 4) {
        var gallowsPic = 'three';
    } else {
        var gallowsPic = 'four';
    }
    document.getElementById("gallows").innerHTML=gallowsPic;
}

function guessInput(char){
    // checking input
    if(!(guessed.includes(char))){
        guessed.push(char);
    }
    guessed.sort();
    
    // if guess in term
    if(term.includes(char)){
        for (var i = 0; i < term.length; i++) {
            if (term[i] == char){
                correctlyGuessed[i] = char;
            }
        }
    }
    //not in term
    else{
        numWrong++;
        // update gallows
    }
    updateScreen()
    // have they solved the game?
    if(term == correctlyGuessed.join("")){
        //update gallows
        numWrong = 7;
        updateGallows(numWrong);
    }
}

function updateScreen(){
    //document.getElementById("theGallows").innerHTML=style.backgroundImage="url()";
    document.getElementById("definition").innerHTML=definition;
    document.getElementById("correctlyGuessed").innerHTML=correctlyGuessed.join(" ");
    document.getElementById("guessed").innerHTML=guessed.join(" ");
}

function textSolve() {
    var guess = document.getElementById("textSolve").value;
    if(term == guessed){
        //update gallows
        numWrong = 7;
    } else {
        numWrong = 6;
    }
    updateGallows(numWrong);
}

function newTurn() {
    var correctlyGuessed = Array.from("-".repeat(term.length));
    var guessed = [];
    var numWrong = 0;
}