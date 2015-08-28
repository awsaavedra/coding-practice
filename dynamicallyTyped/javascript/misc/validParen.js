function isValid(s) {
    var map = [];
    map['('] = ')';
    map['['] = ']';
    map['{'] = '}';
 
    var stack = [];
 
    for (var i = 0; i < s.length; i++) {
        var curr = s.charAt(i);
 
        if (map[curr]!=null) {
            stack.push(curr);
        } else if (checkValue(map,curr)) {
            if (!stack.length == 0 && map[stack[stack.length-1]] == curr) {
                stack.pop();
            } else {
                return false;
            }
        }
    }
 
    return stack.length == 0;
}

function checkValue(map, val) {
    for(var i in map) {
        if(map[i] == val) {
            return true;
        }
    }
    return false;
}

	
console.log(isValid('{{}[]}'));
console.log(isValid('{{}[]]'));
