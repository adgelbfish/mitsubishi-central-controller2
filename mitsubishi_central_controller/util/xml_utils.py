from xmltodict import parse


def dict2xml(d, root_node=None):
    wrap = False if None == root_node or isinstance(d, list) else True
    root = 'objects' if None == root_node else root_node
    root_singular = root[:-1] if 's' == root[-1] and None == root_node else root
    xml = ''
    attr = ''
    children = []

    if isinstance(d, dict):
        # print(d)
        for key, value in dict.items(d):
            if isinstance(value, dict):
                children.append(dict2xml(value, key))
            elif isinstance(value, list):
                children.append(dict2xml(value, key))
            elif key[0] == '@':
                attr = attr + ' ' + key[1::] + '="' + str(value) + '"'
            else:
                xml = '<' + key + ">" + str(value) + '</' + key + '>'
                children.append(xml)

    else:
        # if list
        for value in d:
            children.append(dict2xml(value, root_singular))

    end_tag = '>' if 0 < len(children) else '/>'

    if wrap or isinstance(d, dict):
        xml = '<' + root + attr + end_tag

    if 0 < len(children):
        for child in children:
            xml = xml + child

        if wrap or isinstance(d, dict):
            xml = xml + '</' + root + '>'

    return xml

def build_xml(obj):
    return dict2xml(obj, root_node="Packet")


def parse_xml(xml):
    return parse(xml)
