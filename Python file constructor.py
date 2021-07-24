# -*- coding: utf-8 -*-
"""
Created on Fri Jul 23 21:53:37 2021

@author: Cnoized
"""
for n in range(1,61):
    
    with open('Problem%d.py'%(n), 'w') as f:
        f.write("# -*- coding: utf-8 -*-\n\"\"\"\nCreated on Fri Jul 23 21:53:37 2021\n\n@author: Cnoized\n\"\"\"\n#This is for problem %d\n" % n)