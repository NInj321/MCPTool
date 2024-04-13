from loguru import logger
from mccolors import mcwrite, mcreplace
from typing import Union


class GetInput:
    def __init__(self, input_message: str, input_type: str) -> None:
        self.input_message: Union[str, None] = input_message
        self.input_type: str = input_type
        self.user_input: str = ''

    def get_input(self) -> tuple:
        """
        Method to get the user input and validate it

        Returns:
            tuple: The user input and a boolean value
        """

        # Check if the input message is None
        if self.input_message is None:
            logger.error('Input message is None')
            return (None, False)

        while True:
            try:
                # Get the user input
                self.user_input: str = input(mcreplace(self.input_message))

                if self.input_type == 'string':
                    return self._string_input()
                
                if self.input_type == 'integer':
                    output: Union[tuple, None] = self._integer_input()
            
                    if output is not None:
                        return output
                    
                if self.input_type == 'boolean':
                    output: Union[tuple, None] = self._boolean_input()
            
                    if output is not None:
                        return output
                    
                if self.input_type == 'country_code':
                    output: Union[tuple, None] = self._country_code_input()
            
                    if output is not None:
                        return output

            except KeyboardInterrupt:
                return (None, False)
            
    def _string_input(self) -> str:
        """
        Method to get the string input
        """

        return (self.user_input, True)
    
    def _integer_input(self) -> int:
        """
        Method to get the integer input
        """

        try:
            return (int(self.user_input), True)
        
        except ValueError:
            mcwrite('Invalid input. Please enter a valid integer.')
            return None
        
    def _boolean_input(self) -> bool:
        """
        Method to get the boolean input
        """

        if self.user_input.lower() == 'y' or self.user_input.lower() == 'n':
            return (self.user_input.lower() == 'y', True)
        
        mcwrite('Invalid input. Please enter either y or n.')
        return None
    
    def _country_code_input(self) -> None:
        """
        Method to get the country code input
        """

        if len(self.user_input) == 2:
            return (self.user_input, True)
        
        mcwrite('Invalid input. Please enter a valid country code.')
        return None
    

            
