"""Numeric Operators EX01"""

__author__ = "730313907"

left_hand_side: str = str(input("Left-hand side: "))
right_hand_side: str = str(input("Right-hand side: "))

int_lhs: int = int(left_hand_side)
int_rhs: int = int(right_hand_side)

print(left_hand_side + " ** " + right_hand_side + " is " + str(int_lhs ** int_rhs))
print(left_hand_side + " / " + right_hand_side + " is " + str(int_lhs / int_rhs))
print(left_hand_side + " // " + right_hand_side + " is " + str(int_lhs // int_rhs))
print(left_hand_side + " % " + right_hand_side + " is " + str(int_lhs % int_rhs))