from kgforge.core.storing import Store


class RdflibGraph(Store):

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        print("FIXME - RdflibGraph")
