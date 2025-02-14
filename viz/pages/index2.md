```sql heros
SELECT
    Name as name_char
FROM lecsv.characters_df3
```

<h1 style="text-align: center;">Choose your hero</h1>

<Dropdown 
    data={heros} 
    name=hero
    value=name_char
/>

```sql hero_stats
SELECT stat, value
FROM lecsv.characters_df3
UNPIVOT (
    value FOR stat IN (STR, CHA, DEX, CON, INT, WIS)
)
WHERE Name like '${inputs.hero.value}'
```



```sql hero_image
SELECT image_medium
FROM lecsv.characters_df3
WHERE Name LIKE '${inputs.hero.value}'
```

<Grid cols=2>
    <Image 
    url={hero_image[0].image_medium}    
    description="Image du héros sélectionné" 
    height=400
    width=300
    />
    <ECharts config={
    {
        title: {
            text: 'Hero Stats',
            left: 'center',
            textStyle: { color: '#fff' } // ✅ Change la couleur du titre si nécessaire
        },
        tooltip: {
            trigger: 'item',
            formatter: '{b}: {c}'
        },
        color: ['#ff4d4d'],
        radar: {
            indicator: [
                { name: 'STR', max: 100 },
                { name: 'DEX', max: 100 },
                { name: 'CON', max: 100 },
                { name: 'INT', max: 100 },
                { name: 'WIS', max: 100 },
                { name: 'CHA', max: 100 }
            ],
            splitArea: { show: false }, // ✅ Supprime les zones grisées à l'intérieur
            axisLine: { lineStyle: { color: '#fff' } }, // ✅ Change la couleur des axes
            splitLine: { lineStyle: { color: '#fff' } }  // ✅ Change les lignes séparatrices
        },
        series: [
            {
                type: 'radar',
                data: [
                    {
                        value: hero_stats.map(item => item.value),
                        name: inputs.hero.value,
                        areaStyle: { color: 'rgba(255, 77, 77, 0.4)' },
                        lineStyle: { color: '#ff4d4d', width: 2 },
                        symbol: 'circle',
                        itemStyle: { color: '#ff4d4d' }
                    }
                ]
            }
        ]
    }
    }/>
    
</Grid>


```sql hero_description
SELECT Deck
FROM lecsv.characters_df3
WHERE Name LIKE '${inputs.hero.value}'
```
<br/><br/>
{hero_description[0].Deck}




    
```sql ennemi_stats
SELECT stat, value
FROM lecsv.characters_df3
UNPIVOT (
    value FOR stat IN (STR, CHA, DEX, CON, INT, WIS)
)
WHERE Name like '${inputs.ennemi.value}'
```

```sql ennemi
SELECT
    Name as name_char
FROM lecsv.characters_df3
```
<br/><br/>
<br/><br/>

<h1 style="text-align: center;">Choose an oppenent</h1>

<Dropdown 
    data={ennemi} 
    name=ennemi
    value=name_char
/>

```sql ennemi_image
SELECT image_medium
FROM lecsv.characters_df3
WHERE Name LIKE '${inputs.ennemi.value}'
```

<Grid cols=2>
<Image 
url={ennemi_image[0].image_medium}    
description="Image du héros sélectionné" 
height=400
width=300
/>
<ECharts config={
{
    title: {
        text: 'ennemi Stats',
        left: 'center',
        textStyle: { color: '#fff' }
    },
    tooltip: {
        trigger: 'item',
        formatter: '{b}: {c}'
    },
    color: ['#ff4d4d'],
    radar: {
        indicator: [
            { name: 'STR', max: 100 },
            { name: 'DEX', max: 100 },
            { name: 'CON', max: 100 },
            { name: 'INT', max: 100 },
            { name: 'WIS', max: 100 },
            { name: 'CHA', max: 100 }
        ],
        splitArea: { show: false }, 
        axisLine: { lineStyle: { color: '#fff' } }, 
        splitLine: { lineStyle: { color: '#fff' } }
    },
    series: [
        {
            type: 'radar',
            data: [
                {
                    value: ennemi_stats.map(item => item.value),
                    name: inputs.enemi.value,
                    areaStyle: { color: 'rgba(255, 77, 77, 0.4)' },
                    lineStyle: { color: '#ff4d4d', width: 2 },
                    symbol: 'circle',
                    itemStyle: { color: '#ff4d4d' }
                }
            ]
        }
    ]
}
}/>

</Grid>

```sql ennemi_description
SELECT Deck
FROM lecsv.characters_df3
WHERE Name LIKE '${inputs.ennemi.value}'
```
<br/><br/>
{ennemi_description[0].Deck}

```sql hero_numb
SELECT STR, DEX, CON, INT, WIS, CHA
FROM lecsv.characters_df3
WHERE Name like '${inputs.hero.value}'
```

```sql ennemi_numb
SELECT STR, DEX, CON, INT, WIS, CHA
FROM lecsv.characters_df3
WHERE Name like '${inputs.ennemi.value}'
```




