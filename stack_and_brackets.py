class Stack:
    """
    Stack realization
    isEmpty - проверка стека на пустоту. Метод возвращает True или False.
    push - добавляет новый элемент на вершину стека. Метод ничего не возвращает.
    pop - удаляет верхний элемент стека. Стек изменяется. Метод возвращает верхний элемент стека
    peek - возвращает верхний элемент стека, но не удаляет его. Стек не меняется.
    size - возвращает количество элементов в стеке.
    """
    def __init__(self):
        self.stack_data = []

    def push(self, new_element):
        self.stack_data.append(new_element)

    def pop(self):
        last_element = self.stack_data.pop()
        return last_element

    def peek(self):
        last_element = self.stack_data[-1]
        return last_element

    def size(self) -> int:
        length_stack = len(self.stack_data)
        return length_stack

    def is_empty(self) -> bool:
        if self.size() == 0:
            return True
        else:
            return False

    def clean(self):
        self.stack_data = []


class BracketsChecker:
    def __init__(self, stack_instant: Stack):
        self.stack = stack_instant

    def __check_brackets_sequence(self, brackets_sequence: str):
        """
        Метод проверяет последовательность скобок и возвращает:
         - True, если строка корректная
         - False, если строка составлена неверно.
        """
        for bracket in brackets_sequence:
            if bracket in ['(', '[', '{']:
                self.stack.push(bracket)
            else:
                if self.stack.is_empty():
                    return False
                elif bracket == ')':
                    if self.stack.peek() == '(':
                        self.stack.pop()
                    else:
                        return False
                elif bracket == ']':
                    if self.stack.peek() == '[':
                        self.stack.pop()
                    else:
                        return False
                elif bracket == '}':
                    if self.stack.peek() == '{':
                        self.stack.pop()
                    else:
                        return False

        if self.stack.is_empty():
            return True
        else:
            return False

    def check_brackets(self, brackets_sequence: str):
        """
        Метод проверяет последовательность скобок и возвращает:
         - 'Сбалансированно', если строка корректная
         - 'Несбалансированно', если строка составлена неверно.
        """
        check_result = self.__check_brackets_sequence(brackets_sequence)
        if check_result:
            return 'Сбалансированно'
        else:
            self.stack.clean()
            return 'Несбалансированно'


if __name__ == '__main__':
    stack = Stack()
    checker = BracketsChecker(stack)
    sequence_1 = '(((([{}]))))'
    sequence_2 = '[([])((([[[]]])))]'
    sequence_3 = '{()}'
    sequence_4 = '{{[()]}}'
    sequence_5 = '}{}'
    sequence_6 = '{{[(])]}}'
    sequence_7 = '[[{())}]'

    print(checker.check_brackets(sequence_1))
    print(checker.check_brackets(sequence_2))
    print(checker.check_brackets(sequence_3))
    print(checker.check_brackets(sequence_4))
    print(checker.check_brackets(sequence_5))
    print(checker.check_brackets(sequence_6))
    print(checker.check_brackets(sequence_7))
