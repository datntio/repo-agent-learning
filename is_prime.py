from math import isqrt

def is_prime(n: int) -> bool:
    """
    Kiểm tra n có phải số nguyên tố.
    - Trả về False cho n <= 1 hoặc số âm.
    - Tối ưu: chỉ duyệt 6k ± 1 đến √n.
    """
    if n <= 1:
        return False
    if n <= 3:
        return True  # 2, 3
    if n % 2 == 0 or n % 3 == 0:
        return False

    # Kiểm tra các số dạng 6k ± 1
    limit = isqrt(n)
    i = 5
    while i <= limit:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True
