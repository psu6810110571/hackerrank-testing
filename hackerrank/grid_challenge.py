def gridChallenge(grid):
    # เรียงลำดับตัวอักษรในแต่ละแถว (a-z)
    sorted_grid = []
    for row in grid:
        sorted_grid.append("".join(sorted(row)))
        
    rows = len(sorted_grid)
    cols = len(sorted_grid[0])
    
    # ตรวจสอบแนวตั้ง (คอลัมน์) ว่าเรียงลำดับตัวอักษรจากบนลงล่างหรือไม่
    for j in range(cols):
        for i in range(1, rows):
            if sorted_grid[i][j] < sorted_grid[i-1][j]:
                return "NO"
                
    return "YES"