def alternate(s):
    # หาอักขระที่ไม่ซ้ำกันทั้งหมด
    unique_chars = list(set(s))
    max_len = 0
    
    # วนลูปจับคู่อักขระ 2 ตัวที่ต่างกัน
    for i in range(len(unique_chars)):
        for j in range(i + 1, len(unique_chars)):
            char1 = unique_chars[i]
            char2 = unique_chars[j]
            
            # กรองเอาเฉพาะตัวอักษร 2 ตัวนี้จากสตริงตั้งต้น
            filtered_chars = [c for c in s if c == char1 or c == char2]
            
            # ตรวจสอบว่าเป็นสลับกันจริงๆ หรือไม่ (ไม่มีตัวติดกันที่เหมือนกัน)
            is_valid = True
            for k in range(1, len(filtered_chars)):
                if filtered_chars[k] == filtered_chars[k-1]:
                    is_valid = False
                    break
            
            # ถ้าสลับกันจริง ให้เก็บค่าความยาวที่มากที่สุด
            if is_valid:
                max_len = max(max_len, len(filtered_chars))
                
    return max_len