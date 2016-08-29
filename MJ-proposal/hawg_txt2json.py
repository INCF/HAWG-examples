#!/usr/bin/env python
import csv
import sys

keywords=['header','resources','structures','tags']
fulldict={}
curdict={}
dictname=''
rscnames=[]
keyRowNext=False

with open(sys.argv[1],'rb') as tsvin:
    tsvin = csv.reader(tsvin, delimiter='\t')
    for row in tsvin:
      if len(row)>0 and row[0][0]!='#':   # ignore blank lines and comment lines
        if keyRowNext:
          curkeys=row
          keyRowNext=False
        elif row[0].lower() in keywords:  # Header row found
      	  #print('Keyword row found: %s' % row)
          if len(curdict.keys())>0:
            fulldict[dictname]=curdict
            curdict={}
          dictname=row[0].lower()
          if dictname!='header': keyRowNext=True
        else:
          #print('Ordinary row: %s' % row)
          if dictname=='header':   # header is different - each line is a key/value pair
              if len(row)>2:
                  curdict[row[0]]=row[1:]
              elif len(row)==2:
                  curdict[row[0]]=row[1]
          elif dictname!='':
              if len(row)<len(curkeys):
                  print('Length of line does not match header line of this section')
                  print('Line is:')
                  print(row)
                  print('header keys are: %s' % curkeys)
                  sys.exit(1)
              curdict[row[0]]={}
              if dictname=='resources':  # keep track of resources for later on
                  rscnames+=[row[0]];
              for n in range(1,len(curkeys)):
                  if row[n]!='' and row[n]!='-':
                    curdict[row[0]][curkeys[n]]=row[n]
          else:
              print('Did not find one of the section keywords: %s' % keywords)
                  
# Add last dictionary
fulldict[dictname]=curdict


# Modify dictionaries to have special features:
#  - structures also appear in tags and split entries

accesskey='access_key'
newsdict={}
strdict=fulldict.pop('structures',None)
tagdict=fulldict.pop('tags',{})
tagkeys=['display_name','includes','part_of','description']  # default
if tagdict!={}: tagkeys=tagdict[tagdict.keys()[0]].keys()
for struct in strdict.keys():
    accessinfo=strdict[struct][accesskey]
    if ';' in accessinfo:   # alternative syntax for access_key (csv list or dict-like)
        adict={}
        for dinfo in accessinfo.split(';'):
            adict[dinfo.split(':')[0]]={'key':dinfo.split(':')[1]}
        newsdict[struct] = adict
    else:
        for rkey,aval in zip(rscnames,accessinfo.split(',')):
            newsdict[struct][rkey] = {'key':aval}
    tagdict[struct]={}   # add this structure to the tags (TODO:  check it doesn't exist)
    for skey in strdict[struct].keys():
        if skey in tagkeys:
            # add this part to the tagdict entry
            tagdict[struct][skey]=strdict[struct][skey]
        else:
            if skey!=accesskey:
                # add this part to the newsdict
                for rsck in newsdict[struct]:
                    newsdict[struct][rsck].update({skey:strdict[struct][skey]})
        

fulldict['structures']=newsdict
fulldict['tags']=tagdict
                
import json
print(json.dumps(fulldict,indent=2))


