# Example code

###

# Extract list of structures
fulldict['structures'].keys()

###

# Extract access information and display name for each structure
[ (x,fulldict['structures'][x],fulldict['tags'][x]['display_name']) for x in fulldict['structures'] ]

###

# Extract all structures that have a particular named resource
[x for x in fulldict['structures'] if 'prob1mm' in fulldict['structures'][x]]
# .. and a less pythonic alternative (for the C++/matlab folks)
ans=[]
for x in fulldict['structures'].keys():
    if 'prob1mm' in fulldict['structures'][x]:
        ans+=[x]

###

# Extract all structures that have a resource that is discrete
structs=[]
for x in fulldict['structures']:
    if any(fulldict['resources'][z]['type']=='discrete'
           for z in fulldict['structures'][x]):
        structs += [x]

###

# All tags that (directly) include a particular structure [graph needed for full transitive closure]
[x for x in fulldict['tags']
   if 'id1_MTG' in fulldict['tags'][x].get('includes',[])]

###

# Build a graph from the tags (set of unique nodes and directed edges)
taglist = [fulldict['tags'][x].get('part_of','').split(',') + fulldict['tags'][x].get('includes','').split(',') for x in fulldict['tags']]
nodes = list(set([val for sublist in taglist for val in sublist if val!=''] + fulldict['tags'].keys()))
edges=[]
for tag in fulldict['tags'].keys():
    edges += [{y:tag} for y in fulldict['tags'][tag].get('part_of','').split(',') if y!='']
    edges += [{tag:y} for y in fulldict['tags'][tag].get('includes','').split(',') if y!='']
uniqedges=[]
for e in edges:
    if e not in uniqedges:
        uniqedges+=[e]

###
