from lispy.error import lispy_function
from discord import Embed


@lispy_function("lpycord:embed:create", [], "Creating Embed")
def lpycord_embed_create(args):
    return Embed()

@lispy_function("lpycord:embed:length", ["Embed"], "Getting total length of Embed (limit is 6000)")
def lpycord_embed_length(args):
    return len(args[0])

@lispy_function("lpycord:embed:title", ["Embed"], "Getting title of Embed")
def lpycord_embed_title(args):
    return args[0].title

@lispy_function("lpycord:embed:settitle", ["Embed", "str"], "Setting title of Embed")
def lpycord_embed_settitle(args):
    args[0].title = args[1]

@lispy_function("lpycord:embed:description", ["Embed"], "Getting description of Embed")
def lpycord_embed_description(args):
    return args[0].description

@lispy_function("lpycord:embed:setdescription", ["Embed", "str"], "Setting description of Embed")
def lpycord_embed_setdescription(args):
    args[0].description = args[1]

@lispy_function("lpycord:embed:url", ["Embed"], "Getting url of Embed")
def lpycord_embed_url(args):
    return args[0].url

@lispy_function("lpycord:embed:seturl", ["Embed", "str"], "Setting url of Embed")
def lpycord_embed_seturl(args):
    args[0].url = args[1]

@lispy_function("lpycord:embed:setimage", ["Embed", "str"], "Setting image of Embed")
def lpycord_embed_setimage(args):
    args[0].set_image(url=args[1])

@lispy_function("lpycord:embed:setfooter", ["Embed", "str|NoneType", "str|NoneType"], "Setting footer of Embed")
def lpycord_embed_setfooter(args):
    if args[1] is None:
        args[1] = Embed.Empty
    if args[2] is None:
        args[2] = Embed.Empty
    args[0].set_footer(text=args[1], icon_url=args[2])

@lispy_function("lpycord:embed:setthumbnail", ["Embed", "str"], "Setting thumbnail of Embed")
def lpycord_embed_setthumbnail(args):
    args[0].set_thumbnail(args[1])

@lispy_function("lpycord:embed:setauthor", ["Embed", "str"], "Setting author of Embed")
def lpycord_embed_setauthor(args):
    args[0].set_author(name=args[1])

@lispy_function("lpycord:embed:removeauthor", ["Embed"], "Remove author of Embed")
def lpycord_embed_removeauthor(args):
    args[0].remove_author()

@lispy_function("lpycord:embed:addfield", ["Embed", "str", "str"], "Add field to Embed with name and value")
def lpycord_embed_addfield(args):
    args[0].add_field(name=args[1], value=args[2], inline=False)

@lispy_function("lpycord:embed:addinlinefield", ["Embed", "str", "str"], "Add inline field to Embed with name and value")
def lpycord_embed_addinlinefield(args):
    args[0].add_field(name=args[1], value=args[2], inline=True)

@lispy_function("lpycord:embed:clearfields", ["Embed"], "Remove all fields of Embed")
def lpycord_embed_clearfields(args):
    args[0].clear_fields()