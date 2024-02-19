# Format Rupiah
def formatrupiah(uang):
    y = str(uang)
    if len(y) <= 3:
        return "Rp " + y
    else:
        p = y[-3:]
        q = y[:-3]
        while len(q) > 3:
            p = "." + q[-3:] + p
            q = q[:-3]
        return "Rp " + q + p