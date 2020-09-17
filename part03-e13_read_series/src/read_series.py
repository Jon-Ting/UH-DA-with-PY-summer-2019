import pandas as pd


def read_series():
    inp_list, idx_list, val_list = [], [], []
    while True:
        inp = input("Give a Series:")
        inp_list.append(inp)
        if inp == '':
            break
    # print(inp_list)
    for i, line in enumerate(inp_list):
        if line == '':
            break
        print(line.split())
        idx_list.append(line.split()[0])
        val_list.append(line.split()[1])
    return_series = pd.Series(val_list, index=idx_list)
    return return_series

def main():
    print(read_series())

if __name__ == "__main__":
    main()
