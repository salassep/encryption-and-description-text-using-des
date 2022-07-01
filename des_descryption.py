import math

def convert_hex_to_binary(hex_str):
  hex_str_arr = hex_str.split()

  binary_arr = []
  for x in hex_str_arr:
    res = "{0:08b}".format(int(x, 16))
    binary_arr.append(res) 
  binary_str = ' '.join(binary_arr)
  return binary_str

def initial_permutation_table(binary_str):
  new_binary_str = binary_str.replace(" ", "")
  table_permutation_arr = [58, 50, 42, 34, 26, 18, 10, 2, 60, 52, 44, 36, 28, 20, 12, 4, 62, 54, 46, 38, 30, 22, 14, 6, 64, 56, 48, 40, 32, 24, 16, 8, 57, 49, 41, 33, 25, 17, 9, 1, 59, 51, 43, 35, 27, 19, 11, 3, 61, 53, 45, 37, 29, 21, 13, 5, 63, 55, 47, 39, 31, 23, 15, 7 ]
  ip = []
  for x in table_permutation_arr:
    ip.append(new_binary_str[x-1])
  return ip

def ekspansion_table(ri):
  if type(ri) == str :
    ri = ri.replace(" ", "")
  ekspansion_table_arr = [32, 1, 2, 3, 4, 5, 4, 5, 6, 7, 8, 9, 8, 9, 10, 11, 12, 13, 12, 13, 14, 15, 16, 17, 16, 17, 18, 19, 20, 21, 20, 21, 22, 23, 24, 25, 24, 25, 26, 27, 28, 29, 28, 29, 30, 31, 32, 1]
  e_ri = []
  for x in ekspansion_table_arr:
    e_ri.append(ri[x-1])
  return e_ri

def xor_key_e_ri(e_ri, key):
  new_key_str = key.replace(" ", "")
  e_ri = ''.join(e_ri)

  new_key_int = int(new_key_str, 2)
  e_ri_int = int(e_ri, 2)

  xor_res = new_key_int ^ e_ri_int

  xor_res_str = str("{0:08b}".format(xor_res)).zfill(len(e_ri))

  return xor_res_str

def s_box_table_spliter(xor_res_str):
  xor_res = xor_res_str.replace(" ", "")

  s_1 = s_box_table(0, xor_res[0:6])
  s_2 = s_box_table(1, xor_res[6:12])
  s_3 = s_box_table(2, xor_res[12:18])
  s_4 = s_box_table(3, xor_res[18:24])
  s_5 = s_box_table(4, xor_res[24:30])
  s_6 = s_box_table(5, xor_res[30:36])
  s_7 = s_box_table(6, xor_res[36:42])
  s_8 = s_box_table(7, xor_res[42:48])

  b_i = s_1 +  s_2 + s_3 + s_4 + s_5 + s_6 + s_7 + s_8

  return b_i

