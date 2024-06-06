class Solution {
    public boolean isValid(String s) {
        if (s.length() == 0) {
            return true;
        }
        if (s.length() % 2 == 1) {
            return false;
        }

        Stack<Character> stack = new Stack();

        for (Character c : s.toCharArray()) {
            switch (c) {
                case ')':
                    if (!stack.empty() && stack.peek() == '(') {
                        stack.pop();
                        break;
                    } else {
                        return false;
                    }
                case ']':
                    if (!stack.empty() && stack.peek() == '[') {
                        stack.pop();
                        break;
                    } else {
                        return false;
                    }
                case '}':
                    if (!stack.empty() && stack.peek() == '{') {
                        stack.pop();
                        break;
                    } else {
                        return false;
                    }
                default:
                    stack.push(c);
            }
        }
        if (stack.empty()) {
            return true;
        } else {
            return false;
        }
    }
}
