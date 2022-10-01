#!/usr/bin/python3

import getopt

# Script option class
class option:

    def __init__(self) -> None:
        pass
    
    def __dummy_calback(self, arg = ""):
        print("Dummy arg callback! arg = [ ", str(arg), " ]")
        pass

    short_option = ""
    long_option = ""
    mandatory = False
    take_arg = False
    callback = __dummy_calback

class options_handler:

    def __init__(self) -> None:
        self.options_list = []
        self.__short_options = ""
        self.__long_options = ""
        pass

    # options_list = []


    def register_option(self, _option):
        if not isinstance(_option, option):
            print("ERROR! Input arg is not an instance of a option class")
            return False
        
        if (type(_option.short_option) is not str) or (type(_option.long_option) is not str):
            print("ERROR! short or long option are not strings")
            return False

        if (len(_option.short_option) == 0) and (len(_option.long_option) == 0):
            print("ERROR! No short or long option given")
            return False

        if (len(_option.long_option) > 0) and (len(_option.long_option) < 3):
            print("ERROR! Long option must be composed of at least 3 characters!")
            

        if self.is_duplicated(_option):
            print("ERROR! Short or long option string duplicated!")
            return False
        else:
            self.options_list.append(_option)
            return True
        
    def is_duplicated(self, _option):
        """ Check if given option (short or long attribute) is already registered"""

        for registered_option in self.options_list:

            if registered_option.short_option == _option.short_option:
                return True
            
            if registered_option.long_option == _option.long_option:
                return True

        return False


    def get_options_number(self):
        return len(self.options_list)

    def __parse_option(self, _option):
        
        pass

    def __create_getops_codes(self):

        pass


    # Process options list. Find if input options mach's registered options and execute their callbacks!
    def process_options(self, input_options):

        print("Processing input options [ ", input_options, " ]")
        
        opts, args = getopt.getopt(input_options, )

        pass

        

