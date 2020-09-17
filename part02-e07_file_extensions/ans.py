#!/usr/bin/env python3
 
def file_extensions(filename):
    no_extension=[]
    d = {}
    with open(filename) as f:
        for line in f:
            line=line.strip()
            v = line.split('.')
            if len(v) == 1:
                no_extension.append(line)
            else:
                extension = v[-1]
                if extension not in d:
                    d[extension] = []
                d[extension].append(line)
    return (no_extension, d)
 
def main():
    no_extension, d = file_extensions("src/filenames.txt")
    print(f"{len(no_extension)} files with no extension")
    for extension, files in sorted(d.items()):
        print(f"{extension} {len(files)}")
 
if __name__ == "__main__":
    main()
 
