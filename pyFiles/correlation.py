# %% [markdown]
# # Correlation plots

# %%
%pip install seaborn

# %% [markdown]
# ### Creating of correlation with plot representation

# %%
import pandas as pd
import seaborn as sns
from matplotlib import pyplot as plt

plt = plt.figure()
df = pd.read_excel('excelFiles/stats.xlsx', sheet_name="2020-21")

sns.set(rc={'figure.figsize':(15,10)})
sns.regplot(x=df["GP"], y=df['PTS']).set(title="Graf korelace mezi odehranými zápasy a body hráčů v sezoně 2020-2021")
plt.savefig("plots/correlation/GP x PTS.png")

# %% [markdown]
# ### Write all correlation plots into own .xlsx file

# %%
import openpyxl

wrkb = openpyxl.Workbook()
  
ws = wrkb.worksheets[0]
img = openpyxl.drawing.image.Image('plots/correlation/GP x FGM.png')
img2 = openpyxl.drawing.image.Image('plots/correlation/GP x MIN.png')
img3 = openpyxl.drawing.image.Image('plots/correlation/GP x PF.png')
img4 = openpyxl.drawing.image.Image('plots/correlation/GP x PTS.png')
img5 = openpyxl.drawing.image.Image('plots/correlation/MIN x PF.png')
img6 = openpyxl.drawing.image.Image('plots/correlation/MIN x PTS.png')
img7 = openpyxl.drawing.image.Image('plots/correlation/PTS x MIN.png')

img.anchor = 'A1'
img2.anchor = 'R1'
img3.anchor = 'A40'
img4.anchor = 'R40'
img5.anchor = 'A80'
img6.anchor = 'R80'
img7.anchor = 'A120'

ws.add_image(img)
ws.add_image(img2)
ws.add_image(img3)
ws.add_image(img4)
ws.add_image(img5)
ws.add_image(img6)
ws.add_image(img7)
wrkb.save('excelFiles/plots_correlation.xlsx')
print('All correlation plots were saved')


