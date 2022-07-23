## overview
this is example which merge 2 json and output csv.

dev.json
```
{
    "Parameters": [
        {
            "Name": "AppDebug",
            "Type": "String",
            "Value": "true",
            ・・・
    ]
}
```

prd.json
```
{
    "Parameters": [
        {
            "Name": "AppDebug",
            "Type": "String",
            "Value": "prd_true",
            ・・・
    ]
}
```

out.csv
```
Name,Type,dev_Value,prd_Value
AppDebug,String,true,true_prd
BatchAvailable,String,true,true_prd
```

## initialize
```
poetry new merge
cd merge
poetry add pandas
```

## run
```
poetry run python create_csv.py
```