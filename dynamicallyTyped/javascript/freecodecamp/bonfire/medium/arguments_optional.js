function add() {
    var args = arguments;
    var checkNum = function (num) {
        if (typeof num !== 'number'){
            return undefined;
        }else
            return num;
    }
    var checkUndef = function(ltr){
      if(ltr === undefined)
        return true;
      else
        return false;
    }
    if (args.length > 1) {
        var a = checkNum(args[0]);
        var b = checkNum(args[1]);
        if (checkUndef(a) || checkUndef(b)) {
            return undefined;
        } else {return a + b;}
    } else {
        var c = args[0];
        if(checkNum(c)){
            return function(arg2) {
                if (checkUndef(c) || checkUndef(checkNum(arg2))) {
                    return undefined;
                }else {
                    return c + arg2;
                }
            };
        }
    }
}

add(2,3);
