from interest import compound_interest, simple_interest
from display import print_result

def main():
    print("=== Program Kalkulator Bunga Tabungan ===")
    principal = float(input("Masukkan saldo awal (contoh:80000): "))
    rate = float(input("Masukkan bunga tahunan (misal 5% → 0.05): "))
    years = int(input("Masukkan lama menabung (tahun): "))

    ci_result = compound_interest(principal, rate, years)
    si_result = simple_interest(principal, rate, years)

    print_result(principal, rate, years, ci_result, si_result)

if __name__ == "__main__":
    main()