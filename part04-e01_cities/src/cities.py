#!/usr/bin/env python3

import pandas as pd
import numpy as np

def cities():
    pop_list = [643272, 279044, 231853, 223027, 201810]
    area_list = [715.48, 528.03, 689.59, 240.35, 3817.52]
    #col_list = ["Population", "Total area"]
    idx_list = ["Helsinki", "Espoo", "Tampere", "Vantaa", "Oulu"]
    cities_df = pd.DataFrame({"Population": pop_list, "Total area": area_list}, index=idx_list)
    return cities_df
    
def main():
    print(cities())
    
if __name__ == "__main__":
    main()
