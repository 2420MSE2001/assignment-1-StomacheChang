# main.py

def right_side(x):
    """
    计算方程右侧的固定值。
    """
    result = (1+2*x)/(1+x+x**2)
    return result

def find_num_terms(x, tolerance=1e-6):
    """
    寻找满足左侧与右侧差异小于容差的最小项数。
    """
    right=right_side(x)
    n = 0
    left=(1-2*x)/(1-x+x**2)
    while (abs(right-left)>=tolerance):
        n += 1
        left += ((2**n)*(x**(2**n-1))-(2**(n+1))*(x**(2**(n+1)-1)))/(1-x**(2**n)+x**(2**(n+1)))
    return n+1

if __name__ == "__main__":
    x = 0.25  # 题目给定的 x 值
    num_terms = find_num_terms(x)
    print(f"所需最小项数: {num_terms}")
