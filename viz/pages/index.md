---
title: Characters Data Dashboard
---
<br/><br/>


```sql test_connection
SELECT
    *
FROM motherduck.table
LIMIT 5
```
<!-- sample_data.hn.hacker_news -->
<!-- characters_db.main.characters_df3 -->

```sql global_cards
SELECT
    COUNT(*) as nb_heroes,
    COUNT(DISTINCT publisher) as nb_publishers,
    MAX(Date_last_updated) as last_update
FROM motherduck.table
```
<BigValue
    data={global_cards}
    value=nb_heroes
    fmt=number0
    title="Characters Count"
    minWidth="200px"
/>
<BigValue 
    data={global_cards} 
    value=nb_publishers
    title="Publishers Count"
    minWidth="300px"
/>
<BigValue 
    data={global_cards} 
    value=last_update
    title="Last Update"
    minWidth="100px"
/>
<br/><br/>



```sql superhero_per_publisher
SELECT publisher as name, COUNT(*) as value
FROM motherduck.table

GROUP BY publisher
HAVING publisher != 'NA'
LIMIT 5
```

```sql gender_barplot
SELECT
    Gender as gender,
    COUNT(*) as nb_superhero
FROM motherduck.table

GROUP BY gender
```

```sql issue_apparence_repartition
SELECT
    Name as name,
    Count_of_issue_appearances as value
FROM motherduck.table

ORDER BY Count_of_issue_appearances DESC
LIMIT 5
```

<Grid cols=2>
    <BarChart
        
        data={issue_apparence_repartition}
        x=name
        y=value
        title="Top 5 characters appearances"
        swapXY=true
        colorPalette={[
        ["#1d4ed8", "#2F648E"],
    ]}
    />

    <ECharts config={
    {
        tooltip: {
            formatter: '{b}: {c} ({d}%)'
        },
        title: {
            text: 'publisher repartition',
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
FROM motherduck.table

GROUP BY decade
ORDER BY decade
```
<BarChart
    data={nb_superhero_created_per_decade}
    x=decade
    y=nb_superhero
    colorPalette={[
        ["#1d4ed8", "#2F648E"],
    ]}
    title="Characters created per decade"
/>

 ```sql best_heroes_STR
SELECT 
    Name as name_char, 
    STR as STR,
    (SELECT AVG(STR) FROM motherduck.table
) as mean_STR
FROM motherduck.table

WHERE STR = (SELECT MAX(STR) FROM motherduck.table
)
order by Mean_Stats DESC
LIMIT 1
```

```sql best_heroes_STR
SELECT 
    mean_stats as Mean_Stats, 
    STR,
    Name as name_char
FROM motherduck.table

```

```sql best_heroes_DEX
SELECT 
    mean_stats as Mean_Stats, 
    DEX,
    Name as name_char
FROM motherduck.table

```

```sql best_heroes_CON
SELECT 
    mean_stats as Mean_Stats, 
    CON,
    Name as name_char
FROM motherduck.table

```

```sql best_heroes_INT
SELECT 
    mean_stats as Mean_Stats, 
    INT,
    Name as name_char
FROM motherduck.table

```

```sql best_heroes_WIS
SELECT 
    mean_stats as Mean_Stats, 
    WIS,
    Name as name_char
FROM motherduck.table

```

```sql best_heroes_DEX
SELECT 
    mean_stats as Mean_Stats, 
    DEX,
    Name as name_char
FROM motherduck.table

```

```sql best_heroes_CHA
SELECT 
    mean_stats as Mean_Stats, 
    CHA,
    Name as name_char
FROM motherduck.table
```


<Grid cols=3>
    <ScatterPlot
        data={best_heroes_STR}
        x=Mean_Stats
        y=STR
        tooltipTitle=name_char
        fmtX=number0
        fmtY=number0
        title="Characters Strength"
    />
    <ScatterPlot
        data={best_heroes_CON}
        x=Mean_Stats
        y=CON
        tooltipTitle=name_char
        fmtX=number0
        fmtY=number0
        title="Characters Constitution"
    />
    <ScatterPlot
        data={best_heroes_INT}
        x=Mean_Stats
        y=INT
        tooltipTitle=name_char
        fmtX=number0
        fmtY=number0
        title="Characters Intelligence"
    />
    <ScatterPlot
        data={best_heroes_WIS}
        x=Mean_Stats
        y=WIS
        tooltipTitle=name_char
        fmtX=number0
        fmtY=number0
        title="Characters Wisdom"
    />
    <ScatterPlot
        data={best_heroes_DEX}
        x=Mean_Stats
        y=DEX
        tooltipTitle=name_char
        fmtX=number0
        fmtY=number0
        title="Characters Dexterity"
    />
    <ScatterPlot
        data={best_heroes_CHA}
        x=Mean_Stats
        y=CHA
        tooltipTitle=name_char
        fmtX=number0
        fmtY=number0
        title="Charcters Charisma"
    />
</Grid>






