---
title: Analyse exploratoire des données
---
### Cette page offre une visualisation globale des données, ces données sont mis à jours tous les x temps


```sql global_cards
SELECT
    COUNT(*) as nb_heroes,
    COUNT(DISTINCT publisher) as nb_publishers,
    MAX(Date_last_updated) as last_update
FROM lecsv.characters_df3
```
<BigValue
    data={global_cards}
    value=nb_heroes
    fmt=number0
    title="Nombre de superhéros"
    minWidth="200px"
/>
<BigValue 
    data={global_cards} 
    value=nb_publishers
    title="Nombre de maisons d'édition"
    minWidth="300px"
/>
<BigValue 
    data={global_cards} 
    value=last_update
    title="Dernière mise à jour"
    minWidth="100px"
/>

```sql superhero_per_publisher
SELECT publisher as name, COUNT(*) as value
FROM lecsv.characters_df3
GROUP BY publisher
HAVING publisher != 'NA'
LIMIT 5
```

```sql gender_barplot
SELECT
    Gender as gender,
    COUNT(*) as nb_superhero
FROM lecsv.characters_df3
GROUP BY gender
```

```sql issue_apparence_repartition
SELECT
    Name as name,
    Count_of_issue_appearances as value
FROM lecsv.characters_df3
ORDER BY Count_of_issue_appearances DESC
LIMIT 5
```

<Grid cols=2>
    <ECharts config={
    {
        tooltip: {
            formatter: '{b}: {c} ({d}%)'
        },
      series: [
        {
          type: 'pie',
          radius: ['40%', '70%'],
          data: issue_apparence_repartition,
        }
      ]
      }
    }
    />

    <ECharts config={
    {
        tooltip: {
            formatter: '{b}: {c} ({d}%)'
        },
      series: [
        {
          type: 'pie',
          radius: ['40%', '70%'],
          data: superhero_per_publisher,
        }
      ]
      }
    }
    />
</Grid>

```sql nb_superhero_created_per_decade
SELECT
    YEAR("First Appearance Date") - (YEAR("First Appearance Date") % 10) AS decade,
    COUNT(*) as nb_superhero
FROM lecsv.characters_df3
GROUP BY decade
ORDER BY decade
```
<BarChart
    data={nb_superhero_created_per_decade}
    x=decade
    y=nb_superhero
/>


/>

 ```sql best_heroes_STR
SELECT 
    Name as name_char, 
    STR as STR,
    (SELECT AVG(STR) FROM lecsv.characters_df3) as mean_STR
FROM lecsv.characters_df3
WHERE STR = (SELECT MAX(STR) FROM lecsv.characters_df3)
order by Mean_Stats DESC
LIMIT 1
```

```sql best_heroes_STR
SELECT 
    mean_stats as Mean_Stats, 
    STR,
    Name as name_char
FROM lecsv.characters_df3
```

```sql best_heroes_DEX
SELECT 
    mean_stats as Mean_Stats, 
    DEX,
    Name as name_char
FROM lecsv.characters_df3
```

```sql best_heroes_CON
SELECT 
    mean_stats as Mean_Stats, 
    CON,
    Name as name_char
FROM lecsv.characters_df3
```

```sql best_heroes_INT
SELECT 
    mean_stats as Mean_Stats, 
    INT,
    Name as name_char
FROM lecsv.characters_df3
```

```sql best_heroes_WIS
SELECT 
    mean_stats as Mean_Stats, 
    WIS,
    Name as name_char
FROM lecsv.characters_df3
```

```sql best_heroes_DEX
SELECT 
    mean_stats as Mean_Stats, 
    DEX,
    Name as name_char
FROM lecsv.characters_df3
```

```sql best_heroes_CHA
SELECT 
    mean_stats as Mean_Stats, 
    CHA,
    Name as name_char
FROM lecsv.characters_df3
```


<Grid cols=3>
    <ScatterPlot
        data={best_heroes_STR}
        x=Mean_Stats
        y=STR
        tooltipTitle=name_char
        fmtX=number0
        fmtY=number0
        title="Force des superhéros"
    />
    <ScatterPlot
        data={best_heroes_CON}
        x=Mean_Stats
        y=CON
        tooltipTitle=name_char
        fmtX=number0
        fmtY=number0
        title="Constitution des superhéros"
    />
    <ScatterPlot
        data={best_heroes_INT}
        x=Mean_Stats
        y=INT
        tooltipTitle=name_char
        fmtX=number0
        fmtY=number0
        title="Intelligence des superhéros"
    />
    <ScatterPlot
        data={best_heroes_WIS}
        x=Mean_Stats
        y=WIS
        tooltipTitle=name_char
        fmtX=number0
        fmtY=number0
        title="Sagesse des superhéros"
    />
    <ScatterPlot
        data={best_heroes_DEX}
        x=Mean_Stats
        y=DEX
        tooltipTitle=name_char
        fmtX=number0
        fmtY=number0
        title="Sagesse des superhéros"
    />
    <ScatterPlot
        data={best_heroes_CHA}
        x=Mean_Stats
        y=CHA
        tooltipTitle=name_char
        fmtX=number0
        fmtY=number0
        title="Sagesse des superhéros"
    />
</Grid>






