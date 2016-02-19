function processData(input) {
    var s = input.toLowerCase();
    var pangram = "pangram";
    var letters = "zqxjkvbpygfwmucldrhsnioate";
    for (var i = 0; i < 26; i++){
        if (s.indexOf(letters.charAt(i)) == -1){
            pangram = "not pangram";
        }
    }
    console.log(pangram);
} 

process.stdin.resume();
process.stdin.setEncoding("ascii");
_input = "";
process.stdin.on("data", function (input) {
    _input += input;
});

process.stdin.on("end", function () {
   processData(_input);
});
