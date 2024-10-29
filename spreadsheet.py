
class SpreadSheet:

    def __init__(self):
        self._cells = {}
        self._evaluating = set()

    def set(self, cell: str, value: str) -> None:
        self._cells[cell] = value

    def get(self, cell: str) -> str:
        return self._cells.get(cell, '')

    def evaluate(self, cell: str) -> int | str:
        if cell in self._evaluating:
            return "#Circular"
        self._evaluating.add(cell)
        
        value = self.get(cell)
        if value.isdigit():
            result = int(value)
        elif value.startswith("'") and value.endswith("'"):
            result = "#Error"
        elif value.startswith("="):
            if value[1:].isdigit():
                result = value[1:]
            elif value[1:].startswith("'") and value[1:].endswith("'"):
                result = value[2:-1]
            elif value[1:] in self._cells:
                result = self.evaluate(value[1:])
            elif '+' in value or '*' in value or '/' in value:
                try:
                    result = str(eval(value[1:], {}, {}))
                except:
                    result = "#Error"
            else:
                result = "#Error"
        else:
            try:
                float(value)
                result = "#Error"
            except ValueError:
                result = "#Error"
        
        self._evaluating.remove(cell)
        return result

