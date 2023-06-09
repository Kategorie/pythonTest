class id:
    idname = ''
    wn = '??!'

    def inp(chr):
        id.idname = chr
        if id.idname == chr:
            return print(f"{id.idname+id.wn}")
        else:
            return print(f"name isn't exist.")
        
if __name__ == '__main__':
    iddd = id
    inchar = input()
    iddd.inp(inchar)
