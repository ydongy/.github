<!-- template: legal.md v1 -->
<!-- docs/legal.md. See handbook/guides/legal.md. -->
# Legal pages: one source per fact

## Where each thing lives

| Thing | Where |
|---|---|
| Terms of service | `https://<domain>/terms`; for a closed product the same English text is `LICENSE`, for an MIT project `LICENSE` is the MIT text |
| Privacy policy | `https://<domain>/privacy` |
| Refund policy | `https://<domain>/refund` |

## Facts that must match the code

| Fact | Code | Website key | Check |
|---|---|---|---|
| <fact as stated> | `<symbol or file>` | `<i18n key>` | `check_facts.py` |

## Refund policy

<The rules in one paragraph; the website text derives from this.>
