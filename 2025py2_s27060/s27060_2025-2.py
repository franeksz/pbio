from Bio import Entrez,SeqIO
import pandas as pd,matplotlib.pyplot as plt
i=input;Entrez.email=i("email: ");Entrez.api_key=i("api-key: ");tx=i("taxid: ");mn,mx=map(int,(i("min len: "),i("max len: ")));mxr=int(i("max rec: "))
s=Entrez.esearch(db="nucleotide",term=f"txid{tx}[Organism]",usehistory="y");d=Entrez.read(s);c=int(d["Count"]);print(c,"records");we,q=d["WebEnv"],d["QueryKey"];r=[];bs=500
for st in range(0,min(c,mxr),bs):
    h=Entrez.efetch(db="nucleotide",rettype="gb",retmode="text",retstart=st,retmax=min(bs,mxr-st),webenv=we,query_key=q)
    r+=[{"acc":x.id,"len":len(x.seq),"desc":x.description}for x in SeqIO.parse(h,"genbank")if mn<=len(x.seq)<=mx]
df=pd.DataFrame(r);df.to_csv(f"taxid_{tx}.csv",index=False)
df=df.sort_values("len",ascending=False)
plt.figure(figsize=(12,6));plt.plot(df["acc"],df["len"],marker='o');plt.xticks(rotation=90,fontsize=8);plt.tight_layout();plt.savefig(f"taxid_{tx}.png")
