from src.com.jalasoft.compiler.common.invalid_data_error import InvalidDataError


class Util:
    def sum_list(self, list_data):
        if len(list_data) == 0:
            raise InvalidDataError
        result = 0
        try:
            for element in list_data:
                result += element
            return result
        except TypeError:
            raise InvalidDataError()
