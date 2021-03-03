import csv
from lispy.error import lispy_function


@lispy_function("csv:read", ["str", ""], "Reading a CSV file with a dialect")
def csv_read(args):
    with open(args[0], newline='') as csvfile:
        reader = csv.reader(csvfile, dialect=args[1])
        return list(reader)

@lispy_function("csv:write", ["str", "", "list"], "Writing a list in a CSV file with a dialect")
def csv_write(args):
    with open(args[0], 'w', newline='') as csvfile:
        writer = csv.writer(csvfile, args[1])
        writer.writerows(args[2])

@lispy_function("csv:regdialect", ["str", ""], "Registering a Dialect with a name")
def csv_regdialect(args):
    csv.register_dialect(args[0], args[1])

@lispy_function("csv:unregdialect", ["str"], "Unregistering a Dialect by it name")
def csv_unregdialect(args):
    csv.unregister_dialect(args[0])

@lispy_function("csv:getdialect", ["str"], "Getting a Dialect by it name")
def csv_getdialect(args):
    return csv.get_dialect(args[0])

@lispy_function("csv:finddialect", ["str"], "Return Dialect used in CSV File")
def csv_finddialect(args):
    with open(args[0], newline='') as csvfile:
        return csv.Sniffer().sniff(csvfile.read(1024))()

@lispy_function("csv:hasheader", ["str"], "Return if the first line of a CSV File is a header")
def csv_hasheader(args):
    with open(args[0], newline='') as csvfile:
        return csv.Sniffer().has_header(csvfile.read(1024))

@lispy_function("csv:dialect:create", [], "Creating a Dialect")
def csv_dialect_create(args):
    class dialect(csv.Dialect):
        delimiter = ','
        quotechar = '"'
        doublequote = True
        escapechar = None
        skipinitialspace = False
        lineterminator = '\r\n'
        quoting = csv.QUOTE_MINIMAL
    return dialect()

@lispy_function("csv:dialect:str", [""], "Getting dialect informations")
def csv_dialect_str(args):
    return f"Dialect(delimiter: {args[0].delimiter}, doublequote: {args[0].doublequote}, escapechar: {args[0].escapechar}, quotechar: {args[0].quotechar}, skipinitialspace: {args[0].skipinitialspace})"

@lispy_function("csv:dialect:delimiter", [""], "Getting dialect delimiter")
def csv_dialect_delimiter(args):
    return args[0].delimiter

@lispy_function("csv:dialect:setdelimiter", ["", "str"], "Setting dialect delimiter")
def csv_dialect_setdelimiter(args):
    args[0].delimiter = args[1]

@lispy_function("csv:dialect:quotechar", [""], "Getting dialect quotechar")
def csv_dialect_quotechar(args):
    return args[0].quotechar

@lispy_function("csv:dialect:setquotechar", ["", "str"], "Setting dialect quotechar")
def csv_dialect_setquotechar(args):
    args[0].quotechar = args[1]

@lispy_function("csv:dialect:escapechar", [""], "Getting dialect escapechar")
def csv_dialect_escapechar(args):
    return args[0].escapechar

@lispy_function("csv:dialect:setescapechar", ["", "str"], "Setting dialect escapechar")
def csv_dialect_setescapechar(args):
    args[0].escapechar = args[1]

@lispy_function("csv:dialect:doublequote", [""], "Getting dialect doublequote")
def csv_dialect_doublequote(args):
    return args[0].doublequote

@lispy_function("csv:dialect:setdoublequote", ["", "bool"], "Setting dialect doublequote")
def csv_dialect_setdoublequote(args):
    args[0].doublequote = args[1]

@lispy_function("csv:dialect:skipinitialspace", [""], "Getting dialect skipinitialspace")
def csv_dialect_skipinitialspace(args):
    return args[0].delimiter

@lispy_function("csv:dialect:setskipinitialspace", ["", "bool"], "Setting dialect skipinitialspace")
def csv_dialect_setskipinitialspace(args):
    args[0].skipinitialspace = args[1]
