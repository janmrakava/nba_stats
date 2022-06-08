# %% [markdown]
# # Functions for all statistic informations of teams 
# 

# %% [markdown]
# ### Number of wins / loses per teams for all seasons

# %%
import pandas as pd 

def W_L_matches(): 
    %store -r teamsAll
    %store -r df_teams
    %store -r sheet_names
    %store -r dict_df  
    stats_W = []
    stats_L = []
    stats_GP = []
    for team in teamsAll:        
        pocetWW = 0
        pocetLL = 0
        for season in sheet_names:               
            seasonList = dict_df.get(season)                   
            pocetW = seasonList.loc[seasonList['TEAM'] == team, 'W'].max()    
            pocetL = seasonList.loc[seasonList['TEAM'] == team, 'L'].max()  
            if (pd.isna(pocetW)):
                pocetW = 0
            if (pd.isna(pocetL)):
                pocetL = 0
            pocetWW += pocetW
            pocetLL += pocetL              
        stats_W.append(pocetWW)
        stats_L.append(pocetLL)  
        stats_GP.append(pocetWW+pocetLL)  
    df_teams['GP'] = stats_GP 
    df_teams['W'] = stats_W
    df_teams['L'] = stats_L
W_L_matches()
print(df_teams)  
    

# %% [markdown]
# ### Count of all scored points per team for all seasons 

# %%
def sum_team_points_all_seasons():
    stats_PTS = []
    soucet = 0    
    for team in teamsAll: 
         soucet = 0  
         for index in sheet_names:   
            seasonList = dict_df.get(index)                 
            soucet += seasonList[seasonList['TEAM']==team].sum()['PTS']
         soucet = round(soucet)
         stats_PTS.append(soucet)
         
   
    df_teams['PTS'] = stats_PTS
    
sum_team_points_all_seasons()
print(df_teams)

# %% [markdown]
# ### Average sum of points per team for all seasons (betting potencional)

# %%
def avg_points():
    stats_PTS = []
    stats_GP = []
    stats_AVGPTS = []
    prumer = 0
    for index in df_teams['PTS']:
        stats_PTS.append(index)
    for index in df_teams['GP']:
        stats_GP.append(index)
    length = range(len(stats_PTS))   
    for i in length:
        prumer = stats_PTS[i]/stats_GP[i]
        prumer = round(prumer,2)      
            
        stats_AVGPTS.append(prumer)  
    df_teams['AVGPTS'] = stats_AVGPTS        
avg_points()
print(df_teams)

# %% [markdown]
# ### Write whole DataFrame into .xlsx file

# %%
import pandas as pd

df_teams.sort_values(by=['GP'], ascending=False, inplace=True)

with pd.ExcelWriter('excelFiles/teams.xlsx', engine='openpyxl', mode='w', if_sheet_exists='overlay') as writer: 
    df_teams.to_excel(writer, sheet_name="all_teams", index=False)
print('Data written into .xlsx file')

# %% [markdown]
# ### Group by all team statistics for all season

# %%
import pandas as pd

def zkousim_groupby():
    %store -r sheet_names
    %store -r dict_df
    for season in sheet_names:
        seasonList = dict_df.get(season)
        dff = seasonList.groupby('TEAM').mean().round(2)
        with pd.ExcelWriter('excelFiles/groupByTeams.xlsx', engine='openpyxl', mode='a', if_sheet_exists='replace') as writer:
            dff.to_excel(writer, sheet_name=season, index=False)
zkousim_groupby()
print('Data written into .xlsx file')


