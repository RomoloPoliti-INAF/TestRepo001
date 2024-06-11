class SimbioTail:
    """SIMBIO-SYS Tail class.
    define a obserbvation window of a channel with all geometric and operative parameters"""

    __slots__ = ['instrument']

    def __init__(self,instrument:str, instrument_mode:int) -> None:
        """AI is creating summary for __init__

        Args:
            instrument (str): Name of the SIMBIO-SYS Tail
            instrument_mode (int): Mode of the acquisition (STC)
        """
        self.instrument = instrument
        self.instrument_mode=instrument_mode