def s_box_table(pos, s_i):
  s_table = [
        [
            [14, 4, 13, 1, 2, 15, 11, 8, 3, 10, 6, 12, 5, 9, 0, 7],
            [0, 15, 7, 4, 14, 2, 13, 1, 10, 6, 12, 11, 9, 5, 3, 8],
            [4, 1, 14, 8, 13, 6, 2, 11, 15, 12, 9, 7, 3, 10, 5, 0],
            [15, 12, 8, 2, 4, 9, 1, 7, 5, 11, 3, 14, 10, 0, 6, 13]
        ],
        [
            [15, 1, 8, 14, 6, 11, 3, 4, 9, 7, 2, 13, 12, 0, 5, 10],
            [3, 13, 4, 7, 15, 2, 8, 14, 12, 0, 1, 10, 6, 9, 11, 5],
            [0, 14, 7, 11, 10, 4, 13, 1, 5, 8, 12, 6, 9, 3, 2, 15],
            [13, 8, 10, 1, 3, 15, 4, 2, 11, 6, 7, 12, 0, 5, 14, 9],
        ],
        [
            [10, 0, 9, 14, 6, 3, 15, 5, 1, 13, 12, 7, 11, 4, 2, 8],
            [13, 7, 0, 9, 3, 4, 6, 10, 2, 8, 5, 14, 12, 11, 15, 1],
            [13, 6, 4, 9, 8, 15, 3, 0, 11, 1, 2, 12, 5, 10, 14, 7],
            [1, 10, 13, 0, 6, 9, 8, 7, 4, 15, 14, 3, 11, 5, 2, 12],
        ],
        [
            [7, 13, 14, 3, 0, 6, 9, 10, 1, 2, 8, 5, 11, 12, 4, 15],
            [13, 8, 11, 5, 6, 15, 0, 3, 4, 7, 2, 12, 1, 10, 14, 9],
            [10, 6, 9, 0, 12, 11, 7, 13, 15, 1, 3, 14, 5, 2, 8, 4],
            [3, 15, 0, 6, 10, 1, 13, 8, 9, 4, 5, 11, 12, 7, 2, 14],
        ],
        [
            [2, 12, 4, 1, 7, 10, 11, 6, 8, 5, 3, 15, 13, 0, 14, 9],
            [14, 11, 2, 12, 4, 7, 13, 1, 5, 0, 15, 10, 3, 9, 8, 6],
            [4, 2, 1, 11, 10, 13, 7, 8, 15, 9, 12, 5, 6, 3, 0, 14],
            [11, 8, 12, 7, 1, 14, 2, 13, 6, 15, 0, 9, 10, 4, 5, 3],
        ],
        [
            [12, 1, 10, 15, 9, 2, 6, 8, 0, 13, 3, 4, 14, 7, 5, 11],
            [10, 15, 4, 2, 7, 12, 9, 5, 6, 1, 13, 14, 0, 11, 3, 8],
            [9, 14, 15, 5, 2, 8, 12, 3, 7, 0, 4, 10, 1, 13, 11, 6],
            [4, 3, 2, 12, 9, 5, 15, 10, 11, 14, 1, 7, 6, 0, 8, 13],
        ],
        [
            [4, 11, 2, 14, 15, 0, 8, 13, 3, 12, 9, 7, 5, 10, 6, 1],
            [13, 0, 11, 7, 4, 9, 1, 10, 14, 3, 5, 12, 2, 15, 8, 6],
            [1, 4, 11, 13, 12, 3, 7, 14, 10, 15, 6, 8, 0, 5, 9, 2],
            [6, 11, 13, 8, 1, 4, 10, 7, 9, 5, 0, 15, 14, 2, 3, 12],
        ],
        [
            [13, 2, 8, 4, 6, 15, 11, 1, 10, 9, 3, 14, 5, 0, 12, 7],
            [1, 15, 13, 8, 10, 3, 7, 4, 12, 5, 6, 11, 0, 14, 9, 2],
            [7, 11, 4, 1, 9, 12, 14, 2, 0, 6, 10, 13, 15, 3, 5, 8],
            [2, 1, 14, 7, 4, 10, 8, 13, 15, 12, 9, 0, 3, 5, 6, 11],
        ]
    ]

  i = int(s_i[0] + s_i[-1], 2)
  j = int(s_i[1:-1], 2)
  s_res = bin(s_table[pos][i][j])[2:].zfill(4)

  print("S", pos + 1, " = ", s_i, sep='')
  print("start end digit = ", s_i[0],s_i[len(s_i)-1], sep='')
  print("digit between = ", s_i[1:len(s_i)-1])
  print("S", pos + 1, " Result = ", s_table[pos][i][j], " = ", s_res , sep='')
  print("")

  return s_res

def p_box_permutation(b_i):
  p_box_arr = [16, 7, 20, 21, 29, 12, 28, 17, 1, 15, 23, 26, 5, 18, 31, 10, 2, 8, 24, 14, 32, 27, 3, 9, 19, 13, 30, 6, 22, 11, 4, 25]
  p_bi = []

  for x in p_box_arr:
    p_bi.append(b_i[x-1])

  return p_bi



