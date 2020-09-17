#!/usr/bin/env python3
 
import pandas as pd
 
def suicide_fractions():
    df = pd.read_csv("src/who_suicide_statistics.csv")
    df["Suicide fraction"] = df["suicides_no"] / df["population"]
    result = df.groupby("country").mean()
    return result["Suicide fraction"]
 
def info(df, name):
    print("\n%s" % name)
    print("=" * len(name))
    print("Shape:", df.shape)
    print("dtypes:\n", df.dtypes)
    if isinstance(df, pd.DataFrame):
        print("column names:", df.columns)
    print(df.head())
    
def suicide_weather():
    suicide = suicide_fractions()
    version = list(map(int, pd.__version__.split(".")))   # Get version of Pandas
    # older Pandas versions don't support displayed_only option 
    if version[0] == 0 and version[1] < 23:   
        tables = pd.read_html("src/List_of_countries_by_average_yearly_temperature.html",
                              header=0, index_col=0)
    else:
        tables = pd.read_html("src/List_of_countries_by_average_yearly_temperature.html",
                              header=0, index_col=0, displayed_only=False)
    
    temperature = tables[1]    # The first table is a non-displayed one, we don't want that
    temperature = pd.to_numeric(temperature.iloc[:, 0].str.replace("\u2212", "-"))
    #info(suicide, "Suicide fractions")
    #info(temperature, "Temperatures")
    corr = suicide.corr(temperature, method="spearman")
    if version[0] == 0 and version[1] < 23:   # older Pandas versions don't support sort option
        common = pd.concat([suicide, temperature], axis=1, join="inner")
    else:
        common = pd.concat([suicide, temperature], axis=1, join="inner", sort=False)
    return (suicide.shape[0], temperature.shape[0], common.shape[0], corr)
 
def main():
    suicide_n, temperature_n, common_n, corr = suicide_weather()
    print(f"Suicide DataFrame has {suicide_n} rows")
    print(f"Temperature DataFrame has {temperature_n} rows")
    print(f"Common DataFrame has {common_n} rows")
    print(f"Spearman correlation: {corr:.1f}")
 
if __name__ == "__main__":
    main()
 
