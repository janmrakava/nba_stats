# %% [markdown]
# # Initialize global variables
# 
# #### Run before work with project

# %% [markdown]
# ### Save all unique teams into DataFrame & memory

# %%
import pandas as pd
import openpyxl

dict_df = pd.read_excel('excelFiles/stats.xlsx', sheet_name=None)
%store dict_df
wb = openpyxl.load_workbook("excelFiles/stats.xlsx")
sheet_names = (wb.sheetnames)
%store sheet_names

teamsAll = []
for index in sheet_names: 
    row_sum = dict_df[index]['TEAM']
    for indexy in row_sum:
        if indexy not in teamsAll:
            teamsAll.append(indexy)
            
%store teamsAll           
df_teams = pd.DataFrame (teamsAll, columns = ['TEAM'])   
%store df_teams      

# %% [markdown]
# ### Save all unique players into DataFrame & memory

# %%
allPlayers = []
for index in sheet_names:
    seasonList = dict_df.get(index)
    players = seasonList['PLAYER']
    for player in players:
        if player not in allPlayers:
            allPlayers.append(player)
            
%store allPlayers
df_allPlayers = pd.DataFrame (allPlayers, columns = ['PLAYER'])  
%store df_allPlayers

# %% [markdown]
# ### Save all seasons into DataFrame & memory

# %%
allSeasons = []
for index in sheet_names:
    allSeasons.append(index)
    
%store allSeasons
df_allSeasons = pd.DataFrame(allSeasons, columns=['SEASON'])
%store df_allSeasons



