
class PascalInterpreter(object):
    def doInterpreter(self, scanner):
        # For an interpreter:

        # for array P, px being symbol in array
        # while not EOF:
        #     switch(px)
        #         case identifier:
        #             px++
        #             get token in array
        #             push identifier onto stack
        #             break
        #         case int_const:
        #             px++
        #             get const in array
        #             push constant into stack
        #             break
        #         case assignment:
        #             px++
        #             pop the last two items from the stack
        #             store the value of the second item into the identifier
        #             break
        #         case other:
        #         .....
        #     px++


        # For an abstract stack machine:
        #     push the value
        #     push value of identifier
        #     push address of identifier
        #     add operator(pop two values on top, add and push result to stack)
        #     assignment op(pop top value, pop address on top, store value on address)
        #     for the infix of x=97*y that would be
        #     push add x
        #     push 97
        #     push y
        #     +
        #     assignment op

        print('interpreted!')
