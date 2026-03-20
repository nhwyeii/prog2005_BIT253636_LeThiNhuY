import pandas as pd
import matplotlib.pyplot as plt
data = {
    'city': ['Los Angeles', 'San Diego', 'San Jose', 'San Francisco', 'Fresno',
             'Sacramento', 'Long Beach', 'Oakland', 'Bakersfield', 'Anaheim'],
    'area_total_km2': [1302, 964, 466, 600, 298, 259, 133, 202, 384, 131]
}

df = pd.DataFrame(data)
df_sorted = df.sort_values(by='area_total_km2', ascending=False).head(10)
plt.barh(df_sorted['city'], df_sorted['area_total_km2'])
plt.gca().invert_yaxis()
plt.title('Top 10 thành phố lớn nhất California (theo diện tích)')
plt.xlabel('Diện tích (km²)')
plt.ylabel('Thành phố')

plt.show()