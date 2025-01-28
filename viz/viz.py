from pathlib import Path
import pandas as pd

chemin = Path("SuperHero")/"bdd"/"df_movie.parquet"
bdd = pd.read_parquet(chemin) # "dossier/sous-dossier/fichier.txt" sur Linux, "dossier\sous-dossier\fichier.txt" sur Windows
print(bdd.head())