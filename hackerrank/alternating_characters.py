def alternatingCharacters(s):
    deletions = 0
    # วนลูปเช็คตัวอักษรเทียบกับตัวก่อนหน้า ถ้าเหมือนกันให้เพิ่มค่าการลบ
    for i in range(1, len(s)):
        if s[i] == s[i-1]:
            deletions += 1
            
    return deletions