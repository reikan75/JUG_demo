class Calculator :
    # return the sum between 2 operands
    def mysum(self, first_operand, second_operand):
        return first_operand + second_operand

    # return the minimum between 2 operands
    def mymin(self, first_operand, second_operand):
        return first_operand if second_operand > first_operand else second_operand

    # return the maximum between 2 operands
    def mymax(self, first_operand, second_operand):
        return first_operand if second_operand < first_operand else second_operand