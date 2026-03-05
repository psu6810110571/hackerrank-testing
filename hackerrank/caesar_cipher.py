def caesarCipher(s, k):
    result = []
    
    for char in s:
        # เช็คว่าเป็นตัวอักษรภาษาอังกฤษหรือไม่
        if char.isalpha():
            # กำหนดค่าเริ่มต้นของ ASCII ว่าเป็นพิมพ์ใหญ่หรือพิมพ์เล็ก
            base = ord('A') if char.isupper() else ord('a')
            
            # คำนวณการเลื่อนตำแหน่ง (ใช้ modulo 26 เพื่อให้วนกลับมา A ถ้าเกิน Z)
            shifted_char = chr((ord(char) - base + k) % 26 + base)
            result.append(shifted_char)
        else:
            # ถ้าไม่ใช่ตัวอักษรภาษาอังกฤษ (เช่น -, !, เว้นวรรค) ให้คงเดิมไว้
            result.append(char)
            
    return "".join(result)