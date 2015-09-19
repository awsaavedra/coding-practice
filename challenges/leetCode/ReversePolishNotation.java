/*
Alexander Saavedra
github: awsaavedra 
Evaluate the value of an arithmetic expression in Reverse Polish Notation.

Valid operators are +, -, *, /. Each operand may be an integer or another expression.

Some examples:
  ["2", "1", "+", "3", "*"] -> ((2 + 1) * 3) -> 9
  ["4", "13", "5", "/", "+"] -> (4 + (13 / 5)) -> 6
*/



public class Solution {
    public int evalRPN(String[] tokens) {
        int temp1 = 0;
        int temp2 = 0;
        int temp3 = 0;
        //create a new stack
        Stack<Integer> stack = new Stack<Integer>(); //cannot dynamically allocate into stack
        for(int i = 0; i < tokens.length; i++){ //if you didn't have length, while(!stack.empty())
            //first check for operators
        if( tokens[i].equals("*")){
                //casting temp1 & 2 into integer values instead of strings
                temp1 = (int)stack.pop();
                temp2 = (int)stack.pop();
                temp3 = temp2*temp1;
                stack.push(temp3);
            }else if( tokens[i].equals("/")){
                //casting temp1 & 2 into integer values instead of strings
                temp1 = (int)stack.pop();
                temp2 = (int)stack.pop();
                temp3 = temp2/temp1;
                stack.push(temp3);
            }else if( tokens[i].equals("+")){
                //casting temp1 & 2 into integer values instead of strings
                temp1 = (int)stack.pop();
                temp2 = (int)stack.pop();
                temp3 = temp2+temp1;
                stack.push(temp3);
            }
            else if( tokens[i].equals("-")){
                //casting temp1 & 2 into integer values instead of strings
                temp1 = (int)stack.pop();
                temp2 = (int)stack.pop();
                temp3 = temp2-temp1;
                stack.push(temp3);
                
            }else{
                
                stack.push(Integer.parseInt(tokens[i]));
            }
            }
            return stack.pop();
        }
}
