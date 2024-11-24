import pandas as pd
import matplotlib.pyplot as plt

df_movies = pd.read_csv('MoviesOnStreamingPlatforms_updated.csv',sep=',')
df_tvshow = pd.read_csv('tv_shows.csv',sep=',')

#getting columns name
df_movies.head().T
df_tvshow.head().T

#df_movies has more columns than tvshow, so we need to get same colunms structure

df_movies = df_movies.iloc[:,0:12]

#extracting grades from text in tv_show

df_tvshow['IMDb_fix'] = df_tvshow['IMDb'].str.slice(0,3).astype('float')
df_tvshow['Rotten_fix'] = df_tvshow['Rotten Tomatoes'].str.slice(0,3).str.rstrip('/').astype('float')

#extracting grades from movies files
df_movies['Rotten_fix'] = df_movies['Rotten Tomatoes'].str.rstrip('%').astype('float')
df_movies['IMDb_fix'] = df_movies['IMDb'].astype('float')

#adding 0 for empty values on Rotten column

df_movies['Rotten_fix'] = df_movies['Rotten_fix'].fillna(0)
df_movies['IMDb'] = df_movies['IMDb'].fillna(0)
df_tvshow['Rotten_fix'] = df_tvshow['Rotten_fix'].fillna(0)
df_tvshow['IMDb'] = df_tvshow['IMDb'].fillna(0)

df_complete['Rotten_fix'].describe()
#Merging both dataframes in 1 DF

df_complete = pd.concat([df_movies,df_tvshow],ignore_index=True)

#adding 0 for empty values on Rotten_fix column fpr merged dataframes

df_complete['Rotten_fix'] = df_movies['Rotten_fix'].fillna(0)

#renaming columnns

df_complete.rename(columns={'Prime Video':'PrimeVideo', 'Disney+':'DisneyPlus'},inplace=True)

#Assigning a classifaction if Movie is available or not in each platform

available = {1: 'Yes',
             0: 'No'}

df_complete = df_complete.assign(Netflix = df_complete.Netflix.map(available))
df_complete = df_complete.assign(Hulu = df_complete.Hulu.map(available))
df_complete = df_complete.assign(PrimeVideo = df_complete.PrimeVideo.map(available))
df_complete = df_complete.assign(DisneyPlus = df_complete.DisneyPlus.map(available))


#Checking describe for grades
df_complete['Rotten_fix'].describe().T
df_complete['IMDb_fix'].describe().T

#Classifing grades by category using percentil 95 as reference
df_complete[['Rotten_fix','IMDb_fix']].quantile(0.95)

df_complete = df_complete.assign(Categ_Rotten = pd.qcut(df_complete.Rotten_fix,q=[0,0.95,1],labels=['minors','majors'],duplicates='drop'))

df_complete = df_complete.assign(Categ_IMDb = pd.qcut(df_complete.IMDb_fix,q=[0,0.95,1],labels=['minors','majors']))

dfbestmovies = df_complete[(df_complete['Categ_Rotten']=='majors') & (df_complete['Categ_IMDb']=='majors') & (df_complete['Type'] == 0)].sort_values(['IMDb_fix','Rotten_fix'],ascending=False).head(10)
dfbesttvshows = df_complete[(df_complete['Categ_Rotten']=='majors') & (df_complete['Categ_IMDb']=='majors') & (df_complete['Type'] == 1)].sort_values(['IMDb_fix','Rotten_fix'],ascending=False).head(10)

#Generating graph

plt.figure(figsize=(10,6))
plt.bar(dfbestmovies['Title'],dfbestmovies['IMDb_fix'],color ='skyblue')
plt.xlabel('Movies')
plt.ylabel('IMDb rank')
plt.title('Top 10 Best Movies - Ranking IMDb')
plt.xticks(rotation=90)
plt.show()
