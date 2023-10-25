import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import psycopg2

sns.set(color_codes=True)

# Деректер қорына қосылу
conn = psycopg2.connect(
    dbname="data_analysis",
    user="postgres",
    password="2003",
    host="localhost"
)

# Данныйға запрос тастау
query = "SELECT * FROM mtcars;"
df = pd.read_sql_query(query, conn)

# Вариант 2:CSV файлдан запрос тастау
# df = pd.read_csv('mtcars.csv', sep=',')

print(len(df))
print(df.head())

# Ең баяу машинаны табу 'qsec'
min_qsec_cars = df[df['qsec'] == df['qsec'].min()]
print('Самая медленная машина по времени квартер-майла:')
print(min_qsec_cars)

# Двигателі кіші машинаны табу 'disp'
min_disp_cars = df[df['disp'] == df['disp'].min()]
print('Машина с минимальным объемом двигателя:')
print(min_disp_cars)

# Данныйдың формасы туралы ақпаратты шығару
df_shape = df.shape
print("Количество строк и столбцов в данных:", df_shape)

# Бағандағы данныйдың типін шығару
df_types = df.dtypes
print("Типы данных в столбцах:\n", df_types)

# Поиск и удаление дубликатов 
duplicate_rows_df = df[df.duplicated()]
print(f"Количество дубликатов: {duplicate_rows_df.shape[0]}")
df = df.drop_duplicates()

# Бос емес бағандардың саның шығару
df_count = df.count()
print("Количество непустых значений в каждом столбце:\n", df_count)

#\\
Q1 = df.quantile(0.25)
Q3 = df.quantile(0.75)
IQR = Q3 - Q1
print("Межквартильные диапазоны:\n", IQR)

# Фильтрация данных
filtered_df = df[~((df < (Q1 - 1.5 * IQR)) | (df > (Q3 + 1.5 * IQR)).any(axis=1)]
filtered_df_shape = filtered_df.shape
print("Размерность данных после фильтрации:", filtered_df_shape)


plt.figure(figsize=(10, 5))
correlation_matrix = df.corr()
sns.heatmap(correlation_matrix, cmap="BrBG", annot=True)
plt.show()

#'hp' и 'qsec'
fig, ax = plt.subplots(figsize=(10, 6))
ax.scatter(df['hp'], df['qsec'])
ax.set_xlabel('HP')
ax.set_ylabel('Qsec')
plt.show()
