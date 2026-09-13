#!/usr/bin/env python3
"""Exact verifier for the finite primitive-seed certificate for Erdos #1061.

No floats are used for the certificate. Each row (a,b,s) must satisfy
  gcd(a,b)=1, a<b, s=a+b, sigma(a)+sigma(b)=sigma(s).
For such a primitive seed, every k coprime to M=a*b*s gives ordered solutions
(ka,kb) and (kb,ka). The asymptotic coefficient contributed by that ray is
  2*phi(M)/(M*s).
Rows have distinct primitive ratios, so the rays are disjoint.

The CSV stores floor(10^12 * coefficient) for each row. Summing those floors
is a rigorous lower bound on 10^12 times the total coefficient.
"""
from __future__ import annotations
import csv, math, os, hashlib

HERE = os.path.dirname(os.path.abspath(__file__))
CSV_PATH = os.path.join(HERE, "ERDOS1061_PRIMITIVE_SEEDS_200K.csv")
MAX_S = 200_000
SCALE = 10**12
CLAIMED_FLOOR_SUM = 2_295_492_576_177


def sigma_sieve(n: int) -> list[int]:
    sig = [0] * (n + 1)
    for d in range(1, n + 1):
        for m in range(d, n + 1, d):
            sig[m] += d
    return sig


def phi_sieve(n: int) -> list[int]:
    phi = list(range(n + 1))
    for p in range(2, n + 1):
        if phi[p] == p:
            for m in range(p, n + 1, p):
                phi[m] -= phi[m] // p
    return phi


def main() -> None:
    sig = sigma_sieve(MAX_S)
    phi = phi_sieve(MAX_S)
    seen: set[tuple[int, int]] = set()
    floor_sum = 0
    rows = 0
    with open(CSV_PATH, newline="", encoding="utf-8") as f:
        for rec in csv.DictReader(f):
            rows += 1
            a = int(rec["a"]); b = int(rec["b"]); s = int(rec["sum_s"])
            if not (1 <= a < b and s == a + b and s <= MAX_S):
                raise AssertionError((rows, "domain/sum", a, b, s))
            if math.gcd(a, b) != 1:
                raise AssertionError((rows, "not primitive", a, b))
            if (a, b) in seen:
                raise AssertionError((rows, "duplicate primitive ray", a, b))
            seen.add((a, b))
            if sig[a] + sig[b] != sig[s]:
                raise AssertionError((rows, "sigma equation", a, b, s, sig[a], sig[b], sig[s]))
            if int(rec["sigma_a"]) != sig[a] or int(rec["sigma_b"]) != sig[b] or int(rec["sigma_s"]) != sig[s]:
                raise AssertionError((rows, "stored sigma mismatch"))

            # gcd(a,b)=1 implies a,b,s=a+b are pairwise coprime.
            M = a * b * s
            phiM = phi[a] * phi[b] * phi[s]
            if int(rec["M_ab_s"]) != M or int(rec["phi_M"]) != phiM:
                raise AssertionError((rows, "M/phi mismatch"))
            num = 2 * phiM
            den = M * s
            units = (num * SCALE) // den
            if int(rec["coeff_num"]) != num or int(rec["coeff_den"]) != den or int(rec["coeff_floor_1e12"]) != units:
                raise AssertionError((rows, "coefficient mismatch"))
            floor_sum += units

    if rows != 152_803:
        raise AssertionError(("row count", rows))
    if floor_sum != CLAIMED_FLOOR_SUM:
        raise AssertionError(("floor sum", floor_sum, CLAIMED_FLOOR_SUM))
    if floor_sum <= 2 * SCALE:
        raise AssertionError("coefficient lower bound did not exceed 2")

    h = hashlib.sha256(open(CSV_PATH, "rb").read()).hexdigest()
    print("PASS")
    print(f"rows={rows}")
    print(f"floor_sum={floor_sum}")
    print(f"rigorous_coefficient_lower_bound={floor_sum}/{SCALE}={floor_sum/SCALE:.12f}")
    print(f"csv_sha256={h}")


if __name__ == "__main__":
    main()
