class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for i in tokens:
            try:
                num = int(i)
                stack.append(num)
            except ValueError:
                a = stack.pop()
                b = stack.pop()

                if i  == "+":
                    stack.append(b + a)
                elif i == "-":
                    stack.append(b - a)
                elif i == "*":
                    stack.append(b * a)
                elif i == "/":
                    stack.append(int(b / a))
        return stack[0]


      