def staircase(n, pattern='#'):
    # เช็คเงื่อนไข 0 < n <= 30
    if n <= 0 or n > 30:
        return ""
    
    steps = []
    for i in range(1, n + 1):
        spaces = " " * (n - i)  # สร้างช่องว่างให้ชิดขวา
        symbols = pattern * i   # สร้างตัวอักษรตามจำนวนขั้น
        steps.append(spaces + symbols)
        
    return "\n".join(steps)