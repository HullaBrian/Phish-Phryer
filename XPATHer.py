from bs4 import BeautifulSoup


def extract(element):
    # Code credit: ergoithz   https://gist.github.com/ergoithz/6cf043e3fdedd1b94fcf
    components = []
    child = element if element.name else element.parent
    for parent in child.parents:
        siblings = parent.find_all(child.name, recursive=False)
        components.append(
            child.name if 1 == len(siblings) else '%s[%d]' % (
                child.name,
                next(i for i, s in enumerate(siblings, 1) if s is child)
            )
        )
        child = parent
    components.reverse()
    return '/%s' % '/'.join(components)
