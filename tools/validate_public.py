"""Public text and link consistency checks. Not a confidentiality guarantee."""
from pathlib import Path
import re
root=Path(__file__).resolve().parents[1]
paths=list(root.rglob("*.md"))
assert len(paths)>=7
for p in paths:
    content=p.read_text(encoding="utf-8")
    for u in re.findall(r"\]\(([^)]+)\)",content):
        if u.startswith(("https://","http://","mailto:","#")):
            continue
        assert (p.parent/u.split("#")[0]).exists(), f"Broken link: {p.relative_to(root)} {u}"
    forbidden=[r"\btwo[- ]print\b",r"\bmulti[- ]print\b",r"\bconduct\s*/\s*experience\b",r"\bTissue\b",r"\bMorph(ic|ological) Memory\b",r"\bscar[s]?\b",r"\bepoch[s]?\b",r"\bMAI[-0-9]+\b",r"\bNO_GO_NATIVE\b"]
    for pattern in forbidden:
        assert not re.search(pattern,content,re.I), f"Proprietary detail or internal outcome label in {p.relative_to(root)}: {pattern}"
print(f"PUBLIC_TEXT_LINK_CHECK_PASS: {len(paths)} Markdown documents; manual IP/legal review still required")
