# COMBO-Edit0r
Tool for editing combolists (removing duplicates, converting to user:pass, filtering emails by email service name) 
COMBO-C0rrect0r
small side tool to clean the combolist from blank lines
# Help menu
-h | --help -----> open help menu

-w  ----->  -w <path to list>                     #Always required as first arg

-d -----> removes duplicates from list


-f -----> -f <emailservice name>  
filters list by emailservice name
             

-u -----> converts email:password list to user:password list

-o -----> -o <path to save into or set txt file name that will be saved in the current dir>
          #Always required as last arg 

# Example
python COMBO-Edit0r-0.1.py -w ~/combolist.txt -d -o ~/combolist_with_no_duplicates

