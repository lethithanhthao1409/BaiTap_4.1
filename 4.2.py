def ma_hoa_caesar(ban_ro, khoa):
    ban_ma = ""
    khoa = khoa % 26  
    for ky_tu in ban_ro:
        if ky_tu.isalpha(): 
            if ky_tu.islower(): 
                c = (ord(ky_tu) - ord('a') + khoa) % 26 + ord('a')
                ban_ma += chr(c)
            else:  
                c = (ord(ky_tu) - ord('A') + khoa) % 26 + ord('A')
                ban_ma += chr(c)
        else:
            ban_ma += ky_tu
    return ban_ma

# Văn bản cần mã hóa
ban_ro = "LeThiThanhThao"
khoa = 41
ban_ma = ma_hoa_caesar(ban_ro, khoa)

print("Bản rõ    :", ban_ro)
print("Khóa      :", khoa)
print("Bản mã    :", ban_ma)
