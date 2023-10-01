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


hierarchy order:
bag first
then items
then pack

### VIEWS

home - select a pack

pack view - like lighterpack

item view -list sorted into categories
click into an item
add or remove it from bags

### FORMS

create/update item:
name
description optional
category
packs this item is in (multiple select)

create/update bag:
name
description

create/update pack:
name
description
bag
items

## LATER

- [x] items list view to show items by category
- [x] tests
- [x] class based views
- [x] delete pack, item, bag
- [ ] item - dimensions, weight
- [ ] bag - days, weather, location
- [ ] auth, users, logins
- [ ] dockerize
- [ ] create/update item - show categories as list or allow typed entry to create a new one
- [ ] import from lighterpack
- [ ] bulk add items (no attach to pack, just add items by name and maybe description)
- [ ] replace django test style with pytest