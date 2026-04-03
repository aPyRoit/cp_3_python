def array_diff(a: list, b: list) -> list:
    return [x for x in a if x not in b]


def sum_pairs(nums: list, sum: int) -> list:
    seen = set()
    for x in nums:
        complement = sum - x
        if complement in seen:
            return [complement, x]
        seen.add(x)
    return None


def remove_duplicate_ids(obj: dict) -> dict:
    sorted_keys = sorted(obj.keys(), key=lambda k: int(k))

    char_owner = {}
    for key in sorted_keys:
        for char in obj[key]:
            char_owner[char] = key
    result = {key: [] for key in obj}
    for key in sorted_keys:
        seen_in_array = set()
        for char in obj[key]:
            if char_owner[char] == key and char not in seen_in_array:
                result[key].append(char)
                seen_in_array.add(char)

    return result


def lazy(n: int):
    def decorator(func):
        call_count = [0]

        def wrapper(*args, **kwargs):
            call_count[0] += 1
            count = call_count[0]

            if n == -1:
                return None
            elif n == 1:
                return func(*args, **kwargs)
            elif n > 0:
                if (count - 1) % n == 0:
                    return func(*args, **kwargs)
                return None
            else:
                if count % (-n) == 0:
                    return None
                return func(*args, **kwargs)

        return wrapper
    return decorator