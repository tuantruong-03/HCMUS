import numpy as np
import sympy as sp


def input_constraints():
    constraints = []
    # Nhập số lượng ràng buộc
    n = int(input())
    
    for i in range(n):
        constraint = input().split()
        a, b, c = map(float, constraint)
        constraints.append((a, b, c))
    
    # Tự động thêm hai phương trình x = 0 và y = 0
    constraints.append((1, 0, 0))  # x = 0
    constraints.append((0, 1, 0))  # y = 0
    # print("Nhập hàm mục tiêu")
    target_function = input().split()
    x, y = map(float, target_function)
    target_function = (x,y)
    return constraints,target_function
def find_intersection_points(constraints):
    intersection_points = []
    for i in range(len(constraints)):
        for j in range(i + 1, len(constraints)):
            # Lấy các hệ số của phương trình đường thẳng
            a1, b1, c1 = constraints[i]
            a2, b2, c2 = constraints[j]
            # Giải hệ phương trình tuyến tính
            det = a1 * b2 - a2 * b1
            if det != 0:
                x = (c1 * b2 - c2 * b1) / det
                y = (a1 * c2 - a2 * c1) / det
                # Kiểm tra xem điểm giao điểm có nằm trong phạm vi không âm không
                if x >= 0 and y >= 0:
                    intersection_points.append((x, y))
    return intersection_points

# Biểu diễn các phương trình đường thẳng dưới dạng ax + by = c

def validated_intersection_points(points, constraints):
    # print(points)
    i = 0
    while i < len(points):
        point = points[i]
        for j in range (len(constraints)-2):
            constraint = constraints[j]
            left = constraint[0]*point[0] + constraint[1]*point[1]
            right = constraint[2]
            if left > float(right):
                points.pop(i)
                i -= 1  # Giảm giá trị của i đi 1 sau khi xóa
                break
        i += 1  # Tăng giá trị của i sau mỗi vòng lặp nếu không xóa phần tử nào
    return points
def standarlize_points(points):
    for i in range(len(points)):
        x, y = points[i]
        if x.is_integer():
            x = int(x)
        if y.is_integer():
            y = int(y)
        points[i] = (x,y)
    return points

def find_max_min(points, target_function):
    # print(target_function)
    values_array = []
    for i in range(len(points)):
        point = points[i]
        value = point[0]*target_function[0] + point[1]*target_function[1]
        values_array.append(value)
    min_index = 0
    max_index = 0
    for i in range(1, len(values_array)):
        if values_array[i] > values_array[max_index]:
            max_index = i
        if values_array[i] < values_array[min_index]:
            min_index = i
    max_value = values_array[max_index]
    x_max = points[max_index][0]
    y_max = points[max_index][1]

    min_value  = values_array[min_index]
    x_min = points[min_index][0]
    y_min = points[min_index][1]

    result = [[max_value, x_max, y_max], [min_value,x_min,y_min]]
    return result

def is_domain_blocked(constraints):
    positive_infinity = float('inf')
    for i in range(len(constraints)-2):
        constraint = constraints[i]
        if positive_infinity*constraint[0] + positive_infinity*constraint[1] > constraint[2]:
            return False
    return True



def main():
    # Nhập ràng buộc và hàm mục tiêu
    constraints, target_function = input_constraints()
    # Tìm tất cả các điểm giao điểm giữa các đường thẳng
    points = find_intersection_points(constraints)
    # Chọn ra các điểm thuộc miền ràng buộc
    points = validated_intersection_points(points, constraints)
    # HÀM PHỤ: chuyển các giá trị như là "5.0" thành "5",... (hàm này không quan trọng)
    points = standarlize_points(points)
    # In danh sách các điểm cực biên
    print("1) Danh sach cac diem cuc bien:")
    for i in  range(len(points)):
        point = points[i]
        end_char = ", "
        if i == len(points) - 1:
            end_char = ".\n"
        print(f"({point[0]};{point[1]})", end=end_char)
    # Giả sử có max, min => Hàm tìm max, min
    result = find_max_min(points,target_function)
    # Kiểm tra miền ràng buộc có bị chặn không
    if is_domain_blocked(constraints) == True:
        print("2) Mien rang buoc bi chan")
        print("3) GTLN khong ton tai")
    else:
        print("2) Mien rang buoc khong bi chan")
        print(f"3) GTLN la F = {result[0][0]} tai x1 = {result[0][1]}, x2 = {result[0][2]}")
    print(f"GTNN la F = {result[1][0]} tai x1 = {result[1][1]}, x2 = {result[1][2]}")


if __name__ == "__main__":
    main()
