# %% [markdown]
# # Functions for all statistic informations of players

# %% [markdown]
# ### Function for counting of average win / lose of every player for 25 seasons

# %%
from openpyxl import load_workbook

def number_W_L_all_time():
    %store -r teamsAll
    %store -r df_teams
    %store -r sheet_names
    %store -r dict_df
    %store -r allPlayers
    %store -r df_allPlayers
    
    stats_W = []
    stats_L = []   
    for player in allPlayers:
        vyher = 0
        pocetZapasu = 0 
        for season in sheet_names:
            seasonList = dict_df.get(season)
            vyher += seasonList.loc[seasonList['PLAYER'] == player, 'W'].sum()
            pocetZapasu += seasonList.loc[seasonList['PLAYER'] == player, 'GP'].sum()
        vyher = round((vyher/pocetZapasu)*100,2)
        proher = round(100 - vyher,2)
        stats_W.append(vyher)
        stats_L.append(proher)
    df_allPlayers['W'] = stats_W
    df_allPlayers['L'] = stats_L
number_W_L_all_time()
print(df_allPlayers)

# %% [markdown]
# ### Function for counting of average field goals of every player for 25 seasons 

# %%
def succ_field_goals():  
    stats_USP = [] 
    for player in allPlayers:
        pocetUspesnych = 0
        celkovyPocet = 0
        for season in sheet_names:
            seasonList = dict_df.get(season)
            celkovyPocet += seasonList.loc[seasonList['PLAYER'] == player, 'FGA'].sum()
            pocetUspesnych += seasonList.loc[seasonList['PLAYER'] == player, 'FGM'].sum()
        if (celkovyPocet > 0):
            uspesnost = round((pocetUspesnych/celkovyPocet)*100,2)
            stats_USP.append(uspesnost)
        else: 
            stats_USP.append(0)        
    df_allPlayers['FGM'] = stats_USP
succ_field_goals()
print(df_allPlayers)

# %% [markdown]
# ### Function for counting of average of 3 point shoots of every player for 25 seasons

# %%
def succ_three_goals():  
    stats_USP = []  
    for player in allPlayers:
        celkovyPocet = 0
        pocetUspesnych = 0
        for season in sheet_names:
            seasonList = dict_df.get(season)
            celkovyPocet += seasonList.loc[seasonList['PLAYER'] == player, '3PA'].sum()
            pocetUspesnych += seasonList.loc[seasonList['PLAYER'] == player, '3PM'].sum()
        if (celkovyPocet > 0 ):            
            uspesnost = round((pocetUspesnych/celkovyPocet)*100,2)
            stats_USP.append(uspesnost)
        else:
            stats_USP.append(0)
    df_allPlayers['3PM'] = stats_USP
succ_three_goals()
print(df_allPlayers)
    

# %% [markdown]
# ### Function for counting of average free throws of every player for 25 seasons

# %%
def succ_free_throws(): 
    stats_USP = []  
    for player in allPlayers:
        celkovyPocet = 0
        pocetUspesnych = 0
        for season in sheet_names:
            seasonList = dict_df.get(season)
            celkovyPocet += seasonList.loc[seasonList['PLAYER'] == player, 'FTA'].sum()
            pocetUspesnych += seasonList.loc[seasonList['PLAYER'] == player, 'FTM'].sum()
        if (celkovyPocet > 0):
            uspesnost = round((pocetUspesnych/celkovyPocet)*100,2)
            stats_USP.append(uspesnost)
        else: 
            stats_USP.append(0)  
    df_allPlayers['FTM'] = stats_USP      
succ_free_throws()
print(df_allPlayers)


# %% [markdown]
# ### Function for counting of average assists of every player for 25 seasons

# %%
def avg_assists(): 
    stats_AST = [] 
    for player in allPlayers:
        pocetAST = 0
        pocetZapasu = 0
        for season in sheet_names:
            seasonList = dict_df.get(season)
            pocetAST += seasonList.loc[seasonList['PLAYER'] == player, 'AST'].sum()
            pocetZapasu += seasonList.loc[seasonList['PLAYER'] == player, 'GP'].sum()
        if (pocetZapasu > 0 ):
            prumerAST = round((pocetAST/pocetZapasu),2)
            stats_AST.append(prumerAST)
        else: 
            stats_AST.append(0)
    df_allPlayers['AST'] = stats_AST
avg_assists()
print(df_allPlayers)   

# %% [markdown]
# ### Function for counting of average rebounds of every player for 25 seasons

# %%
def avg_rebounds():
    stats_REB = []
    stats_OREB = []
    stats_DREB = []
    for player in allPlayers:
        pocetDoskoku = 0
        pocetZapasu = 0
        pocetOfDoskoku = 0
        for season in sheet_names:
            seasonList = dict_df.get(season)
            pocetDoskoku += seasonList.loc[seasonList['PLAYER'] == player, 'REB'].sum()
            pocetOfDoskoku += seasonList.loc[seasonList['PLAYER'] == player, 'OREB'].sum()
            pocetZapasu += seasonList.loc[seasonList['PLAYER'] == player, 'GP'].sum()
        if (pocetZapasu > 0):
            prumer = round((pocetDoskoku/pocetZapasu),2)
            prumerOf = round((pocetOfDoskoku/pocetZapasu),2)
            stats_REB.append(prumer)
            stats_OREB.append(prumerOf)
            stats_DREB.append(prumer-prumerOf)
        else:
            stats_REB.append(0)
            stats_OREB.append(0)
            stats_DREB.append(0)            
    df_allPlayers['REB'] = stats_REB
    df_allPlayers['OREB'] = stats_OREB
    df_allPlayers['DREB'] = stats_DREB
avg_rebounds()
print(df_allPlayers)
            

