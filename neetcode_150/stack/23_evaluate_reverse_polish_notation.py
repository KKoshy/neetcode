class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        register = []
        for token in tokens:
            if token in "+-/*":
                num_2 = register.pop()
                num_1 = register.pop()
                if token == "+":
                    result = num_1 + num_2
                elif token == "-":
                    result = num_1 - num_2
                elif token == "*":
                    result = num_1 * num_2
                else:
                    result = int(num_1/num_2)
                register.append(result)
            else:
                register.append(int(token))
        return register[0]
