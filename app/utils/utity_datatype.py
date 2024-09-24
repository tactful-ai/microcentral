
def parse_stringified_value(value: str, target_type: str) -> int | float | bool | str:

    value_str = str(value).lower()

    if target_type == 'boolean':
        if value_str in ('true', '1'):
            return True
        elif value_str in ('false', '0'):
            return False
        else:
            raise ValueError(f"Cannot convert {value} to boolean.")

    elif target_type == 'integer':
        try:
            return int(value)
        except ValueError:
            raise ValueError(f"Cannot convert {value} to integer.")

    elif target_type == 'float':
        try:
            return float(value)
        except ValueError:
            raise ValueError(f"Cannot convert {value} to float.")

    elif target_type == 'string':
        try:
            return value
        except ValueError:

            raise ValueError(f"Cannot convert {value} to string.")
    else:
        raise ValueError(f"Unsupported value type: {type(value)}")


def stringify_value(value) -> str:

    if isinstance(value, bool):
        return 'True' if value else 'False'
    elif isinstance(value, (int, float)):
        return str(value)
    elif isinstance(value, str):
        return value
    else:
        raise ValueError(f"Unsupported value type: {type(value)}")
