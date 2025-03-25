def standardize(originPath: str) -> str:
    nPath = originPath
    fIndex = nPath.index('.')

    if fIndex == -1:
        return nPath

    nPath = nPath[:fIndex]
    return nPath

def testStandarize():
    assert standardize("/usr/bin/../bin/./scripts/../") == "/usr/bin/"
