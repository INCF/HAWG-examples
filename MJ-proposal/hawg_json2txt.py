# Print out tsv file from a fulldict structure
print('HEADER')
for h in fulldict['header']:
    print('%s   %s' % (h,fulldict['header'][h]))

print('\nRESOURCES')
print('shortname	location	format	type	key_axes	nominal_resolution	name')
rd=fulldict['resources']
for r in rd:
    print('%s	%s	%s	%s	%s	%s	%s' % (r,rd[r].get('location','-'),rd[r].get('format','-'),rd[r].get('type','-'),rd[r].get('key_axes','-'),rd[r].get('nominal_resolution','-'),rd[r].get('name','-')))

print('\nSTRUCTURES')
print('shortname	access_keys	example_coord	example_color	display_name	part_of	description')
sd=fulldict['structures']
td=fulldict['tags']
for s in sd:
    rstr=""   # show access info in dictionary format (for generality)
    for k in sd[s]:
        rstr+=";"+k+":"+sd[s][k].get('key','')
    print('%s	%s	%s	%s	%s	%s	%s' % (s,rstr[1:],sd[s][k].get('example_coord','-'),sd[s][k].get('example_color','-'),td[s].get('display_name','-'),td[s].get('part_of','-'),td[s].get('description','-')))

print('\nTAGS')
print('shortname	display_name	includes	part_of	description')
for t in td:
    if t not in sd:
        print('%s	%s	%s	%s	%s' % (t,td[t].get('display_name','-'),td[t].get('includes','-'),td[t].get('part_of','-'),td[t].get('description','-')))


