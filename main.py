from typing import List

class ExpressionEvaluator:
    def __init__(self, expression: str) -> None:
        self.expression = expression

    def evaluate(self) -> int:
        stack: List[int] = []
        num = 0
        sign = '+'

        for i, char in enumerate(self.expression + '+'):
            if char.isdigit():
                num = num * 10 + int(char)

            if char in '+-*/':
                if sign == '+':
                    stack.append(num)
                elif sign == '-':
                    stack.append(-num)
                elif sign == '*':
                    stack.append(stack.pop() * num)
                elif sign == '/':
                    stack.append(int(stack.pop() / num))

                num = 0
                sign = char

        return sum(stack)


if __name__ == "__main__":
    evaluator = ExpressionEvaluator("3+2*2")
    print(evaluator.evaluate())
