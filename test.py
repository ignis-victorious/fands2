#  ________________
#  Import LIBRARIES
from typing import Annotated, Any, get_type_hints, get_origin, get_args
from functools import wraps
#  Import FILES
#  ________________


def check_value_range(func):
    @wraps(func)
    def wrapped(x):
        type_hints = get_type_hints(double, include_extras=True)
        hint = type_hints["x"]
        if get_origin(hint) is Annotated:
            hint_type, *hint_args = get_args(hint)
            low, high = hint_args[0]

            if not low <= x <= high:
                raise ValueError(f"{x} falls outside boundary {low}-{high}")

        # execute function once all checks passed
        return func(x)

    return wrapped


def double(x: Annotated[int, (0, 100)]) -> int:
    type_hints: dict[str, Any] = get_type_hints(double, include_extras=True)
    hint = type_hints["x"]
    if get_origin(hint) is Annotated:
        hint_type, *hint_args = get_args(hint)
        low, high = hint_args[0]
        print(f"hint_type: {hint_type}")  # int
        print(f"hint_args: {hint_args}")  # the value
        print(f"low, high: {low, high}")  # the value
        if not low <= x <= high:
            raise ValueError(f"{x} falls outside boundary {low}-{high}")

    print(f"hint: {hint}")
    return x * 2


result = double(55)
print(result)

result = double(11155)
print(result)

# def double(x: Annotated[int, (0, 100)]) -> int:
#     # def double(x: int) -> int:
#     return x * 2


result: int = double(400)
print(result)
