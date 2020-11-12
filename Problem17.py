# 1'den 5'e kadar olan rakamlar kelimelerle yazılırsa one,two,three,four,five o zaman toplamda 3+3+5+4+4=19
# Buna göre eğer 1'den 1000'e(dahil) tüm sayılar kelimelerle yazılmış olsaydı kaç harf kullanılırdı?

ONES = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine",
        "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
TENS = ["", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]

def compute():
    ans = sum(len(to_english(i)) for i in range(1, 1001))
    return str(ans)


def to_english(n):
    if 0 <= n < 20:
        return ONES[n]
    elif 20 <= n < 100:
        return TENS[n // 10] + (ONES[n % 10] if (n % 10 != 0) else "")
    elif 100 <= n < 1000:
        return ONES[n // 100] + "hundred" + (("and" + to_english(n % 100)) if (n % 100 != 0) else "")
    elif 1000 <= n < 1000000:
        return to_english(n // 1000) + "thousand" + (to_english(n % 1000) if (n % 1000 != 0) else "")
    else:
        raise ValueError()
        



if __name__ == "__main__":
    print(compute())
