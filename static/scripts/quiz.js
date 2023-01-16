var quizResults = [];

function getAnswer() {
    var radioID = document.querySelector('input[name="inlineRadioOptions1"]:checked').id;
    console.log(radioID)
    var result = radioID.substring(radioID.length - 1);

    switch (result) {
        case "1":
            quizResults.push("A");
            break;
        case "2":
            quizResults.push("B");
            break;
        case "3":
            quizResults.push("C");
            break;
        case "4":
            quizResults.push("D");
            break;
        case "5":
            quizResults.push("E");
            break;
    }

    console.log(quizResults);
}