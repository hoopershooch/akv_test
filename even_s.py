def calc_sum(array2d,x,y):
    arr_height = len(array2d)
    arr_widths = [len(arr) for arr in array2d]
    if y < 0 or y > arr_height-1:
        raise IndexError(
            f"Y={y} coordinate is out of range(0-{arr_height-1})!"
        )
    if x<0 or x > arr_widths[y]-1:
        raise IndexError(
            f"X={x} coordinate is out of range(0-{arr_widths[y]-1})!"
        )

    visited_sites = set()
    mysum=0
    def spawn_from(arr,r,c):
        nonlocal mysum, visited_sites
        if arr[r][c] % 2 == 0 and (r,c) not in visited_sites:
            mysum+=arr[r][c]
            visited_sites.add((r,c))
            if c-1 >= 0:
                spawn_from(arr,r,c-1)
            if r-1 >= 0:
                spawn_from(arr,r-1,c)
            if c < len(arr[r])-1:
                spawn_from(arr,r,c+1)
            if r < len(arr)-1:
                spawn_from(arr,r+1,c)
   
    spawn_from(array2d,x,y)        
    return mysum



if __name__=="__main__":
    arr = [
        [4,2,2,2,2],
        [2,1,1,1,2],
        [2,1,6,1,2],
        [2,1,1,1,2],
        [2,1,2,1,2],
        [2,2,2,2,2]
    ]
    x = 0
    y = 1
    print(
        f"Sum = {calc_sum(arr, x, y)} initial row = {x} initial col = {y}"
    )
  

