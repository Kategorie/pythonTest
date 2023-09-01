rng_mx = 0
rng_mn = 0
tmp_L = []
tmp_t = []
for i in range(5):
    tmp_l = list(input())
    tmp_t.append(len(tmp_l))
    tmp_L.append(tmp_l)

rng_mx = max(tmp_t)
rng_mn = min(tmp_t)
for ii in range(rng_mx):
    for iii in range(len(tmp_L)):
        if tmp_L[iii] == '*':
            continue
        else:
            print(tmp_L[iii][ii], end="")
            if len(tmp_L[iii]) == rng_mn and rng_mn == ii+1:
                if len(tmp_L) == 1:
                    continue
                else:
                    tmp_L[iii] = '*'
                    tmp_t.remove(rng_mn)
                    if not tmp_t:
                        continue
                    else:
                        rng_mn = min(tmp_t)
                