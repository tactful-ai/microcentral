from app.api.exceptions import ExceptionCustom
from app.utils.utity_datatype import parse_stringified_value
#def convert_desired_value(desired_value, measured_value) -> float:
#    if type(desired_value) == type(measured_value):
#        return 100.0 if desired_value == measured_value else 0.0
#    else:
#        return 0.0 

##def  calculate_error_for_strings(value, desired, weight, criteria):
##  return 0
#def calculate_error(measured: float, desired: str, criteria: str) -> float:
#    converted_value = convert_desired_value(desired, measured)  
#    print(type(converted_value))  

#    #if metricType == 'string':
#    #  return calculate_error_for_strings(value, desired, weight, criteria)
#    #elif metric
  
#    if criteria == 'greater':
#        error = max(0, ((converted_value - measured) / converted_value) * 100)
#    elif criteria == 'smaller':
#        error = max(0, ((measured - converted_value) / converted_value) * 100)
#    elif criteria == 'greater or equal':
#        error = max(0, ((converted_value - measured) / converted_value) * 100)
#    elif criteria == 'smaller or equal':
#        error = max(0, ((measured - converted_value) / converted_value) * 100)
#    elif criteria == 'equal':
#        error = (abs(measured - converted_value) / converted_value) * 100
#    else:
#        raise ValueError(f"Invalid criteria: {criteria}")

#    return min(100, error)

#def calculate_score(error: float) -> float:
#    return 100 - error

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
