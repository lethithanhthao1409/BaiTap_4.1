def ma_hoa_caesar(van_ban_goc, k):
    ket_qua = ""
    k = k % 26  
    for ky_tu in van_ban_goc:
        if ky_tu.isalpha():  
            co_so = ord('A') if ky_tu.isupper() else ord('a')
            ket_qua += chr((ord(ky_tu) - co_so + k) % 26 + co_so)
        else:
            ket_qua += ky_tu
    return ket_qua


k = 41
van_ban_goc = "Lê Thị Thanh Thảo"
ket_qua = ma_hoa_caesar(van_ban_goc, k)

print("Kết quả trước khi mã hóa :", van_ban_goc)
print("kết quả sau khi đã mã hóa:", ket_qua)

