# juan

bag view
item view

item can be in many bags
bag can have many items

what about item quantities - different quantites per bag, how would that work?
can items be grouped/associated with each other in 'kits'?
some sort of source control so you can go back to previous bags?
 
## MVP

### MODELS
item model:
name
description
category
bags

pack model:
name
description
bag
items

bag model:
name
description
dimensions

### VIEWS

home - select a pack

pack view - like lighterpack

item view -list sorted into categories
click into an item
add or remove it from bags

## LATER

item - dimensions, weight
bag - days, weather, location