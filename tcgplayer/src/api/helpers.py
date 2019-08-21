# TODO: Add unit tests
def _build_path_param_str(tuples: list):
    ''' Creates full param path string from tuples of key/value args '''
    paramstring = ''
    for i in tuples:
        substr = ''.join([i[0], i[1]])
        paramstring = ''.join([paramstring, substr])
    return paramstring
