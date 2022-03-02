from spreadsheet_handler import SpreadsheetHandler

def main() -> None:
    spreadsheet_id:str = "1CPkReD-GKcWRXe20W4DRdZ_MQkCu2xZOQ481GUbM3zM"
    sheet = SpreadsheetHandler(spreadsheet_id)

    INFO_SHEET_NAME:str = "DietData"
    INFO_RANGE:str = f"{INFO_SHEET_NAME}!A4:I4"
    MEALS_RANGE:str = f"{INFO_SHEET_NAME}!B8:G14"
    MEAL_MACRO_RANGE:str = "B1:E1"

    spreadsheet_data = sheet.get([INFO_RANGE, MEALS_RANGE])


if __name__ == "__main__":
    main()