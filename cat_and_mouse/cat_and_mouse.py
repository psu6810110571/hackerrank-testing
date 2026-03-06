def cat_and_mouse(x: int, y: int, z: int) -> str:
    # x = ตำแหน่งแมว A
    # y = ตำแหน่งแมว B
    # z = ตำแหน่งหนู C
    
    dist_a = abs(z - x) # ระยะทางแมว A ถึงหนู C
    dist_b = abs(z - y) # ระยะทางแมว B ถึงหนู C
    
    if dist_a < dist_b:
        return "Cat A"
    elif dist_b < dist_a:
        return "Cat B"
    else:
        return "Mouse C"