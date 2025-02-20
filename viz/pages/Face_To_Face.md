```sql heros
SELECT
    Name as name_char
FROM motherduck.table
```

<h1 style="text-align: center;">Choose your character</h1>
<div style="display: flex; justify-content: center; align-items: center;">
<Dropdown 
    data={heros} 
    name=hero
    value=name_char
    defaultValue="Batman"
/>
</div>

```sql hero_stats
SELECT stat, value
FROM motherduck.table
UNPIVOT (
    value FOR stat IN (STR, CHA, DEX, CON, INT, WIS)
)
WHERE Name like '${inputs.hero.value}'
```

```sql hero_image
SELECT image_medium
FROM motherduck.table
WHERE Name LIKE '${inputs.hero.value}'
```

<Grid cols=2 style="min-height: 600px;">
    <Image 
        url={hero_image[0].image_medium} 
        height=400
        width=300
    />
    <ECharts config={
    {
        title: {
            text: 'Hero Stats',
            top: '2%',
            left: 'center',
            textStyle: { 
                color: '#fff',
                fontSize: 16,
                fontWeight: 'bold'
            }
        },
        tooltip: {
            trigger: 'item',
            formatter: '{b}: {c}'
        },
        color: ['#4d79ff'],
        grid: {
            top: '15%',
            containLabel: true
        },
        radar: {
            center: ['50%', '55%'],
            radius: '70%',
            indicator: [
                { name: 'STR', max: 100 },
                { name: 'CHA', max: 100 },
                { name: 'DEX', max: 100 },
                { name: 'CON', max: 100 },
                { name: 'INT', max: 100 },
                { name: 'WIS', max: 100 }
            ],
            splitArea: { show: false },
            axisLine: { lineStyle: { color: '#fff' } },
            splitLine: { lineStyle: { color: '#fff' } },
            name: {
                textStyle: {
                    color: '#fff',
                    fontSize: 14
                }
            }
        },
        series: [
            {
                type: 'radar',
                data: [
                    {
                        value: hero_stats.map(item => item.value),
                        name: inputs.hero.value,
                        areaStyle: { color: 'rgba(77, 121, 255, 0.4)' },
                        lineStyle: { color: '#4d79ff', width: 2 },
                        symbol: 'circle',
                        symbolSize: 6,
                        itemStyle: { color: '#4d79ff' }
                    }
                ]
            }
        ]
    }}
    style={{
        height: '500px',
        width: '100%'
    }}
    />
</Grid>


```sql hero_description
SELECT Deck
FROM motherduck.table
WHERE Name LIKE '${inputs.hero.value}'
```
<br/><br/>
{hero_description[0].Deck}




    
```sql ennemi_stats
SELECT stat, value
FROM motherduck.table
UNPIVOT (
    value FOR stat IN (STR, CHA, DEX, CON, INT, WIS)
)
WHERE Name like '${inputs.ennemi.value}'
```

```sql ennemi
SELECT
    Name as name_char
FROM motherduck.table
```
<br/><br/>

<h1 style="text-align: center;">Choose an oppenent</h1>
<div style="display: flex; justify-content: center; align-items: center;">
<Dropdown 
    data={ennemi} 
    name=ennemi
    value=name_char
    defaultValue="Superman"
/>
</div>

```sql ennemi_image
SELECT image_medium
FROM motherduck.table
WHERE Name LIKE '${inputs.ennemi.value}'
```


<Grid cols=2 style="min-height: 600px;">
    <Image 
        url={ennemi_image[0].image_medium} 
        height=400
        width=300
    />
    <ECharts config={
    {
        title: {
            text: 'Opponent Stats',
            top: '2%',
            left: 'center',
            textStyle: { 
                color: '#fff',
                fontSize: 16,
                fontWeight: 'bold'
            }
        },
        tooltip: {
            trigger: 'item',
            formatter: '{b}: {c}'
        },
        color: ['#4d79ff'],
        grid: {
            top: '15%',
            containLabel: true
        },
        radar: {
            center: ['50%', '55%'],
            radius: '70%',
            indicator: [
                { name: 'STR', max: 100 },
                { name: 'CHA', max: 100 },
                { name: 'DEX', max: 100 },
                { name: 'CON', max: 100 },
                { name: 'INT', max: 100 },
                { name: 'WIS', max: 100 }
            ],
            splitArea: { show: false },
            axisLine: { lineStyle: { color: '#fff' } },
            splitLine: { lineStyle: { color: '#fff' } },
            name: {
                textStyle: {
                    color: '#fff',
                    fontSize: 14
                }
            }
        },
        series: [
            {
                type: 'radar',
                data: [
                    {
                        value: ennemi_stats.map(item => item.value),
                        name: inputs.ennemi.value,
                        areaStyle: { color: 'rgba(77, 121, 255, 0.4)' },
                        lineStyle: { color: '#4d79ff', width: 2 },
                        symbol: 'circle',
                        symbolSize: 6,
                        itemStyle: { color: '#4d79ff' }
                    }
                ]
            }
        ]
    }}
    style={{
        height: '500px',
        width: '100%'
    }}
    />
</Grid>

```sql ennemi_description
SELECT Deck
FROM motherduck.table
WHERE Name LIKE '${inputs.ennemi.value}'
```
<br/><br/>
{ennemi_description[0].Deck}

```sql hero_numb
SELECT STR, DEX, CON, INT, WIS, CHA
FROM motherduck.table
WHERE Name like '${inputs.hero.value}'
```

```sql ennemi_numb
SELECT STR, DEX, CON, INT, WIS, CHA
FROM motherduck.table
WHERE Name like '${inputs.ennemi.value}'
```

<div style="display: flex; justify-content: center; align-items: center;">
  <LinkButton 
    url='https://superfight.streamlit.app/chatbot?tm1={inputs.hero.value}&o1={inputs.ennemi.value}'>
    FIGHT !!!
  </LinkButton>
</div>
