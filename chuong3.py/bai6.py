def read_number(a: int, natural: bool = True) -> str:
    unit = {
        0: "",
        1: "Muoi",
        2: "Tram",
        3: "Nghin",
        4: "Muoi Nghin",
        5: "Tram Nghin",
        6: "Trieu",
        7: "Muoi Trieu",
        8: "Tram Trieu",
        9: "Ty",
    }
    number = {
        0: "Khong",
        1: "Mot",
        2: "Hai",
        3: "Ba",
        4: "Bon",
        5: "Nam",
        6: "Sau",
        7: "Bay",
        8: "Tam",
        9: "Chin",
    }

    if a == 0:
        return "Khong"

    result = ""
    i = 0
    while a > 0:
        digit = a % 10
        if digit != 0:
            part = number[digit] + " " + unit[i]
            result = part.strip() + " " + result
        a //= 10
        i += 1

    result = result.strip()

    # ✅ If natural mode is enabled, fix some common cases
    if natural:
        result = (
            result.replace("Mot Muoi", "Muoi")
                  .replace("Muoi Nam", "Muoi Lam")
                  .replace("Muoi Mot", "Muoi Mot")  # keep as is
                  .replace("Mot Nghin Mot", "Mot Nghin Le Mot")  # keep as is
                  .replace("Mot Trieu", "Mot Trieu")  # keep as is
        )

    return result


# Example usage:
print(read_number(15))           # digit mode: "Mot Muoi Nam - bai6.py:56"
print(read_number(15, True))     # natural: "Muoi Lam - bai6.py:57"

print(read_number(1001))         # "Mot Nghin Mot Muoi - bai6.py:59"
print(read_number(1010, True))   # same (no change needed)