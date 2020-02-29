from spacy.matcher import Matcher

def create_versioned(name):
    return [
        [{'LOWER': name}], 
        [{'LOWER': {'REGEX': f'({name}\d+\.?\d*.?\d*)'}}], 
        [{'LOWER': name}, {'TEXT': {'REGEX': '(\d+\.?\d*.?\d*)'}}],
    ]


def create_patterns():
    versioned_languages = ['ruby', 'php', 'python', 'perl', 'java', 'haskell', 
                           'scala', 'c', 'cpp', 'matlab', 'bash', 'delphi']
    flatten = lambda l: [item for sublist in l for item in sublist]
    versioned_patterns = flatten([create_versioned(lang) for lang in versioned_languages])

    lang_patterns = [
        [{'LOWER': 'objective'}, {'IS_PUNCT': True, 'OP': '?'},{'LOWER': 'c'}],
        [{'LOWER': 'objectivec'}],
        [{'LOWER': 'c'}, {'LOWER': '#'}],
        [{'LOWER': 'c'}, {'LOWER': 'sharp'}],
        [{'LOWER': 'c#'}],
        [{'LOWER': 'f'}, {'LOWER': '#'}],
        [{'LOWER': 'f'}, {'LOWER': 'sharp'}],
        [{'LOWER': 'f#'}],
        [{'LOWER': 'lisp'}],
        [{'LOWER': 'common'}, {'LOWER': 'lisp'}],
        [{'LOWER': 'go', 'POS': {'NOT_IN': ['VERB']}}],
        [{'LOWER': 'golang'}],
        [{'LOWER': 'html'}],
        [{'LOWER': 'css'}],
        [{'LOWER': 'sql'}],
        [{'LOWER': {'IN': ['js', 'javascript']}}],
        [{'LOWER': 'c++'}],
    ]

    return versioned_patterns + lang_patterns
