function add() {
  var args = arguments;
  var argsLen = args.length;
  if(argsLen > 1){
    if(ifNum(args[0]) && ifNum(args[1])){
      var args1 = args[0];
      var args2 = args[1]; 
      return args1 + args2;
    } 
  }else{
    var args1 = args[0];
    if(ifNum(args1)){
      return function(arg2){
        if(ifNum(arg2)){
          return args1 + arg2;
        }
      }
    }
  }
   
  
  function ifNum(n){
    if(typeof n === "number"){
      return true;
    }else{
      return false;
    }
  }
  
  function ifDef(y){
    if(y !== undefined){
      return true;
    }else{
      return false;
    }
  }
}

