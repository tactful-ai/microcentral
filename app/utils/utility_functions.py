from app.api.exceptions import ExceptionCustom
from app.utils.utity_datatype import parse_stringified_value

def calculate_error_for_strings(value: str, desired: str, weight: float, criteria: str) -> float:
    if criteria == 'equal':
        return weight if value != desired else 0
    else:
        raise ExceptionCustom(status_code=422, detail="Invalid criteria for string type.")


def calculate_error_for_booleans(value: bool, desired: bool, weight: float, criteria: str) -> float:
    if criteria == 'equal':
        return weight if value != desired else 0
    else:
        raise ExceptionCustom(status_code=422, detail="Invalid criteria for boolean type.")

def calculate_error_for_numbers(value: float, desired: float, weight: float, criteria: str) -> float:
    if criteria == 'equal':
        return weight if value != desired else 0
    elif criteria == 'greater':
        return max(0, ((desired - value) / desired) * weight) if value < desired else 0
    elif criteria == 'smaller':
        return max(0, ((value - desired) / desired) * weight) if value > desired else 0
    elif criteria == 'greater or equal':
        return max(0, ((desired - value) / desired) * weight) if value < desired else 0
    elif criteria == 'smaller or equal':
        return max(0, ((value - desired) / desired) * weight) if value > desired else 0
    else:
        raise ExceptionCustom(status_code=422, detail="Invalid criteria for number type.")

  
def main_calculate_error(measured: str, desired: str, weight: float, criteria: str, metric_type: str) -> float:
    parsed_measured = parse_stringified_value(measured, metric_type)
    parsed_desired = parse_stringified_value(desired, metric_type)
    
    if metric_type == 'string':
        return calculate_error_for_strings(parsed_measured, parsed_desired, weight, criteria)
    elif metric_type == 'boolean':
        return calculate_error_for_booleans(parsed_measured, parsed_desired, weight, criteria)
    elif metric_type == 'integer':
        return calculate_error_for_numbers(float(parsed_measured), float(parsed_desired), weight, criteria)
    elif metric_type =='float':
        return calculate_error_for_numbers(float(parsed_measured), float(parsed_desired), weight, criteria)
    else:
        raise ValueError("Unsupported metric type for error calculation.")
      
      
def calculate_score(error_value: float) -> float:
    return 100 - error_value if error_value is not None else 0
