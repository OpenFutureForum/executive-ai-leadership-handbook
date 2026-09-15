from pathlib import Path
import re, sys
root=Path(__file__).resolve().parents[1]
pages=list((root/"handbook").rglob("*.md"))
errors=[]
if len(pages)!=75: errors.append(f"expected 75 pages, found {len(pages)}")
titles=[]
for p in pages:
 t=p.read_text()
 h=re.findall(r"^# (.+)$",t,re.M)
 if len(h)!=1: errors.append(f"{p}: expected one H1")
 else: titles.append(h[0])
 if len(t.split())<300: errors.append(f"{p}: under 300 words")
 if "murray.newlands@gmail.com" in t.lower(): errors.append(f"{p}: personal email")
 if "OFF Research and Video Map" in t: errors.append(f"{p}: private map reference")
if len(titles)!=len(set(titles)): errors.append("duplicate H1 titles")
summary=(root/"SUMMARY.md").read_text()
if summary.count("](handbook/")!=75: errors.append("SUMMARY does not contain 75 page links")
if errors:
 print("\n".join(errors)); sys.exit(1)
print(f"Validated {len(pages)} handbook pages; privacy and structure checks passed.")
