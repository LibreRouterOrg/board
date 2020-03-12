#
# Example python script to generate a BOM from a KiCad generic netlist
#
# Example: Sorted and Grouped CSV BOM
#

FIELDS = [
    ('Value', lambda c: c.getValue()), 
    ('Cmp name', lambda c: c.getPartName()), 
    ('Manufacturer', None), 
    ('Manufacturer PN', None),
    ('Supplier', None),
    ('Supplier PN', None),
    ('DNP', None),
    ('Footprint', lambda c: c.getFootprint()),
    ('Description', lambda c: c.getDescription()),
]

FIELD_NAMES = [f[0] for f in FIELDS]

def get_value(component, field):
    if field[1] is None:
        return component.getField(field[0])
    else:
        return field[1](component)

"""
    @package
    Generate a comma delimited list (csv file type).
    Components are sorted by ref and grouped by value with same footprint.
    Components with DNP field (do not place) are also grouped.
    Fields are (if exist)
    'Ref', 'Qnty', and fields defined in FIELDS list

    Command line:
    python "pathToFile/bom_csv_grouped_by_value_with_fp.py" "%I" "%O.csv"
""" 

import sys

sys.path.append("/usr/share/kicad/plugins/")
# Import the KiCad python helper module and the csv formatter
import kicad_netlist_reader
import csv

# Generate an instance of a generic netlist, and load the netlist tree from
# the command line option. If the file doesn't exist, execution will stop
net = kicad_netlist_reader.netlist(sys.argv[1])

# Open a file to write to, if the file cannot be opened output to stdout
# instead
try:
    f = open(sys.argv[2], 'w')
except IOError:
    e = "Can't open output file for writing: " + sys.argv[2]
    print(__file__, ":", e, sys.stderr)
    f = sys.stdout

# Create a new csv writer object to use as the output formatter
out = csv.writer(f, lineterminator='\n', delimiter=',', quotechar='\"', quoting=csv.QUOTE_ALL)


# Output a set of rows for a header providing general information
out.writerow(["%s, %s, %s, %s, %s" % (net.getSource(), net.getDate(), net.getTool(), sys.argv[0], len(net.components))])
out.writerow(['Ref', 'Qnty'] + FIELD_NAMES)

# Get all of the components in groups of matching parts + values
# (see ky_generic_netlist_reader.py)
grouped = net.groupComponents()

# Output all of the component information
for group in grouped:
    refs = ""

    # Add the reference of every component in the group and keep a reference
    # to the component so that the other data can be filled in once per group
    c = None
    for component in group:
        if not component.getField("DNP"):
            refs += component.getRef() + ", "
            c = component
    if c is not None:
        out.writerow([refs, len(group)] + [get_value(c, field) for field in FIELDS])

# Output all of the component information
for group in grouped:
    refs = ""

    # Add the reference of every component in the group and keep a reference
    # to the component so that the other data can be filled in once per group
    c = None
    for component in group:
        if component.getField("DNP"):
            refs += component.getRef() + ", "
            c = component

    if c is not None:
        # Fill in the component groups common data
        out.writerow([refs, len(group)] + [get_value(c, field) for field in FIELDS])
