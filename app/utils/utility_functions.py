
def convert_desired_value(desired_value ) -> float:
    if isinstance(desired_value, str):
        if desired_value == "Excellant":
            return 100.0
        elif desired_value == "Good":
            return 65.0
        elif desired_value == "Bad":
            return 0.0
        elif desired_value == "True":
            return 100.0
        elif desired_value == "False":
            return 0.0
        else:
            try:
                return float(desired_value)
            except ValueError:
                raise ValueError(f"Invalid desired_value: {desired_value}")
    elif isinstance(desired_value, bool):
        return 100.0 if desired_value else 0.0
    elif isinstance(desired_value, (float, int)):
        return float(desired_value)
    else:
        raise TypeError(f"Unsupported type for desired_value: {type(desired_value)}")


def calculate_error(measured: float, desired: str, criteria: str) -> float:
    converted_value = convert_desired_value(desired)  
    print(type(converted_value))  

    if criteria == 'greater':
        error = max(0, ((converted_value - measured) / converted_value) * 100)
    elif criteria == 'smaller':
        error = max(0, ((measured - converted_value) / converted_value) * 100)
    elif criteria == 'greater or equal':
        error = max(0, ((converted_value - measured) / converted_value) * 100)
    elif criteria == 'smaller or equal':
        error = max(0, ((measured - converted_value) / converted_value) * 100)
    elif criteria == 'equal':
        error = (abs(measured - converted_value) / converted_value) * 100
    else:
        raise ValueError(f"Invalid criteria: {criteria}")

    return min(100, error)

def calculate_score(error: float) -> float:
    return 100 - error