# %% [markdown]
# ### Function for counting of average points of every player for 25 seasons

# %%
def sum_point_all_players():
    stats_POINTS = []   
    for player in allPlayers:
        soucet = 0
        pocet = 0
        for season in sheet_names:
            seasonList = dict_df.get(season)
            soucet += seasonList.loc[seasonList['PLAYER'] == player, 'PTS'].sum()
            pocet += seasonList.loc[seasonList['PLAYER'] == player, 'GP'].sum()
        if (pocet > 0): 
            prumer = soucet.item()/pocet.item()
            prumer = round(prumer,2)
            stats_POINTS.append(prumer)
        else:
            stats_POINTS.append(0)
    df_allPlayers['PTS']= stats_POINTS
sum_point_all_players()
print(df_allPlayers)
            

# %% [markdown]
# ### Function for counting of average steals of every player for 25 seasons

# %%
def avg_steals():
    stats_STL = []
    for player in allPlayers:
        soucet = 0
        pocet = 0
        for season in sheet_names:
            seasonList = dict_df.get(season)
            soucet += seasonList.loc[seasonList['PLAYER'] == player, 'STL'].sum()
            pocet += seasonList.loc[seasonList['PLAYER'] == player, 'GP'].sum()
        if (pocet > 0):
            prumer = round((soucet/pocet),2)
            stats_STL.append(prumer)
        else:
            stats_STL.append(0)
    df_allPlayers['STL'] = stats_STL
avg_steals()
print(df_allPlayers)

# %% [markdown]
# ### Function for counting of average turnovers of every player for 25 seasons

# %%
def avg_turnovers():
    stats_TOV = []
    for player in allPlayers:
        soucet = 0
        pocet = 0
        for season in sheet_names:
            seasonList = dict_df.get(season)
            soucet += seasonList.loc[seasonList['PLAYER'] == player, 'TOV'].sum()
            pocet += seasonList.loc[seasonList['PLAYER'] == player, 'GP'].sum()
        if (pocet > 0):
            prumer = round((soucet/pocet),2)
            stats_TOV.append(prumer)
        else:
            stats_TOV.append(0)
    df_allPlayers['TOV'] = stats_TOV
avg_turnovers()
print(df_allPlayers)
            

# %% [markdown]
# ### Function for counting of average blocks of every player for 25 seasons

# %%
def avg_blocks():
    stats_BLK = []
    for player in allPlayers:
        soucet = 0
        pocet = 0
        for season in sheet_names:
            seasonList = dict_df.get(season)
            soucet += seasonList.loc[seasonList['PLAYER'] == player, 'BLK'].sum()
            pocet += seasonList.loc[seasonList['PLAYER'] == player, 'GP'].sum()
        if (pocet > 0):
            prumer = round((soucet/pocet),2)
            stats_BLK.append(prumer)
        else:
            stats_BLK.append(0)
    df_allPlayers['BLK'] = stats_BLK
avg_blocks()
print(df_allPlayers)
            

# %% [markdown]
# ### Function for counting of average personal fouls of every player for 25 seasons

# %%
def avg_person_fauls():
    stats_PF = []
    for player in allPlayers:
        soucet = 0
        pocet = 0
        for season in sheet_names:
            seasonList = dict_df.get(season)
            soucet += seasonList.loc[seasonList['PLAYER'] == player, 'PF'].sum()
            pocet += seasonList.loc[seasonList['PLAYER'] == player, 'GP'].sum()
        if (pocet > 0):
            prumer = round((soucet/pocet),2)
            stats_PF.append(prumer)
        else:
            stats_PF.append(0)
    df_allPlayers['PF'] = stats_PF
avg_person_fauls()
print(df_allPlayers)
            
    

# %% [markdown]
# ### Function for counting of average +/- of every player for 25 seasons

# %%
def avg_plus_minus():
    stats_PLMIN = []
    for player in allPlayers:
        soucet = 0
        pocet = 0
        for season in sheet_names:
            seasonList = dict_df.get(season)
            soucet += seasonList.loc[seasonList['PLAYER'] == player, '+/-'].sum()
            pocet += seasonList.loc[seasonList['PLAYER'] == player, 'GP'].sum()
        if (pocet > 0):
            prumer = round((soucet/pocet),2)
            stats_PLMIN.append(prumer)
        else:
            stats_PLMIN.append(0)
    df_allPlayers['+/-'] = stats_PLMIN
avg_plus_minus()
print(df_allPlayers) 

# %% [markdown]
# ### Function for counting of the ratio of the player's time played to the total time (%) of every player for 25 seasons

# %%
def return_max_GP():
    seasonGamesCount = 0
    for season in sheet_names:
        seasonList = dict_df.get(season)    
        seasonGamesCount += seasonList['GP'].max()
    return seasonGamesCount      
returnIS = return_max_GP()
    
def minutes_played():
    stats_MIN = []
    for player in allPlayers:
        pocetMinut = 0 
        maxPocet = return_max_GP()  
        maxOdehPocet = maxPocet * 48
        for season in sheet_names:
            seasonList = dict_df.get(season)
            pocetMinut += seasonList.loc[seasonList['PLAYER'] == player, 'MIN'].sum()    
        min = round((pocetMinut/maxOdehPocet),2)     
          
        stats_MIN.append(min)    
    df_allPlayers['MIN'] = stats_MIN
minutes_played()
print(df_allPlayers)
    

# %% [markdown]
# ### Write whole DataFrame into .xlsx file

# %%
import pandas as pd

with pd.ExcelWriter('excelFiles/stats.xlsx', engine='openpyxl', mode='a', if_sheet_exists='overlay') as writer: 
    df_allPlayers.to_excel(writer, sheet_name="all_players", index=False)
print('Written into .xlsx') 


