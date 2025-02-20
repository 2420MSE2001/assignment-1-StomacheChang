def calculate_S(x:list,a:list,xn:float,n:int)->float:
    S = 0
    for k in range(n):
        l = 1
        for j in range(n):
            if k != j:
                l *= (xn - x[j]) / (x[k] - x[j])
        S += l * a[k]
    return S

if __name__ == "__main__":
    print("=== 拉格朗日插值计算器 ===")
    # 获取用户输入
    n = int(input("请输入项数n: "))
    x,a=[],[]
    for i in range(n):
        a.append(float(input(f"请输入已知点{i}的函数值x坐标 x{i}: ")))
        x.append(float(input(f"请输入已知点{i}的x坐标 a{i}: ")))   

    xn = float(input("请输入需要插值的x坐标 x : "))
    
    # 计算并输出结果

    S = calculate_S(x,a,xn,n)
    print(f"\n插值结果 S({xn}) = {S:.4f}")
    