hex_str = input("Input your hexa with space as separator (if you have done the conversion to binary, please n for skip this step & s for iteration 2 and so on): ")

if hex_str == 'n':
  binary_str = input("Input your binary for initial permutation : ")
  key = input("Input your binary key : ")
  li_for_xor = input("Input your binary li for last xor operation : ")

  ip_res = initial_permutation_table(binary_str)
  li = ip_res[:32]
  ri = ip_res[32:]
  print("\nInitial Permutation Phase : ")
  print("IP(X) = ", ''.join(ip_res))
  print("L0 = ", ''.join(li))
  print("R0 = ", ''.join(ri))

  expansion_res = ekspansion_table(ri)
  print("\nExpansion Phase : ")
  print("E(Ri) = ", ''.join(expansion_res))

  xor_res = xor_key_e_ri(expansion_res, key)
  print("\nXOR BETWEEN E(Ri) and The Key Phase : ")
  print("E(Ri) = ", ''.join(expansion_res))
  print("Your key = ", key)
  print("XOR Result = ", xor_res)

  print("\nS-Box Phase : ")
  sbox_res = s_box_table_spliter(xor_res)
  print("B(i) = ", sbox_res)

  print("\nP-Box Permutation Phase : ")
  pbox_res = p_box_permutation(sbox_res)
  print("P(Bi) = ", ''.join(pbox_res))

  print("\nLast XOR Phase : ")
  ri_res = xor_key_e_ri(pbox_res, li_for_xor)
  print("R(i) = ", ri_res)

elif hex_str == 's':
  binary_str = input("Input your binary for expansion permutation : ")
  key = input("Input your binary key : ")
  li_for_xor = input("Input your binary li for last xor operation: ")

  expansion_res = ekspansion_table(binary_str)
  print("\nExpansion Phase : ")
  print("E(Ri) = ", ''.join(expansion_res))

  xor_res = xor_key_e_ri(expansion_res, key)
  print("\nXOR BETWEEN E(Ri) and The Key Phase : ")
  print("E(Ri) = ", ''.join(expansion_res))
  print("Your key = ", key)
  print("XOR Result = ", xor_res)

  print("\nS-Box Phase : ")
  sbox_res = s_box_table_spliter(xor_res)
  print("B(i) = ", sbox_res)

  print("\nP-Box Permutation Phase : ")
  pbox_res = p_box_permutation(sbox_res)
  print("P(Bi) = ", ''.join(pbox_res))

  print("\nLast XOR Phase : ")
  ri_res = xor_key_e_ri(pbox_res, li_for_xor)
  print("R(i) = ", ri_res)
  
else :
  hex_str = input("Input your hexadecimal with space : ")
  key = input("Input your binary key : ")
  li_for_xor = input("Input your binary li for last xor operation : ")

  binary_str = convert_hex_to_binary(hex_str)
  print("\nHex Converted =", binary_str)

  ip_res = initial_permutation_table(binary_str)
  li = ip_res[:32]
  ri = ip_res[32:]
  print("\nInitial Permutation Phase : ")
  print("IP(X) = ", ''.join(ip_res))
  print("L0 = ", ''.join(li))
  print("R0 = ", ''.join(ri))

  expansion_res = ekspansion_table(ri)
  print("\nExpansion Phase : ")
  print("E(Ri) = ", ''.join(expansion_res))

  xor_res = xor_key_e_ri(expansion_res, key)
  print("\nXOR BETWEEN E(Ri) and The Key Phase : ")
  print("E(Ri) = ", ''.join(expansion_res))
  print("Your key = ", key)
  print("XOR Result = ", xor_res)

  print("\nS-Box Phase : ")
  sbox_res = s_box_table_spliter(xor_res)
  print("B(i) = ", sbox_res)

  print("\nP-Box Permutation Phase : ")
  pbox_res = p_box_permutation(sbox_res)
  print("P(Bi) = ", ''.join(pbox_res))

  print("\nLast XOR Phase : ")
  ri_res = xor_key_e_ri(pbox_res, li_for_xor)
  print("R(i) = ", ri_res)


