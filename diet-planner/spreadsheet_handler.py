class SpreadsheetHandler:
    """Handler for getting data from spreadsheet with Google Sheets API"""
    SPREADSHEET_ID:str

    def __init__(self, spreadsheet_id:str) -> None:
        """Sets up credentials if using Google Sheets (local .xml file support not yet implemented)"""
        self.SPREADSHEET_ID = spreadsheet_id

    def get(self, range_name) -> list:
        """Takes either str range (for single) or list range (for batch results) and returns a list of values"""
        pass
