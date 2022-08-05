def trap(height) -> int:
    a = max(height)
    ind = height.index(a)


    result = 0
    h = 0
    for j in range(0,ind):
        if height[j] > h:
            h = height[j]
        water = h - height[j+1]

        if water > 0:
            result += water

    h2 = 0
    for k in range(ind+1,len(height))[::-1]:
        if height[k] > h2:
            h2 = height[k]
        water = h2 - height[k-1]

        if water > 0:
            result += water

    return result

            
heig = [4,2,0,3,2,5]
print(trap(heig))