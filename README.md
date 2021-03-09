# CS337_proj2

## Setup
* ```sh
  python3 -m venv virtualenv
 
* ```sh
  source virtualenv/bin/activate
  
* ```sh
  pip install -r requirements.txt
  
## Run

### Get a recipe that you want to transform
```sh
  python3 get_recipes.py [url]
```  
  
### Transform the current recipe to vegetarian
```sh
  python3 to_veg.py
```

### Transform the current recipe to meaty recipe
```sh
  python3 to_meat.py
```

### Transform the current recipe to a healthy recipe
```sh
  python3 to_healthy.py
```

### Transform the current recipe to an unhealthy recipe
```sh
  python3 to_unhealhy.py
```

### Double the amount of the current recipe
```sh
  python3 double_amount.py
```

### reduce the amount by half of the current recipe
```sh
  python3 amount_cut_half.py
```

### Change the current recipe's style to Thai
```sh
  python3 to_style.py
```
### Display human-readable format of the current recipe
```sh
  python3 human_readable.py
```

## Note:
* The transformation is sequential. For example, if you run get_recipes.py, then to_veg.py then double_amount.py, the original recipe becomes vegetarian **and** with doubled amount 
* If you want the recipe only transformed once and see the result, you can run get_recipes.py again to start over.
