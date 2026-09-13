#!/usr/bin/env python3
"""Replay the finite r(N) <= tau(N) counterexample census for Erdős #1061."""

LIMIT = 400

sigma = [0] * (LIMIT + 1)
tau = [0] * (LIMIT + 1)
for d in range(1, LIMIT + 1):
    for m in range(d, LIMIT + 1, d):
        sigma[m] += d
        tau[m] += 1

failures = []
rvals = {}
for N in range(3, LIMIT + 1):
    rN = sum(1 for a in range(1, N)
             if sigma[a] + sigma[N - a] == sigma[N])
    rvals[N] = rN
    if rN > tau[N]:
        failures.append((N, rN, tau[N]))

expected = [
    (123, 6, 4),
    (141, 6, 4),
    (183, 8, 4),
    (249, 6, 4),
    (279, 8, 6),
    (303, 6, 4),
    (309, 6, 4),
    (393, 10, 4),
]
assert failures == expected, (failures, expected)
assert rvals[123] == 6
assert rvals[393] == 10

pairs123 = [(a, 123 - a) for a in range(1, 123)
            if sigma[a] + sigma[123 - a] == sigma[123]]
assert pairs123 == [(38, 85), (41, 82), (46, 77),
                    (77, 46), (82, 41), (85, 38)]

print('PASS')
print('failures:', failures)
print('ordered pairs at N=123:', pairs123)
