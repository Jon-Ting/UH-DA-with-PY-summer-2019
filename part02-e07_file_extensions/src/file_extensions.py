#!/usr/bin/env python3

def file_extensions(filename):
    no_ext_list, ext_dict = [], {}
    with open(filename, "r") as f:
        for i, line in enumerate(f.readlines()):
            if "." not in line:
                no_ext_list.append(line.strip("\n"))
            else:
                ext = line.split(".")[-1].strip("\n")
                if ext in ext_dict:
                    ext_dict[ext].append(line.strip("\n"))
                else:
                    ext_dict[ext] = [line.strip("\n")]
    return (no_ext_list, ext_dict)

def main():
    (no_ext_list, ext_dict) = file_extensions("src/filenames.txt")
    print("{0} files with no extension".format(len(no_ext_list)))
    key_list = []
    for key in ext_dict.keys():
        key_list.append(key)
    key_list = sorted(key_list)
    for key in key_list:
        print("{0} {1}".format(key, len(ext_dict[key])))

if __name__ == "__main__":
    main()
