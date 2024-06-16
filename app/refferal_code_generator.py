import random


class CodeGenerator:
    
    __max_len: int = 16
    __low_symbols: str = 'abcdefghijklmnopqrstuvwxyz'
    __high_symbols: str = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    __num_symbols: str = '1234567890'
    
    def __init__(self) -> None:
        self.code = self.__generate_code()

    def __generate_code(self) -> str:
        code = 'obelisk-'
        choices = [self.__low_symbols, self.__high_symbols, self.__num_symbols]
        for i in range(self.__max_len):
            if i % 2 == 0:
                code += random.choice(random.choice(choices[:-random.randint(1, 2)]))
            else:
                code += random.choice(random.choice(choices))
        
        return code
