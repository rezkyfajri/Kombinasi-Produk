import pandas as pd
import json
from mlxtend.frequent_patterns import apriori, association_rules
from mlxtend.preprocessing import TransactionEncoder

class proces():
    def __init__(self):
        self.data = pd.DataFrame()

    def read_data(self,file_data):
        df = pd.read_csv(file_data)
        self.data = df
        df = df.rename(columns={'No.':'no','KOPI KULO':'kopi_kulo','KOPI HITAM':'kopi_hitam','COKELAT KEJU':'cokelat_keju','COKELAT':'cokelat','COOKIES N CREAM':'cookies_n_cream','AVOCATTO VANILLA':'avocatto_vanilla','AVOCATTO CHOCOLATE':'avocatto_chocolate','KOPI BAILEYS ':'kopi_baileys_','LEMON LIME ':'lemon_lime_','HONEY LEMON':'honey_lemon','LEMON YAKULT':'lemon_yakult','ARUNIKA':'arunika','KOPI DIREGALIN':'kopi_diregalin','MATCHA LATTE':'matcha_latte','YAKULT BERRY':'yakult_berry','KOPI BERRY':'kopi_berry','KOPI NAM':'kopi_nam','VICTORY CARAMEL FRAPPE':'victory_caramel_frappe','STRAWBERRY CHEESECAKE':'strawberry_cheesecake','MATCHA KEJU':'matcha_keju','KOPI SPEKULO':'kopi_spekulo','REGALIN ':'regalin_','BLACKFOREST':'blackforest','KULOCADO':'kulocado','KOPI KEJU':'kopi_keju','REVIVE MATCHA CARAMEL':'revive_matcha_caramel','KOPI LATTE':'kopi_latte','KING BISCOFF BLEND':'king_biscoff_blend','DANIKA':'danika','NAYANIKA':'nayanika','MATCHA PURIN':'matcha_purin','SISUKA PURIN':'sisuka_purin','HOJICHA':'hojicha','KOPI KULO 1LT':'kopi_kulo_1lt'})
        json = df.to_dict(orient='records')
        return json

    def train(self,input):
        print(input)
        encoded_transactions_df = self.data.drop(labels=['No.'],axis=1).astype(bool)
        frequent_itemsets = apriori(encoded_transactions_df, min_support=float(input['support']), use_colnames = True)
        rulesdf = association_rules(frequent_itemsets, metric="confidence", min_threshold=float(input['confidence']))
        rulesdf['no'] = rulesdf.index
        rules = rulesdf.to_dict(orient='records')
        return rules