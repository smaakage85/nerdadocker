print("Downloading ressources")
# download 'punkt' and DaNE data (FIX!)
import nltk
nltk.download('punkt')
from NERDA.datasets import download_dane_data
download_dane_data()

# download ELECTRA DA
from NERDA.precooked import DA_ELECTRA_DA
model = DA_ELECTRA_DA()
model.download_network()
