# %% [markdown]
# # Functions for all statistic informations of seasons 

# %% [markdown]
# ### Average points of teams per season

# %%
def avg_Points():
    %store -r allSeasons
    %store -r df_allSeasons
    %store -r sheet_names
    %store -r dict_df
    %store -r teamsAll
    avg_PTS = []
    pocetZapasu = 30 * 82
    for season in sheet_names:        
            seasonList = dict_df.get(season)
            soucet = seasonList['PTS'].sum()            
            prumer = round((soucet/pocetZapasu),2)
            soucet = 0
            avg_PTS.append(prumer)
    df_allSeasons['AVGPTS'] = avg_PTS
    print(df_allSeasons)
avg_Points()  

# %% [markdown]
# ### Average players age per season

# %%
def avg_age():
    %store -r allSeasons
    %store -r df_allSeasons
    %store -r sheet_names
    %store -r dict_df
    %store -r teamsAll
    avg_age = []
    for index in sheet_names:         
        seasonList = dict_df.get(index)
        celkovyVek = 0
        pocetHracu = len(seasonList)
        celkovyVek += seasonList['AGE'].sum();
        prumer = round(celkovyVek/pocetHracu, 2)        
        avg_age.append(prumer)
    df_allSeasons['AGE'] = avg_age
avg_age()
print(df_allSeasons)
    

# %% [markdown]
# ### Max points of teams per season

# %%
def max_points():
    %store -r allSeasons
    %store -r df_allSeasons
    %store -r sheet_names
    %store -r dict_df
    %store -r teamsAll
    max_PTS = []
    for index in sheet_names:
        seasonList = dict_df.get(index)
        maxPTS = seasonList['PTS'].max()
        max_PTS.append(maxPTS)
    df_allSeasons['MAXPTS'] = max_PTS
max_points()
print(df_allSeasons)
    

# %% [markdown]
# ### Max played minutes per season

# %%
def max_minutes():
    %store -r allSeasons
    %store -r df_allSeasons
    %store -r sheet_names
    %store -r dict_df
    %store -r teamsAll
    max_MIN = []
    for index in sheet_names:
        seasonList = dict_df.get(index)
        maxMIN = seasonList['MIN'].max()
        max_MIN.append(maxMIN)
    df_allSeasons['MAXMIN'] = max_MIN
max_minutes()
print(df_allSeasons)


