class Path:
    def __init__(self, path):
        self._path = path

    def __repr__(self):
        return "Path(%r)" % self._path

    def write_bytes(self, data):
        with open(self._path, 'wb') as f:
            return f.write(data)

    def write_text(self, data):
        with open(self._path, 'w') as f:
            return f.write(data)


Path('hi.txt').write_text('hi there')
