import textwrap


def wrap1(string, width):
    new_str = ''

    wigth_el = [string[i:i + width] for i in range(0, len(string), width)]
    new_str = '\n'.join(wigth_el)
    return new_str


print(wrap1('XtkjdtrGferCyjdfDRbyjdctktyyjqVfhdtk', 4))


def wrap2(string, width):
    new_str = ''

    for ch in textwrap.wrap(string, width):
        new_str += f'{ch}\n'

    return new_str


print(wrap2('XtkjdtrGferCyjdfDRbyjdctktyyjqVfhdtk', 4))


def wrap3(string, width):
    new_str = ''
    for i, ch in enumirate(string, start=0):
        if i % width == 0:
            new_str += f"{ch}\n"
        else:
            new_str += ch

    return new_str


print(wrap3('XtkjdtrGferCyjdfDRbyjdctktyyjqVfhdtk', 4))
