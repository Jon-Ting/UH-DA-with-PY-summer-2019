#!/usr/bin/env python3

def detect_ranges(L):
    return_list = [sorted(L)[0]]
    is_start = False
    for i, number in enumerate(sorted(L)):
        if i == 0:
            continue
        elif i == len(L)-1:
            prev_num = sorted(L)[i-1]
            if number == prev_num + 1:
                if is_start:
                    end = number + 1
                    return_list[-1] = (start,end)
                else:
                    start = prev_num
                    end = number + 1
                    return_list[-1] = (start,end)
            else:
                if is_start:
                    end = prev_num + 1
                    return_list[-1] = (start,end)
                    return_list.append(number)
                else:
                    return_list.append(number)
        else:  # From 2nd elements onward
            prev_num = sorted(L)[i-1]
            if number == prev_num + 1:
                if not is_start:
                    start = prev_num
                    is_start = True
                else:
                    continue
            else:
                if is_start:
                    end = prev_num + 1
                    return_list[-1] = (start,end)
                    return_list.append(number)
                    is_start = False
                else:
                    return_list.append(number)
    return return_list

def main():
    L = [2, 5, 4, 8, 12, 6, 7, 10, 13]
    L = [89, -26, 43, -77, -76, 86, 87, -8, -71, -34]
    result = detect_ranges(L)
    print(L)
    print(result)

if __name__ == "__main__":
    main()
