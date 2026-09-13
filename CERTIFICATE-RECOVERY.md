# Erdős #1061 primitive-seed certificate — recovery manifest

The #1061 mathematical result, verifier and replay receipt are public. One large exact certificate object is still missing from the branch-visible release:

```text
ERDOS1061_PRIMITIVE_SEEDS_200K.csv
```

Known identity:

- bytes: **17,026,297**;
- SHA-256:

```text
343b12fceb642d15b898f1a4bbbd9018b4a4301c0e72ac46ba30f559358e1a68
```

The release-day accounting records **152,803 primitive-seed rows** in this certificate.

## Authority boundary

The absence of this CSV does **not** erase the already-public theorem/verifier work, but it does mean the complete finite certificate estate has not yet been transported.

When recovered, the file must hash exactly to the identity above before being accepted under that filename. A byte-different object should be versioned separately rather than silently substituted.

**Current status:** result public; large certificate bytes pending recovery/transport.
