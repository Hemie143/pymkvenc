#! /usr/bin/python

'''
Takes a MKV file and make it fit to home standards

Flow
----
1. Create AVS & LWSMASH index
2. Extract Audio (handle case of multiple tracks) if not AC3
3. Convert Audio to AC3
4. Re-encode Video to size of 4480MB or multiple of 1120MB (combined with Audio) - Compute arguments
5. Mux files
 
Args
----
Anime ? 

 
Config file
-----------
Location of tools
'''

