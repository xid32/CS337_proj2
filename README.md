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
  python3 get_recipes.py url
```  
  
### Transform the recipe to vegetarian
```sh
  python3 to_veg.py
```

### Transform the recipe to meaty recipe
```sh
  python3 to_meat.py
```

### Transform the recipe to healthy recipe
```sh
  python3 to_healthy.py
```

### Transform the recipe to unhealthy recipe
```sh
  python3 to_unhealhy.py
```

### Double the amount
```sh
  python3 double_amount.py
```

### reduce the amount by half
```sh
  python3 amount_cut_half.py
```

### Change the recipe's style to Thai
```sh
  python3 to_style.py
```
### Display human-readable format
```sh
  python3 human_readable.py
```
