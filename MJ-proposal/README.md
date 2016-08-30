# HAWG-proposal-MJ

##HAWG - The Humane Atlasing Working Group - examples to illustrate a proposal by MJ (August 2016)

I've tried to reconcile the examples from the Boston meeting and also to extend some things to allow us to deal with a range of use cases (simple label atlas, probabilistic atlas, set of atlases that are linked - e.g. developmental atlases).  As part of this I have also written some python code to convert to and from a simple plain text (tsv) description and some code snippets to show how to access info in ways that developers might often want. 
 
Most of the details I think could change (especially the naming and the arrangement of the text file) but I wanted to include a full set of stuff here to illustrate how I see it working.  It also helped me to clarify some of the details myself.

I don't have strong views (mostly) on naming or implementational details, so please focus your comments primarily on the overall structure, then secondly on the implementation details and naming. Oh, and please don't laugh at my python - I'm only learning.
 
## Files

The files contained here are:
 - an example json file (sample.json); 
 - an extra json snippet showing a variant for a developments (5D) atlas (sample_mods.json); 
 - example plain text (tsv) short specification file (sample.txt); 
 - python code to convert tsv to json (hawg_txt2json.py); 
 - python snippets to show how to extract useful info from hawg python dictionary structure (example_code.py); 
 - python code to convert hawg json file to tsv file (hawg_json2txt.py).  
 
I've also written a summary of the proposed format and my rationale in coming up with it, plus a few extra bits (see below).
 
## Fundamental principles:

 - The json format (and its corresponding data structure in code) should be well suited to programmers/developers rather than end-users, although it shouldn't be so complicated/verbose that it can't be read and modified by hand.
 - Non-developers that are building atlases should interact via much simpler text file specifications, and we provide code that converts to and from json (I've included these here).  For complicated things they'll need to modify the json directly, but I think that's fine if it is only for the most advanced cases (<10% of the time).  In some cases the text might be fairly verbose, but should be straightforward to generate from excel or similar.
 - There are four main sections of information: header, resources, structures and tags
   - header: captures top-level info relevant for the whole conceptual atlas (often several related data-files)
   - resources: one per data-file/web-address/resource used to access data, each containing information needed to determine how to get the necessary data
   - structures: one per fundamental structure/unit stored by the atlas and contains only the information related to accessing that data from the resource and displaying it (other info in tags - see next)
    - tags: one per scientific region/unit/meta-object of the atlas, including one for each fundamental structure/unit (with identical short-name/id as in "structures"). This is where all the scientific information (e.g. names, references, relationships) exists and is separate from information about access and display.
 
So there is replication of structure info between "structures" and "tags" but I think it is helpful to separate data/file/storage-related issues from the scientific/conceptual info.  A simple atlas without any "tags" would still have N items in both "structures" and "tags" but this does not have to specify any relationships between them.  However, if a hierarchy (or non-hierarchical-relationship-web/mess) is specified then all the information needed to build the graph that represents this (nodes and edges) is purely within the "tags" part of the spec.
 
## Convention for interpreting key values

I would also like to re-propose the idea that values for access information, like data keys and dimension indices, are not specified/interpreted by the HAWG format but are left to match the conventions/specifications used by the format of the file that is storing the data.  So, for instance, if you have an index of 2 for a probability map (pulling out a 3D image from a 4D collection) then this means the third 3D volume of a nifti file, since the nifti coordinates start at 0, but that it might mean something different for a minc image (sorry, I don't know the minc standard) or some other image format, or a web-based interface, or whatever.  The application needs to understand the actual format and I think it is easier if it receives info that is tailored for that format, rather than having to understand/translate any additional (and I'd say unnecessary) HAWG conventions for these values.
 
