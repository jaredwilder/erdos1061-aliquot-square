# Erdős #1061 primitive-seed certificate receipt

Public extraction rerun: **2026-09-11**

Recovered Library artifact:

```text
name=ERDOS1061_PRIMITIVE_SEEDS_200K.csv
bytes=17026297
sha256=343b12fceb642d15b898f1a4bbbd9018b4a4301c0e72ac46ba30f559358e1a68
```

Recovered verifier:

```text
ERDOS1061_SEED_CERT_VERIFY.py
```

Fresh rerun from the recovered bytes:

```text
PASS
rows=152803
floor_sum=2295492576177
rigorous_coefficient_lower_bound=2295492576177/1000000000000=2.295492576177
csv_sha256=343b12fceb642d15b898f1a4bbbd9018b4a4301c0e72ac46ba30f559358e1a68
```

The CSV is therefore pinned byte-for-byte even where the current connector cannot stream a
17,026,297-byte Library payload directly into GitHub. Any later copy claiming to be the original
certificate must match the SHA-256 above before use.

The historical end-to-end release package containing the certificate was recorded as:

```text
ERDOS_CAMPAIGN_END_TO_END_FULL_RELEASE_2026-09-02.zip
bytes=28744585
sha256=caf640969671b6260e33ff5b4ec48c20290c89dbf004f16c89b80ec7c324fdb0
files_in_release=49
```

This receipt certifies the recovered base certificate only. The separate 43-row aliquot-square
generator certificate is described in the directory README at its source-audited status.
