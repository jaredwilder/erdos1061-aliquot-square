#!/usr/bin/env python3
"""Exact verifier for ERDOS1061_PRIMITIVE_SEEDS_200K.csv.

Stdlib only. Validates every published row and the rigorous floor-sum lower bound.
This verifies validity of the listed seed bank; it does not claim completeness among all seeds.
"""
import csv
import math
import sys

SCALE = 10**12
EXPECTED_ROWS = 152803
EXPECTED_FLOOR_SUM = 2295492576177
MAX_S = 200000


def require(ok, msg):
    if not ok:
        raise SystemExit("FAIL: " + msg)


def spf_table(n):
    spf = list(range(n + 1))
    if n >= 1:
        spf[1] = 1
    for p in range(2, int(n**0.5) + 1):
        if spf[p] == p:
            for m in range(p * p, n + 1, p):
                if spf[m] == m:
                    spf[m] = p
    return spf


def factor(n, spf):
    out = []
    while n > 1:
        p = spf[n]
        e = 0
        while n % p == 0:
            n //= p
            e += 1
        out.append((p, e))
    return out


def sigma(n, spf):
    z = 1
    for p, e in factor(n, spf):
        z *= (p ** (e + 1) - 1) // (p - 1)
    return z


def phi(n, spf):
    z = n
    for p, _ in factor(n, spf):
        z = z // p * (p - 1)
    return z


def main(path):
    spf = spf_table(MAX_S)
    rows = 0
    floor_sum = 0
    seen = set()
    with open(path, newline="", encoding="utf-8") as f:
        r = csv.DictReader(f)
        expected = [
            "a", "b", "sum_s", "sigma_a", "sigma_b", "sigma_s",
            "M_ab_s", "phi_M", "coeff_num", "coeff_den", "coeff_floor_1e12",
        ]
        require(r.fieldnames == expected, f"header mismatch: {r.fieldnames}")
        for rec in r:
            rows += 1
            x = {k: int(v) for k, v in rec.items()}
            a, b, s = x["a"], x["b"], x["sum_s"]
            require(1 <= a < b, f"row {rows}: ordering")
            require(s == a + b and s <= MAX_S, f"row {rows}: sum/range")
            require(math.gcd(a, b) == 1, f"row {rows}: nonprimitive")
            require((a, b) not in seen, f"row {rows}: duplicate")
            seen.add((a, b))

            sa, sb, ss = sigma(a, spf), sigma(b, spf), sigma(s, spf)
            require(
                (sa, sb, ss) == (x["sigma_a"], x["sigma_b"], x["sigma_s"]),
                f"row {rows}: sigma columns",
            )
            require(sa + sb == ss, f"row {rows}: sigma equation")

            M = a * b * s
            require(x["M_ab_s"] == M, f"row {rows}: M")

            # gcd(a,b)=1 implies a,b,a+b are pairwise coprime.
            ph = phi(a, spf) * phi(b, spf) * phi(s, spf)
            require(x["phi_M"] == ph, f"row {rows}: phi(M)")

            num, den = 2 * ph, M * s
            require(
                x["coeff_num"] == num and x["coeff_den"] == den,
                f"row {rows}: coefficient",
            )
            fl = num * SCALE // den
            require(x["coeff_floor_1e12"] == fl, f"row {rows}: floor")
            floor_sum += fl

    require(rows == EXPECTED_ROWS, f"rows={rows}")
    require(floor_sum == EXPECTED_FLOOR_SUM, f"floor_sum={floor_sum}")
    print("PASS")
    print(f"rows={rows}")
    print(f"floor_sum={floor_sum}")
    print(f"scale={SCALE}")
    print(f"rigorous_base_lower_bound>={floor_sum}/{SCALE}")


if __name__ == "__main__":
    require(
        len(sys.argv) == 2,
        "usage: verify_base_certificate.py ERDOS1061_PRIMITIVE_SEEDS_200K.csv",
    )
    main(sys.argv[1])
